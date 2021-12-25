#! /usr/bin/env python3
import platform

from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import pyqtSlot,pyqtSignal
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView

from copy import deepcopy as copy
from PIL import Image
import pyzbar.pyzbar as zbar
from io import BytesIO
from cryptography.fernet import Fernet
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from pathlib import Path
from barcode import generate,Code128
from pyzbar.pyzbar import decode
from PIL import Image
import shutil,csv,string,requests,time,sys,os,pyqrcode,base64,json,cairosvg
from io import BytesIO,StringIO
#import pyocr
#import pyocr.builders
import pytesseract
#local import

class Signals(QObject):
    error=pyqtSignal(tuple)
    result=pyqtSignal(object)
    finished=pyqtSignal()
    stop=pyqtSignal()
    update=pyqtSignal(object)

class PollingWorker(QRunnable):
    '''worker thread'''
    def __init__(self,*args,**kwargs):
        super(PollingWorker,self).__init__()
        self.args=args
        self.kwargs=kwargs
        self.running=True
        self.signals=Signals()
        self.location=None
        self.code=None
        self.column1=None
        self.column2=None
        self.column3=None


    @pyqtSlot()
    def STOP(self):
        self.running=False

    @pyqtSlot()
    def run(self):
        #check for new messages
        if not Path(self.location.text()).exists():
            try:
                Path(self.location.text()).mkdir(parents=True)
            except Exception as e:
                print(e)
        location_count=0
        for i in Path(self.location.text()).iterdir():
            if i.is_file() and i.suffix == ".svg":
                location_count+=1
        self.signals.result.emit(
            {
            'column1':len(self.column1.toPlainText().split('\n')),
            'column2':len(self.column2.toPlainText().split('\n')),
            'column3':len(self.column3.toPlainText().split('\n'))
            }
        )
        self.signals.update.emit('codes_in_sheet: {}'.format(location_count))
        print('polling worker:',self.location.text())

        self.signals.result.emit('')

class Window(QMainWindow,QWidget):
    svg_options={'text_distance':10, 'quiet_zone':2.5, 'module_height':20,'module_width':1.08,'font_size':12}
    svg_options_file="svg_options.json"
    styles_css='styles.css'
    @pyqtSlot()
    def stop_thread(self):
        print('stop thread')
        self.worker.signals.stop.emit()

    @pyqtSlot()
    def stop(self,worker):
        worker.running=False

    def closeEvent(self, event):
        # do stuff
        print("attempting to stop closeEvent()")
        can_exit=True
        self.worker.signals.stop.emit()
        self.worker.signals.quit()
        if can_exit:
            event.accept() # let the window close
        else:
            event.ignore()
    def update_results_values(self,results):
        print(results,type(results),'self.update_results_values(results:dict())')
        if type(results) == type(dict()):
            column1_count=results.get('column1')
            column2_count=results.get('column2')
            column3_count=results.get('column3')
            self.window.column1_count.display(column1_count)
            self.window.column2_count.display(column2_count)
            self.window.column3_count.display(column3_count)
    def setup_external_worker(self,code=None,save_location=None):
        #ensures save location exists
        #automically creates filename from lineedit
        pass
        print('external worker')
        self.worker=PollingWorker()
        self.worker.location=self.window.save_location
        self.worker.column1=self.window.column1
        self.worker.column2=self.window.column2
        self.worker.column3=self.window.column3
        self.worker.signals.result.connect(self.update_results_values)
        self.worker.signals.update.connect(self.window.statusBar().showMessage)
    def getStyle(self):
        try:
            with open(self.styles_css,'r') as styles:
                style=styles.read()
            return style
        except Exception as e:
            return '''tr,th,td {
                border:1px solid black;
                    padding: 4px;
                    margin: auto;
            }
            .upc {
                display: flex;
                flex-flow: row wrap;
                align-content: center;
                align-items: center;
                justify-content: center;
                width: 250;
                margin: auto;
                overflow: auto;
                padding: 8px;
            }'''
    def generate_html(self):
        html='''
        <html>
            <head>
                <title>{title}</title>
                <style>
                    {style}
                </style>
            </head>
            <body>
                <h1>{title}</h1>
                <table>
                    <thead>
                        <tr>
                            <th>Row Number</th>
                            <th>Code 1</th>
                            <th>Code 2</th>
                            <th>Code 3</th>
                        </tr>
                    </thead>
                    <tbody>
                        {rows}
                    </tbody>
                </table>
            </body>
        </html>
        '''
        rows=[]
        '''
        style=\'\'\'
            tr,th,td {
                border:1px solid black;
                    padding: 4px;
                    margin: auto;
            }
            .upc {
                display: flex;
                flex-flow: row wrap;
                align-content: center;
                align-items: center;
                justify-content: center;
                width: 250;
                margin: auto;
                overflow: auto;
                padding: 8px;
            }
        \'\'\'
        '''
        style=self.getStyle()
        for num,i in enumerate(Path(self.window.save_location.text()).iterdir()):
            print(i)
            if i.is_file() and i.suffix == '.svg':
                h='''
            <tr>
                <th>{num}</th>
                <td>{name}</th>
                <td><div class="upc">{alt}</div></td>
                <td><div class='code2'>{code2}</div></td>
            </tr>
                '''.format(alt=i.open('r').read(),name=i.stem.split('_')[0],num=num,code2=i.stem.split('_')[-1])
                rows.append(h)
        #html.format(rows='\n'.join(rows),)
        on=Path(self.window.save_location.text())/Path(self.window.ordersheet_name.text())
        with open(on,'w') as x:
            x.write(html.format(title=self.window.order_sheet_title.text(),style=style,rows='\n'.join(rows)))
        self.window.file_saved_path.setText('file://'+str(on.absolute()))
    def update_svg_options(self):
        with open(self.svg_options_file,'r') as options:
            self.svg_options=json.load(options)
    def santize(self,stringy,codes2='NOCODE2'):
        temp=copy(stringy)
        if codes2 == '':
            codes2='NOCODE2'
        codes2_temp=copy(codes2)
        for i in string.punctuation:
            if i not in ['-','_']:
                temp=temp.replace(i,'_')
                codes2_temp=codes2_temp.replace(i,' ')
            #print(i,codes2_temp,temp)
        return '{temp}_{codes2}'.format(temp=temp,codes2=codes2_temp)
    def import_codes(self):
        self.update_svg_options()
        try:
            with open(self.window.import_file.text(),'r') as x:
                reader=csv.reader(x,delimiter=',')
                for num,i in enumerate(reader):
                    self.window.statusBar().showMessage('working on import: {}'.format(num))
                    if self.window.sorterHB1.isChecked():
                        tmp=['','','']
                        index_to_pop=None
                        indexes=[0,2]
                        for num,ii in enumerate(i):
                            try:
                                int(ii)
                                tmp[1]=ii
                                print(ii,i,tmp,'sorting')
                                index_to_pop=num
                            except:
                                pass
                        i.pop(index_to_pop)
                        for num,iii in enumerate(i):
                            tmp[indexes[num]]=iii

                        print(ii,i,tmp,'sorting','index {}'.format(indexes))
                        indexes.pop(0)
                        i=tmp
                        print(tmp,'#WORK#')
                    elif self.window.sorterHB2.isChecked():
                        print(i)
                        tmp=['','','']
                        for num_i,column in enumerate(i):
                            if len(column) == 8:
                                try:
                                    int(column)
                                    tmp[1]=column
                                except:
                                    tmp[2]=column
                            else:
                                try:
                                    int(column)
                                    tmp[0]=column
                                except:
                                    tmp[2]=column
                        print(tmp)
                        if tmp[1] == '':
                            tmp[1]='0'*8
                        i=tmp
                    elif self.window.sorterHB3.isChecked():
                        print(i,'virgin')
                        tmp=['','','']
                        for num_i,column in enumerate(i):
                            if len(column) <= 8:
                                if column == 'NOCODE2':
                                    tmp[1]=column
                                elif column == 'NOCODE1':
                                    tmp[0]=column
                                elif column == 'NOCODE3':
                                    tmp[2]=column
                                else:
                                    try:
                                        int(column)
                                        tmp[1]=column
                                    except:
                                        tmp[2]=column
                            else:
                                try:
                                    int(column)
                                    tmp[0]=column
                                except:
                                    tmp[2]=column
                            if tmp[1] == '':
                                tmp[1]='0'*8
                            i=tmp
                            print(tmp,'alter')
                    code=i[self.window.upc_col.value()]
                    print(code,'#code#')
                    code_name=self.window.save_location.text()+"/"+self.santize(i[self.window.item_name_col.value()],i[self.window.codes2_col.value()])
                    print(code_name)
                    #generate('Code128',output=code_name,code=self.window.code.text())
                    z=Code128(code)
                    z.save(options=self.svg_options,filename=code_name)

                    #self.window.code.setText('')
                    if self.window.saveOnServer_import.isChecked():
                        self.save_on_server(i)
                        print(i,'import row(3)')

        except Exception as e:
            print(e)
            raise e
    def browse_server_export(self):
        name=QFileDialog.getSaveFileName(filter="CSV (*.csv);;All Files(*)")[0]
        if name not in ['','.']:
            if Path(name).suffix != '.csv':
                name=name+".csv"
            self.window.server_export_file.setText(name)
    def export_server_csv(self):
        if self.window.server_export_file.text() != '' and not Path(self.window.server_export_file.text()).is_dir():
            address=self.get_server_address(alt='/export_server/')[0]
            token=self.get_server_address(alt='/export_server/')[1]
            response=requests.get(address,headers={'authorization':'Token {}'.format(token)})
            JSON=response.json()
            print(JSON)
            with open(self.window.server_export_file.text(),'w') as exporter:
                writer=csv.writer(exporter,delimiter=',')
                for row in JSON['export']:
                    x=[row[i] for i in row.keys()]
                    writer.writerow(x)

    def nocode1(self,btn):
        if btn == True:
            self.window.code.setText('NOCODE1')
        else:
            self.window.code.setText('')
    def nocode2(self,btn):
        if btn == True:
            self.window.code2.setText('NOCODE2')
        else:
            self.window.code2.setText('')
    def nocode3(self,btn):
        if btn == True:
            self.window.item_name.setText('NOCODE3')
        else:
            self.window.item_name.setText('')

    def generate_bar(self):
        self.update_svg_options()
        print(self.window.code.text())
        if self.window.item_name.text() == '':
            code_name=self.window.save_location.text()+"/"+self.santize(self.window.code.text(),self.window.code2.text())
        else:
            code_name=self.window.save_location.text()+"/"+self.santize(self.window.item_name.text(),self.window.code2.text())
        #generate('Code128',output=code_name,code=self.window.code.text())
        z=Code128(self.window.code.text())
        skip_next=False
        try:
            z.save(options=self.svg_options,filename=code_name)
        except Exception as e:
            print(e)
            skip_next=True
        if not skip_next and self.window.saveOnServer.isChecked():
            row=[self.window.code.text(),self.window.code2.text(),self.window.item_name.text()]
            self.save_on_server(row)
            print(row)
        if not skip_next:
            self.window.code.setText('')
            self.window.code2.setText('')
            self.window.item_name.setText('')
    def export_to_csv(self):
        entries=[]
        for i in Path(self.window.save_location.text()).iterdir():
            if i.suffix == ".svg":
                self.window.statusBar().showMessage('Exporting [READ] {}'.format(i))
                out = BytesIO()
                cairosvg.svg2png(url=str(i), write_to=out)
                image = Image.open(out)

                result=decode(image)[0]
                entries.append([i.stem.split('_')[0],result.data.decode('utf-8'),str(i.stem.split('_')[-1])])
        with open(Path(self.window.export_file.text()),'w') as out:
            writer=csv.writer(out)
            for i in entries:
                for num,col in enumerate(i):
                    for char in col:
                        if bytes(char,'utf-8') not in bytes(string.ascii_letters+string.digits,'utf-8'):
                            x=bytes(col,'utf-8').replace(bytes(char,'utf-8'),b' ')
                            i[num]=x.decode('utf-8')
                            #col[num]=str(x)
                            #col[num]=x.decode('utf-8')
                            #print(bytes(char,'utf-8'))
                            print(col)
                writer.writerow(i)
                self.window.statusBar().showMessage('Exporting [WRITING] {}'.format(i))
    def get_export(self):
        name=QFileDialog.getSaveFileName(filter="CSV (*.csv);;All Files(*)")[0]
        if name not in ['','.']:
            self.window.export_file.setText(name)
    def get_save_location(self):
        dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', '.')
        print(dir,'DIR')
        if dir:
            self.window.save_location.setText(dir)
    def clear_save_location_f(self):

        '''
        def delete(button):
            print(button,QMessageBox.StandardButton.Ok)

        msg=QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setText('You are about to delete "{}"! Are you sure?'.format(self.window.save_location.text()))
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        msg.buttonClicked.connect(delete)
        rval=msg.exec()
        print(rval)
        '''
        rval=QMessageBox.question(self,'Delete','Are you sure you want to clear "{}"?'.format(self.window.save_location.text()),QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,QMessageBox.StandardButton.No)
        print(rval)
        if self.window.save_location.text() != '/':
            if rval == QMessageBox.StandardButton.Yes:
                shutil.rmtree(self.window.save_location.text())
            else:
                self.window.statusBar().showMessage('user canceled delete')
    def aboutMe(self,x):
        print('About run()')
        msgBox = QMessageBox()
        #msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("""Home2Bar Qt6
        About: Convert Coded data to barcodes
        Version: {version}
        Import File Formats:
            Text/csv:
                - 1 Column = Column 1 is Item Code
                - 2 Columns = Column 1 is Item Name, Column 2 is Item Code
        """.format(version=Path('version.txt').open('r').readline()))
        msgBox.setWindowTitle("Home2Bar About")
        returnValue = msgBox.exec()
    def setup_buttons(self):
        self.window.submit.clicked.connect(
            self.generate_bar                )
        self.window.browse_save_location.clicked.connect(self.get_save_location)
        self.window.gen_sheet.clicked.connect(self.generate_html)
        self.window.import_f.clicked.connect(self.import_codes)
        self.window.browse_import_codes_file.clicked.connect(self.get_import_file)
        self.window.clear_save_location.clicked.connect(self.clear_save_location_f)
        self.window.export_2.clicked.connect(self.export_to_csv)
        self.window.action_About.triggered.connect(self.aboutMe)
        self.window.load.clicked.connect(self.ImageToText)
        self.window.browse_image_file.clicked.connect(self.get_image_file)
        self.window.Save.clicked.connect(self.save_image_content)
        self.window.content_ready.clicked.connect(self.copy_content)
        self.window.clear_columns.clicked.connect(self.clear_columns_f)
        self.window.browse_export.clicked.connect(self.get_export)
        self.window.test_connection.clicked.connect(self.test_connection)
        self.window.save_server.clicked.connect(self.save_server)
        self.window.export_to_file.clicked.connect(self.export_server_csv)
        self.window.browse_server_export.clicked.connect(self.browse_server_export)
        self.window.noCode1.toggled.connect(self.nocode1)
        self.window.noCode2.toggled.connect(self.nocode2)
        self.window.noCode3.toggled.connect(self.nocode3)

    def get_server_address(self,alt='/test_connection/'):
        protocol=self.window.server_http.currentText()
        address=self.window.server_address.text()
        token=self.window.token.text()
        addressStr='{proto}{address}{alt}'.format(alt=alt,proto=protocol,address=address)
        return addressStr,token

    def test_connection(self):
        addressStr=self.get_server_address()[0]
        token=self.get_server_address()[1]
        response=requests.get(addressStr,headers={'authorization':'Token {}'.format(token)})
        self.window.statusBar().showMessage(str(response))
        print(addressStr)

    def save_on_server(self,row):
        address=self.get_server_address(alt='/insert_row/')[0]
        token=self.get_server_address(alt='/insert_row/')[1]
        response=requests.post(address,headers={'authorization':'Token {}'.format(token)},json=row)
        self.window.statusBar().showMessage(str(response))

    def clear_columns_f(self):
        self.window.column1.setPlainText('')
        self.window.column2.setPlainText('')
        self.window.column3.setPlainText('')

    def copy_content(self):
        try:
            text=self.window.image_content.toPlainText()
            t=text.split('\n')
            col1=[]
            col2=[]
            col3=[]

            for i in t:
                tt=i.split(' ')
                if len(tt) >= 3:
                    print(tt[2:])
                    col1.append(tt[0])
                    col2.append(tt[1])
                    col3.append(' '.join(tt[2:]))
            self.window.column1.setPlainText('\n'.join(col1))
            self.window.column2.setPlainText('\n'.join(col2))
            self.window.column3.setPlainText('\n'.join(col3))
            self.window.image_content.setPlainText('')
        except Exception as e:
            print(e)
            self.window.statusBar().showMessage('Nothing to Copy')

    def save_image_content(self):
        try:
            col1=self.window.column1.toPlainText().split('\n')
            col2=self.window.column2.toPlainText().split('\n')
            col3=self.window.column3.toPlainText().split('\n')
            text=[]
            if len(col1) != len(col2) and len(col1) != len(col3):
                self.window.statusBar().showMessage('rows do not match')
                return
            for num,i in enumerate(col1):
                text.append([col1[num],col2[num],col3[num]])
            with open(self.window.image_file.text()+".csv","w") as out:
                writer=csv.writer(out)
                writer.writerows(text)
            self.window.statusBar().showMessage('Data Successfully Written')
            self.window.file_saved_path.setText(self.window.image_file.text()+".csv")
        except Exception as e:
            print(e)
            print(len(col1),col1,len(col2),col2,len(col3),col3)


    def get_image_file(self):
        import_file=QFileDialog.getOpenFileName(filter="PNG Files (*.png *.PNG);;JEPG Files (*.jpg *.JPG *.JPEG,*.jpeg);;All Files(*)")
        print(import_file)
        if import_file[0]:
            self.window.image_file.setText(import_file[0])


    def get_import_file(self):
        import_file=QFileDialog.getOpenFileName(filter="CSV Files (*.csv);;Text Files (*.txt);;All Files(*)")
        print(import_file)
        if import_file[0]:
            self.window.import_file.setText(import_file[0])

    def run_pollthread(self):
        code=self.window.code.text()
        codetemp=''
        for i in code:
            if i in string.ascii_lowercase+string.digits:
                codetemp+=i
        save_location=self.window.save_location.text()

        self.setup_external_worker(codetemp,save_location)
        self.threadpool.start(self.worker)

    def ImageToText(self):
        try:
            #replace with shell version
            #tools=pyocr.get_available_tools()
            #t0=tools[0]
            #self.window.content_preview.setPixmap(QPixmap(self.window.image_file.text()))
            #self.window.image_prewview


            pix = QPixmap(self.window.image_file.text())
            item = QGraphicsPixmapItem(pix)

            scene = QGraphicsScene(self)
            scene.addItem(item)

            self.window.image_preview.setScene(scene)

            image=Image.open(self.window.image_file.text())
            text=pytesseract.image_to_string(image)
            #t0.image_to_string(image)
            self.window.image_content.setPlainText(text)
        except Exception as e:
            print(e)
            self.window.statusBar().showMessage(str(e))

    def load_server_config(self):
        try:
            with open('server.json') as config:
                config=json.load(config)
                self.window.server_address.setText(config.get("address"))
                self.window.token.setText(config.get("token"))
                self.window.server_http.setCurrentText(config.get("protocol"))
        except Exception as e:
            config={"address": "127.0.0.1:8000/h2bs", "token": "\t1cd0130cc8870ddc77abd1b08df634c2ba46ea01", "protocol": "http://"}
            self.window.server_address.setText(config.get("address"))
            self.window.token.setText(config.get("token"))
            self.window.server_http.setCurrentText(config.get("protocol"))

    def save_server(self):
        with open('server.json','w') as config:
            data=dict(address=self.window.server_address.text(),token=self.window.token.text(),protocol=self.window.server_http.currentText())
            json.dump(data,config)


    ui='''PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHVpIHZlcnNpb249IjQuMCI+
CiA8Y2xhc3M+SG9tZTJCYXI8L2NsYXNzPgogPHdpZGdldCBjbGFzcz0iUU1haW5XaW5kb3ciIG5h
bWU9IkhvbWUyQmFyIj4KICA8cHJvcGVydHkgbmFtZT0id2luZG93TW9kYWxpdHkiPgogICA8ZW51
bT5RdDo6Tm9uTW9kYWw8L2VudW0+CiAgPC9wcm9wZXJ0eT4KICA8cHJvcGVydHkgbmFtZT0iZ2Vv
bWV0cnkiPgogICA8cmVjdD4KICAgIDx4PjA8L3g+CiAgICA8eT4wPC95PgogICAgPHdpZHRoPjk5
MTwvd2lkdGg+CiAgICA8aGVpZ2h0Pjg2NDwvaGVpZ2h0PgogICA8L3JlY3Q+CiAgPC9wcm9wZXJ0
eT4KICA8cHJvcGVydHkgbmFtZT0iYWNjZXB0RHJvcHMiPgogICA8Ym9vbD50cnVlPC9ib29sPgog
IDwvcHJvcGVydHk+CiAgPHByb3BlcnR5IG5hbWU9IndpbmRvd1RpdGxlIj4KICAgPHN0cmluZz5I
b21lMkJhciBRVDYgRXhTMy4wPC9zdHJpbmc+CiAgPC9wcm9wZXJ0eT4KICA8cHJvcGVydHkgbmFt
ZT0id2luZG93SWNvbiI+CiAgIDxpY29uc2V0PgogICAgPG5vcm1hbG9mZj5pY29uLnBuZzwvbm9y
bWFsb2ZmPmljb24ucG5nPC9pY29uc2V0PgogIDwvcHJvcGVydHk+CiAgPHByb3BlcnR5IG5hbWU9
InRvb2xUaXAiPgogICA8c3RyaW5nPmV4dHJhY3QgdGV4dCBmcm9tIGltYWdlczwvc3RyaW5nPgog
IDwvcHJvcGVydHk+CiAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgIDxzdHJpbmc+ZXh0
cmFjdCB0ZXh0IGZyb20gaW1hZ2VzPC9zdHJpbmc+CiAgPC9wcm9wZXJ0eT4KICA8cHJvcGVydHkg
bmFtZT0id2hhdHNUaGlzIj4KICAgPHN0cmluZz5leHRyYWN0IHRleHQgZnJvbSBpbWFnZXM8L3N0
cmluZz4KICA8L3Byb3BlcnR5PgogIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAg
IDxzdHJpbmc+ZXh0cmFjdCB0ZXh0IGZyb20gaW1hZ2VzPC9zdHJpbmc+CiAgPC9wcm9wZXJ0eT4K
ICA8cHJvcGVydHkgbmFtZT0id2luZG93RmlsZVBhdGgiPgogICA8c3RyaW5nPi48L3N0cmluZz4K
ICA8L3Byb3BlcnR5PgogIDx3aWRnZXQgY2xhc3M9IlFXaWRnZXQiIG5hbWU9ImNlbnRyYWx3aWRn
ZXQiPgogICA8bGF5b3V0IGNsYXNzPSJRR3JpZExheW91dCIgbmFtZT0iZ3JpZExheW91dF8yIj4K
ICAgIDxpdGVtIHJvdz0iMiIgY29sdW1uPSIwIj4KICAgICA8d2lkZ2V0IGNsYXNzPSJRTGFiZWwi
IG5hbWU9ImZpbGVfc2F2ZWRfcGF0aCI+CiAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4K
ICAgICAgIDxzdHJpbmc+aGlnaGxpZ2h0IGFuZCBjb3B5IGdlbmVyYXRlZCBmaWxlcGF0aDwvc3Ry
aW5nPgogICAgICA8L3Byb3BlcnR5PgogICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4K
ICAgICAgIDxzdHJpbmc+aGlnaGxpZ2h0IGFuZCBjb3B5IGdlbmVyYXRlZCBmaWxlcGF0aDwvc3Ry
aW5nPgogICAgICA8L3Byb3BlcnR5PgogICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4K
ICAgICAgIDxzdHJpbmc+aGlnaGxpZ2h0IGFuZCBjb3B5IGdlbmVyYXRlZCBmaWxlcGF0aDwvc3Ry
aW5nPgogICAgICA8L3Byb3BlcnR5PgogICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5h
bWUiPgogICAgICAgPHN0cmluZz5oaWdobGlnaHQgYW5kIGNvcHkgZ2VuZXJhdGVkIGZpbGVwYXRo
PC9zdHJpbmc+CiAgICAgIDwvcHJvcGVydHk+CiAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3Np
YmxlRGVzY3JpcHRpb24iPgogICAgICAgPHN0cmluZz5oaWdobGlnaHQgYW5kIGNvcHkgZ2VuZXJh
dGVkIGZpbGVwYXRoPC9zdHJpbmc+CiAgICAgIDwvcHJvcGVydHk+CiAgICAgIDxwcm9wZXJ0eSBu
YW1lPSJhdXRvRmlsbEJhY2tncm91bmQiPgogICAgICAgPGJvb2w+ZmFsc2U8L2Jvb2w+CiAgICAg
IDwvcHJvcGVydHk+CiAgICAgIDxwcm9wZXJ0eSBuYW1lPSJmcmFtZVNoYXBlIj4KICAgICAgIDxl
bnVtPlFGcmFtZTo6V2luUGFuZWw8L2VudW0+CiAgICAgIDwvcHJvcGVydHk+CiAgICAgIDxwcm9w
ZXJ0eSBuYW1lPSJmcmFtZVNoYWRvdyI+CiAgICAgICA8ZW51bT5RRnJhbWU6OlN1bmtlbjwvZW51
bT4KICAgICAgPC9wcm9wZXJ0eT4KICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAg
PHN0cmluZy8+CiAgICAgIDwvcHJvcGVydHk+CiAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzY2FsZWRD
b250ZW50cyI+CiAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICA8L3Byb3BlcnR5PgogICAg
ICA8cHJvcGVydHkgbmFtZT0id29yZFdyYXAiPgogICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAg
ICAgPC9wcm9wZXJ0eT4KICAgICAgPHByb3BlcnR5IG5hbWU9Im9wZW5FeHRlcm5hbExpbmtzIj4K
ICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgIDwvcHJvcGVydHk+CiAgICAgIDxwcm9wZXJ0
eSBuYW1lPSJ0ZXh0SW50ZXJhY3Rpb25GbGFncyI+CiAgICAgICA8c2V0PlF0OjpMaW5rc0FjY2Vz
c2libGVCeUtleWJvYXJkfFF0OjpMaW5rc0FjY2Vzc2libGVCeU1vdXNlfFF0OjpUZXh0QnJvd3Nl
ckludGVyYWN0aW9ufFF0OjpUZXh0U2VsZWN0YWJsZUJ5S2V5Ym9hcmR8UXQ6OlRleHRTZWxlY3Rh
YmxlQnlNb3VzZTwvc2V0PgogICAgICA8L3Byb3BlcnR5PgogICAgIDwvd2lkZ2V0PgogICAgPC9p
dGVtPgogICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjAiPgogICAgIDxsYXlvdXQgY2xhc3M9IlFH
cmlkTGF5b3V0IiBuYW1lPSJncmlkTGF5b3V0Ii8+CiAgICA8L2l0ZW0+CiAgICA8aXRlbSByb3c9
IjAiIGNvbHVtbj0iMCI+CiAgICAgPHdpZGdldCBjbGFzcz0iUVRhYldpZGdldCIgbmFtZT0idGFi
V2lkZ2V0Ij4KICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgPHN0cmluZz5z
ZXQgc2VydmVyIGNvbm5lY3Rpb24gc2V0dGluZ3RzPC9zdHJpbmc+CiAgICAgIDwvcHJvcGVydHk+
CiAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgPHN0cmluZz5zZXQgc2Vy
dmVyIGNvbm5lY3Rpb24gc2V0dGluZ3RzPC9zdHJpbmc+CiAgICAgIDwvcHJvcGVydHk+CiAgICAg
IDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgPHN0cmluZz5zZXQgc2VydmVyIGNv
bm5lY3Rpb24gc2V0dGluZ3RzPC9zdHJpbmc+CiAgICAgIDwvcHJvcGVydHk+CiAgICAgIDxwcm9w
ZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICA8c3RyaW5nPnNldCBzZXJ2ZXIgY29u
bmVjdGlvbiBzZXR0aW5ndHM8L3N0cmluZz4KICAgICAgPC9wcm9wZXJ0eT4KICAgICAgPHByb3Bl
cnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICA8c3RyaW5nPnNldCBzZXJ2
ZXIgY29ubmVjdGlvbiBzZXR0aW5ndHM8L3N0cmluZz4KICAgICAgPC9wcm9wZXJ0eT4KICAgICAg
PHByb3BlcnR5IG5hbWU9ImN1cnJlbnRJbmRleCI+CiAgICAgICA8bnVtYmVyPjA8L251bWJlcj4K
ICAgICAgPC9wcm9wZXJ0eT4KICAgICAgPHdpZGdldCBjbGFzcz0iUVdpZGdldCIgbmFtZT0idGFi
Ij4KICAgICAgIDxhdHRyaWJ1dGUgbmFtZT0idGl0bGUiPgogICAgICAgIDxzdHJpbmc+R2VuZXJh
dGlvbjwvc3RyaW5nPgogICAgICAgPC9hdHRyaWJ1dGU+CiAgICAgICA8bGF5b3V0IGNsYXNzPSJR
R3JpZExheW91dCIgbmFtZT0iZ3JpZExheW91dF85Ij4KICAgICAgICA8aXRlbSByb3c9IjAiIGNv
bHVtbj0iMCI+CiAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFXaWRnZXQiIG5hbWU9IndpZGdldCIg
bmF0aXZlPSJ0cnVlIj4KICAgICAgICAgIDxsYXlvdXQgY2xhc3M9IlFHcmlkTGF5b3V0IiBuYW1l
PSJncmlkTGF5b3V0XzMiPgogICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIwIj4KICAg
ICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVNjcm9sbEFyZWEiIG5hbWU9InNjcm9sbEFyZWEiPgog
ICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndpZGdldFJlc2l6YWJsZSI+CiAgICAgICAgICAg
ICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAg
ICA8d2lkZ2V0IGNsYXNzPSJRV2lkZ2V0IiBuYW1lPSJzY3JvbGxBcmVhV2lkZ2V0Q29udGVudHMi
PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJnZW9tZXRyeSI+CiAgICAgICAgICAgICAg
IDxyZWN0PgogICAgICAgICAgICAgICAgPHg+MDwveD4KICAgICAgICAgICAgICAgIDx5PjA8L3k+
CiAgICAgICAgICAgICAgICA8d2lkdGg+OTIyPC93aWR0aD4KICAgICAgICAgICAgICAgIDxoZWln
aHQ+NzUwPC9oZWlnaHQ+CiAgICAgICAgICAgICAgIDwvcmVjdD4KICAgICAgICAgICAgICA8L3By
b3BlcnR5PgogICAgICAgICAgICAgIDxsYXlvdXQgY2xhc3M9IlFHcmlkTGF5b3V0IiBuYW1lPSJn
cmlkTGF5b3V0XzgiPgogICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMCI+CiAg
ICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRRnJhbWUiIG5hbWU9ImZyYW1lIj4KICAgICAg
ICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZnJhbWVTaGFwZSI+CiAgICAgICAgICAgICAgICAg
IDxlbnVtPlFGcmFtZTo6U3R5bGVkUGFuZWw8L2VudW0+CiAgICAgICAgICAgICAgICAgPC9wcm9w
ZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZnJhbWVTaGFkb3ciPgogICAg
ICAgICAgICAgICAgICA8ZW51bT5RRnJhbWU6OlJhaXNlZDwvZW51bT4KICAgICAgICAgICAgICAg
ICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxsYXlvdXQgY2xhc3M9IlFHcmlkTGF5b3V0
IiBuYW1lPSJncmlkTGF5b3V0XzUiPgogICAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjYiIGNv
bHVtbj0iMCIgY29sc3Bhbj0iMiI+CiAgICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJR
R3JvdXBCb3giIG5hbWU9Imdyb3VwQm94XzMiPgogICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0
eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5NYW51YWwgRW50
cnk8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAg
ICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgICA8
c3RyaW5nPk1hbnVhbCBFbnRyeTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgIDwvcHJvcGVy
dHk+CiAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAg
ICAgICAgICAgICAgICAgIDxzdHJpbmc+TWFudWFsIEVudHJ5PC9zdHJpbmc+CiAgICAgICAgICAg
ICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0i
YWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPk1hbnVhbCBFbnRy
eTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAg
ICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAg
ICAgICAgICAgIDxzdHJpbmc+TWFudWFsIEVudHJ5PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAg
ICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGl0bGUi
PgogICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPk1hbnVhbCBFbnRyeTwvc3RyaW5nPgogICAg
ICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgPGxheW91dCBj
bGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRMYXlvdXRfNiI+CiAgICAgICAgICAgICAgICAg
ICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIyIj4KICAgICAgICAgICAgICAgICAgICAgIDx3aWRn
ZXQgY2xhc3M9IlFMaW5lRWRpdCIgbmFtZT0iaXRlbV9uYW1lIj4KICAgICAgICAgICAgICAgICAg
ICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxz
dHJpbmc+aXRlbSBuYW1lPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0
eT4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAg
ICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5pdGVtIG5hbWU8L3N0cmluZz4KICAgICAgICAg
ICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0
eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPml0ZW0g
bmFtZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAg
ICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAg
ICAgICAgICAgICAgICAgPHN0cmluZz5pdGVtIG5hbWU8L3N0cmluZz4KICAgICAgICAgICAgICAg
ICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1l
PSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5n
Pml0ZW0gbmFtZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAg
ICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImRyYWdFbmFibGVkIj4KICAgICAg
ICAgICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICAgICAgICAg
ICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFj
ZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPml0ZW0gbmFtZTwv
c3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAg
ICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImNsZWFyQnV0dG9uRW5hYmxlZCI+CiAgICAgICAgICAg
ICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgICAgICAgPC9w
cm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAg
ICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIx
Ij4KICAgICAgICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFMaW5lRWRpdCIgbmFtZT0i
Y29kZTIiPgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4K
ICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5hZGRpdGlvbmFsIGNvZGUgdG8gYWRkIHRv
IHNoZWV0IGZvciByZWZlcmVuY2U8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3By
b3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAi
PgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmFkZGl0aW9uYWwgY29kZSB0byBhZGQg
dG8gc2hlZXQgZm9yIHJlZmVyZW5jZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwv
cHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhp
cyI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YWRkaXRpb25hbCBjb2RlIHRvIGFk
ZCB0byBzaGVldCBmb3IgcmVmZXJlbmNlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAg
PC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNz
aWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmFkZGl0aW9uYWwgY29k
ZSB0byBhZGQgdG8gc2hlZXQgZm9yIHJlZmVyZW5jZTwvc3RyaW5nPgogICAgICAgICAgICAgICAg
ICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9
ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+
YWRkaXRpb25hbCBjb2RlIHRvIGFkZCB0byBzaGVldCBmb3IgcmVmZXJlbmNlPC9zdHJpbmc+CiAg
ICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8
cHJvcGVydHkgbmFtZT0ibGF5b3V0RGlyZWN0aW9uIj4KICAgICAgICAgICAgICAgICAgICAgICAg
PGVudW0+UXQ6OkxlZnRUb1JpZ2h0PC9lbnVtPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJv
cGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImRyYWdFbmFibGVk
Ij4KICAgICAgICAgICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAg
ICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBu
YW1lPSJwbGFjZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkFk
ZGl0aW9uYWwgQ29kZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+
CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImNsZWFyQnV0dG9uRW5hYmxl
ZCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAg
ICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgIDwvd2lkZ2V0Pgog
ICAgICAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAgICAgIDxpdGVtIHJv
dz0iMCIgY29sdW1uPSIzIj4KICAgICAgICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQ
dXNoQnV0dG9uIiBuYW1lPSJzdWJtaXQiPgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0
eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5nZW5lcmF0
ZSBjb2RlZCBmaWxlIGZyb20gZGF0YTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwv
cHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1Rp
cCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+Z2VuZXJhdGUgY29kZWQgZmlsZSBm
cm9tIGRhdGE8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAg
ICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAg
ICAgICAgICAgICAgICA8c3RyaW5nPmdlbmVyYXRlIGNvZGVkIGZpbGUgZnJvbSBkYXRhPC9zdHJp
bmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAg
ICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAg
ICAgICA8c3RyaW5nPmdlbmVyYXRlIGNvZGVkIGZpbGUgZnJvbSBkYXRhPC9zdHJpbmc+CiAgICAg
ICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8cHJv
cGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgICAg
ICAgPHN0cmluZz5nZW5lcmF0ZSBjb2RlZCBmaWxlIGZyb20gZGF0YTwvc3RyaW5nPgogICAgICAg
ICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3Bl
cnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPiZhbXA7U3Vi
bWl0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAg
ICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZmxhdCI+CiAgICAgICAgICAgICAgICAgICAg
ICAgIDxib29sPmZhbHNlPC9ib29sPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+
CiAgICAgICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgICAgICAgPC9p
dGVtPgogICAgICAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMCI+CiAgICAg
ICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRTGluZUVkaXQiIG5hbWU9ImNvZGUiPgog
ICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAg
ICAgICAgICAgICAgICAgPHN0cmluZz5jb2RlIHRvIGVuY29kZWQgdG8gYSBiYXJjb2RlPC9zdHJp
bmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAg
ICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgICAgICAg
PHN0cmluZz5jb2RlIHRvIGVuY29kZWQgdG8gYSBiYXJjb2RlPC9zdHJpbmc+CiAgICAgICAgICAg
ICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkg
bmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5jb2RlIHRv
IGVuY29kZWQgdG8gYSBiYXJjb2RlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9w
cm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJs
ZU5hbWUiPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmNvZGUgdG8gZW5jb2RlZCB0
byBhIGJhcmNvZGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5Pgog
ICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRp
b24iPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmNvZGUgdG8gZW5jb2RlZCB0byBh
IGJhcmNvZGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAg
ICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJkcmFnRW5hYmxlZCI+CiAgICAgICAg
ICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgICAgICAg
PC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0icGxhY2Vo
b2xkZXJUZXh0Ij4KICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5VUEMvU0tVL0hvbWUg
Q29kZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAg
ICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImNsZWFyQnV0dG9uRW5hYmxlZCI+CiAgICAg
ICAgICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgICAg
ICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAg
ICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMSIgY29s
dW1uPSIzIj4KICAgICAgICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDaGVja0JveCIg
bmFtZT0ic2F2ZU9uU2VydmVyIj4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFt
ZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c2F2ZSBkYXRhIG9u
IHNlcnZlcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAg
ICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAg
ICAgICAgICAgICAgIDxzdHJpbmc+c2F2ZSBkYXRhIG9uIHNlcnZlcjwvc3RyaW5nPgogICAgICAg
ICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3Bl
cnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c2F2
ZSBkYXRhIG9uIHNlcnZlcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVy
dHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1l
Ij4KICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5zYXZlIGRhdGEgb24gc2VydmVyPC9z
dHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAg
ICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAg
ICAgICAgICAgICAgICAgPHN0cmluZz5zYXZlIGRhdGEgb24gc2VydmVyPC9zdHJpbmc+CiAgICAg
ICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8cHJv
cGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+U2F2ZSBP
biBTZXJ2ZXI8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAg
ICAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICAgICAgIDwvaXRlbT4K
ICAgICAgICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjAiPgogICAgICAgICAg
ICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNoZWNrQm94IiBuYW1lPSJub0NvZGUxIj4KICAg
ICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAg
ICAgICAgICAgICAgIDxzdHJpbmc+Tm8gQ29kZSAxPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAg
ICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0i
c3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5ObyBDb2RlIDE8L3N0
cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAg
ICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgICAg
ICA8c3RyaW5nPk5vIENvZGUgMTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJv
cGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVO
YW1lIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5ObyBDb2RlIDE8L3N0cmluZz4K
ICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAg
IDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAg
ICAgICAgICA8c3RyaW5nPk5vIENvZGUgMTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAg
IDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQi
PgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPk5vIENvZGUgMTwvc3RyaW5nPgogICAg
ICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICA8L3dp
ZGdldD4KICAgICAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgICAgICA8
aXRlbSByb3c9IjEiIGNvbHVtbj0iMSI+CiAgICAgICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNs
YXNzPSJRQ2hlY2tCb3giIG5hbWU9Im5vQ29kZTIiPgogICAgICAgICAgICAgICAgICAgICAgIDxw
cm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5O
byBDb2RlIDI8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAg
ICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAg
ICAgICAgICAgICAgICA8c3RyaW5nPk5vIENvZGUgMjwvc3RyaW5nPgogICAgICAgICAgICAgICAg
ICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9
IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+Tm8gQ29kZSAyPC9z
dHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAg
ICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAg
ICAgICAgICA8c3RyaW5nPk5vIENvZGUgMjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAg
IDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vz
c2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+Tm8gQ29k
ZSAyPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAg
ICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgICAg
ICAgIDxzdHJpbmc+Tm8gQ29kZSAyPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9w
cm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAg
ICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSIy
Ij4KICAgICAgICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDaGVja0JveCIgbmFtZT0i
bm9Db2RlMyI+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAi
PgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPk5vIENvZGUgMzwvc3RyaW5nPgogICAg
ICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHBy
b3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+
Tm8gQ29kZSAzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAg
ICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAg
ICAgICAgICAgICAgICAgPHN0cmluZz5ObyBDb2RlIDM8L3N0cmluZz4KICAgICAgICAgICAgICAg
ICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1l
PSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+Tm8gQ29k
ZSAzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAg
ICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAg
ICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5ObyBDb2RlIDM8L3N0cmluZz4KICAgICAgICAg
ICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0
eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5ObyBDb2RlIDM8
L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAg
ICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAg
ICAgICAgICAgICA8L2xheW91dD4KICAgICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAg
ICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iNyIgY29sdW1u
PSIwIiBjb2xzcGFuPSIyIj4KICAgICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFHcm91
cEJveCIgbmFtZT0iZ3JvdXBCb3hfMiI+CiAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5h
bWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkltcG9ydCBFeHBvcnQ8
L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAg
ICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgICA8c3Ry
aW5nPkltcG9ydCBFeHBvcnQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5
PgogICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAg
ICAgICAgICAgICAgICA8c3RyaW5nPkltcG9ydCBFeHBvcnQ8L3N0cmluZz4KICAgICAgICAgICAg
ICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJh
Y2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+SW1wb3J0IEV4cG9y
dDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAg
ICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAg
ICAgICAgICAgIDxzdHJpbmc+SW1wb3J0IEV4cG9ydDwvc3RyaW5nPgogICAgICAgICAgICAgICAg
ICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRpdGxl
Ij4KICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5JbXBvcnQgRXhwb3J0PC9zdHJpbmc+CiAg
ICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICA8bGF5b3V0
IGNsYXNzPSJRR3JpZExheW91dCIgbmFtZT0iZ3JpZExheW91dF80Ij4KICAgICAgICAgICAgICAg
ICAgICAgPGl0ZW0gcm93PSI0IiBjb2x1bW49IjEiPgogICAgICAgICAgICAgICAgICAgICAgPHdp
ZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9ImJyb3dzZV9leHBvcnQiPgogICAgICAgICAg
ICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAg
ICAgICAgPHN0cmluZz5icm93c2UgZXhwb3J0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAg
ICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3Rh
dHVzVGlwIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgZXhwb3J0PC9z
dHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAg
ICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgICAg
ICAgPHN0cmluZz5icm93c2UgZXhwb3J0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAg
PC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNz
aWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBleHBvcnQ8
L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAg
ICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAg
ICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBleHBvcnQ8L3N0cmluZz4KICAgICAgICAg
ICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0
eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5Ccm93c2U8L3N0
cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAg
ICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAg
ICAgICAgICAgPGl0ZW0gcm93PSIyIiBjb2x1bW49IjEiPgogICAgICAgICAgICAgICAgICAgICAg
PHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9ImJyb3dzZV9pbXBvcnRfY29kZXNfZmls
ZSI+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAg
ICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkJyb3dzZSBmb3IgT3JkZXIgY29kZXMgaW1wb3J0
IEZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAg
ICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAg
ICAgICAgICAgICA8c3RyaW5nPkJyb3dzZSBmb3IgT3JkZXIgY29kZXMgaW1wb3J0IEZpbGU8L3N0
cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAg
ICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgICAg
ICA8c3RyaW5nPkJyb3dzZSBmb3IgT3JkZXIgY29kZXMgaW1wb3J0IEZpbGU8L3N0cmluZz4KICAg
ICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxw
cm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxz
dHJpbmc+QnJvd3NlIGZvciBPcmRlciBjb2RlcyBpbXBvcnQgRmlsZTwvc3RyaW5nPgogICAgICAg
ICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3Bl
cnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICAgICAg
IDxzdHJpbmc+QnJvd3NlIGZvciBPcmRlciBjb2RlcyBpbXBvcnQgRmlsZTwvc3RyaW5nPgogICAg
ICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHBy
b3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkJyb3dz
ZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAg
ICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAg
ICAgICAgICAgICAgICA8aXRlbSByb3c9IjQiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICAg
ICAgICA8d2lkZ2V0IGNsYXNzPSJRTGluZUVkaXQiIG5hbWU9ImV4cG9ydF9maWxlIj4KICAgICAg
ICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAg
ICAgICAgICAgIDxzdHJpbmc+ZXhwb3J0IGZpbGUgbmFtZTwvc3RyaW5nPgogICAgICAgICAgICAg
ICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5h
bWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZXhwb3J0IGZp
bGUgbmFtZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAg
ICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAg
ICAgICAgICAgICAgIDxzdHJpbmc+ZXhwb3J0IGZpbGUgbmFtZTwvc3RyaW5nPgogICAgICAgICAg
ICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5
IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5l
eHBvcnQgZmlsZSBuYW1lPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0
eT4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2Ny
aXB0aW9uIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5leHBvcnQgZmlsZSBuYW1l
PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAg
ICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgICAgICAg
IDxzdHJpbmc+Y29kZXNfZXhwb3J0LmNzdjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAg
IDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImRyYWdF
bmFibGVkIj4KICAgICAgICAgICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAg
ICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9w
ZXJ0eSBuYW1lPSJwbGFjZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICAgICAgICAgICA8c3Ry
aW5nPmV4cG9ydCBmaWxlIG5hbWU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3By
b3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICAg
ICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIyIiBjb2x1bW49IjAi
PgogICAgICAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUxpbmVFZGl0IiBuYW1lPSJp
bXBvcnRfZmlsZSI+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xU
aXAiPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkltcG9ydCBDb2RlcyBGaWxlIE5h
bWU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAg
ICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAg
ICAgICAgICA8c3RyaW5nPkltcG9ydCBDb2RlcyBGaWxlIE5hbWU8L3N0cmluZz4KICAgICAgICAg
ICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0
eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkltcG9y
dCBDb2RlcyBGaWxlIE5hbWU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3Bl
cnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFt
ZSI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+SW1wb3J0IENvZGVzIEZpbGUgTmFt
ZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAg
ICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAg
ICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+SW1wb3J0IENvZGVzIEZpbGUgTmFtZTwvc3RyaW5n
PgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAg
ICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5n
PmNvZGVzLnR4dDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAg
ICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImRyYWdFbmFibGVkIj4KICAgICAg
ICAgICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICAgICAgICAg
ICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFj
ZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmltcG9ydCBjb2Rl
cyB0ZXh0IGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5Pgog
ICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJjbGVhckJ1dHRvbkVuYWJsZWQi
PgogICAgICAgICAgICAgICAgICAgICAgICA8Ym9vbD5mYWxzZTwvYm9vbD4KICAgICAgICAgICAg
ICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAg
ICAgICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgICAgICAgPGl0ZW0gcm93
PSIyIiBjb2x1bW49IjIiPgogICAgICAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1
c2hCdXR0b24iIG5hbWU9ImltcG9ydF9mIj4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVy
dHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+UnVuIGlt
cG9ydCBmcm9tIGltcG9ydCBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9w
cm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlw
Ij4KICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5SdW4gaW1wb3J0IGZyb20gaW1wb3J0
IGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAg
ICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAg
ICAgICAgICAgICA8c3RyaW5nPlJ1biBpbXBvcnQgZnJvbSBpbXBvcnQgZmlsZTwvc3RyaW5nPgog
ICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAg
PHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgICAgICAg
PHN0cmluZz5SdW4gaW1wb3J0IGZyb20gaW1wb3J0IGZpbGU8L3N0cmluZz4KICAgICAgICAgICAg
ICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBu
YW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgICAgICAgICA8c3Ry
aW5nPlJ1biBpbXBvcnQgZnJvbSBpbXBvcnQgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAg
ICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9
InRleHQiPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkltcG9ydDwvc3RyaW5nPgog
ICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICA8
L3dpZGdldD4KICAgICAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgICAg
ICA8aXRlbSByb3c9IjEiIGNvbHVtbj0iMCIgY29sc3Bhbj0iNCI+CiAgICAgICAgICAgICAgICAg
ICAgICA8d2lkZ2V0IGNsYXNzPSJRR3JvdXBCb3giIG5hbWU9Imdyb3VwQm94XzUiPgogICAgICAg
ICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0aXRsZSI+CiAgICAgICAgICAgICAgICAg
ICAgICAgIDxzdHJpbmc+Q29sdW1uczwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwv
cHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlv
dXQiIG5hbWU9ImdyaWRMYXlvdXRfMjEiPgogICAgICAgICAgICAgICAgICAgICAgICA8aXRlbSBy
b3c9IjAiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNz
PSJRU3BpbkJveCIgbmFtZT0iaXRlbV9uYW1lX2NvbCI+CiAgICAgICAgICAgICAgICAgICAgICAg
ICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICAgICAgICAgICA8
c3RyaW5nPml0ZW0gbmFtZSBjb2x1bW4gaW4gaW1wb3J0IGZpbGU8L3N0cmluZz4KICAgICAgICAg
ICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgICAgIDxw
cm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgICAgICAgICA8c3Ry
aW5nPml0ZW0gbmFtZSBjb2x1bW4gaW4gaW1wb3J0IGZpbGU8L3N0cmluZz4KICAgICAgICAgICAg
ICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgICAgIDxwcm9w
ZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5n
Pml0ZW0gbmFtZSBjb2x1bW4gaW4gaW1wb3J0IGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAg
ICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0
eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJp
bmc+aXRlbSBuYW1lIGNvbHVtbiBpbiBpbXBvcnQgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAg
ICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgICAgPHByb3Bl
cnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICAgICAg
ICAgIDxzdHJpbmc+aXRlbSBuYW1lIGNvbHVtbiBpbiBpbXBvcnQgZmlsZTwvc3RyaW5nPgogICAg
ICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAg
ICAgPHByb3BlcnR5IG5hbWU9InNpbmdsZVN0ZXAiPgogICAgICAgICAgICAgICAgICAgICAgICAg
ICA8bnVtYmVyPjE8L251bWJlcj4KICAgICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5
PgogICAgICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ2YWx1ZSI+CiAgICAg
ICAgICAgICAgICAgICAgICAgICAgIDxudW1iZXI+MDwvbnVtYmVyPgogICAgICAgICAgICAgICAg
ICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgICA8L3dpZGdldD4K
ICAgICAgICAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgICAgICAgICA8
aXRlbSByb3c9IjAiIGNvbHVtbj0iMSI+CiAgICAgICAgICAgICAgICAgICAgICAgICA8d2lkZ2V0
IGNsYXNzPSJRU3BpbkJveCIgbmFtZT0idXBjX2NvbCI+CiAgICAgICAgICAgICAgICAgICAgICAg
ICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICAgICAgICAgICA8
c3RyaW5nPnVwYyBjb2x1bW4gaW4gaW1wb3J0IGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAg
ICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0
eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnVw
YyBjb2x1bW4gaW4gaW1wb3J0IGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICAg
ICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3
aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnVwYyBjb2x1bW4g
aW4gaW1wb3J0IGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3Bl
cnR5PgogICAgICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxl
TmFtZSI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+dXBjIGNvbHVtbiBpbiBp
bXBvcnQgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+
CiAgICAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNj
cmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+dXBjIGNvbHVtbiBp
biBpbXBvcnQgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVy
dHk+CiAgICAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InZhbHVlIj4KICAg
ICAgICAgICAgICAgICAgICAgICAgICAgPG51bWJlcj4xPC9udW1iZXI+CiAgICAgICAgICAgICAg
ICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICAgIDwvd2lkZ2V0
PgogICAgICAgICAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAgICAgICAg
IDxpdGVtIHJvdz0iMCIgY29sdW1uPSIyIj4KICAgICAgICAgICAgICAgICAgICAgICAgIDx3aWRn
ZXQgY2xhc3M9IlFTcGluQm94IiBuYW1lPSJjb2RlczJfY29sIj4KICAgICAgICAgICAgICAgICAg
ICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICAgICAg
ICAgIDxzdHJpbmc+Y29kZTIgY29sdW1uIG51bWJlciBmb3IgaW1wb3J0IGZpbGU8L3N0cmluZz4K
ICAgICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAg
ICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgICAg
ICAgICA8c3RyaW5nPmNvZGUyIGNvbHVtbiBudW1iZXIgZm9yIGltcG9ydCBmaWxlPC9zdHJpbmc+
CiAgICAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAg
ICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgICAg
ICAgICAgPHN0cmluZz5jb2RlMiBjb2x1bW4gbnVtYmVyIGZvciBpbXBvcnQgZmlsZTwvc3RyaW5n
PgogICAgICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAg
ICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAg
ICAgICAgICAgICAgPHN0cmluZz5jb2RlMiBjb2x1bW4gbnVtYmVyIGZvciBpbXBvcnQgZmlsZTwv
c3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAg
ICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAg
ICAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+Y29kZTIgY29sdW1uIG51bWJlciBmb3Ig
aW1wb3J0IGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5
PgogICAgICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ2YWx1ZSI+CiAgICAg
ICAgICAgICAgICAgICAgICAgICAgIDxudW1iZXI+MjwvbnVtYmVyPgogICAgICAgICAgICAgICAg
ICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgICA8L3dpZGdldD4K
ICAgICAgICAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgICAgICAgIDwv
bGF5b3V0PgogICAgICAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICAg
ICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgICAgICAgPGl0ZW0gcm93PSI0IiBjb2x1bW49IjIi
PgogICAgICAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9
ImV4cG9ydF8yIj4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRp
cCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RXhwb3J0IGNvZGVzIHRvIGNzdjwv
c3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAg
ICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgICAg
ICAgIDxzdHJpbmc+RXhwb3J0IGNvZGVzIHRvIGNzdjwvc3RyaW5nPgogICAgICAgICAgICAgICAg
ICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9
IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RXhwb3J0IGNvZGVz
IHRvIGNzdjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAg
ICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAg
ICAgICAgICAgICAgICAgICAgPHN0cmluZz5FeHBvcnQgY29kZXMgdG8gY3N2PC9zdHJpbmc+CiAg
ICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8
cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAg
ICAgICAgPHN0cmluZz5FeHBvcnQgY29kZXMgdG8gY3N2PC9zdHJpbmc+CiAgICAgICAgICAgICAg
ICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFt
ZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RXhwb3J0PC9zdHJpbmc+
CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAg
IDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAg
ICAgIDxpdGVtIHJvdz0iMyIgY29sdW1uPSIwIiBjb2xzcGFuPSIyIj4KICAgICAgICAgICAgICAg
ICAgICAgIDx3aWRnZXQgY2xhc3M9IlFHcm91cEJveCIgbmFtZT0iZ3JvdXBCb3hfNiI+CiAgICAg
ICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRpdGxlIj4KICAgICAgICAgICAgICAg
ICAgICAgICAgPHN0cmluZz5Tb3J0aW5nPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAg
PC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8bGF5b3V0IGNsYXNzPSJRR3JpZExh
eW91dCIgbmFtZT0iZ3JpZExheW91dF8yMiI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxpdGVt
IHJvdz0iMCIgY29sdW1uPSIyIj4KICAgICAgICAgICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xh
c3M9IlFDaGVja0JveCIgbmFtZT0ic29ydGVySEIxIj4KICAgICAgICAgICAgICAgICAgICAgICAg
ICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgIDxz
dHJpbmc+c29ydCByb3dzIGJ5IGF0dGVtcHRpbmcgdG8gZmluZCBhdCBsZWFzdCBvbmUgc2Nhbm5h
YmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAg
ICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAg
ICAgICAgICAgICAgICAgICAgPHN0cmluZz5zb3J0IHJvd3MgYnkgYXR0ZW1wdGluZyB0byBmaW5k
IGF0IGxlYXN0IG9uZSBzY2FubmFibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICAg
ICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3
aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnNvcnQgcm93cyBi
eSBhdHRlbXB0aW5nIHRvIGZpbmQgYXQgbGVhc3Qgb25lIHNjYW5uYWJsZTwvc3RyaW5nPgogICAg
ICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAg
ICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgICAg
ICAgICAgPHN0cmluZz5zb3J0IHJvd3MgYnkgYXR0ZW1wdGluZyB0byBmaW5kIGF0IGxlYXN0IG9u
ZSBzY2FubmFibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5
PgogICAgICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVz
Y3JpcHRpb24iPgogICAgICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnNvcnQgcm93cyBi
eSBhdHRlbXB0aW5nIHRvIGZpbmQgYXQgbGVhc3Qgb25lIHNjYW5uYWJsZTwvc3RyaW5nPgogICAg
ICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAg
ICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgICAgICAgICA8c3Ry
aW5nPkZpbmQKT25lClNjYW5uYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgICAg
IDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRy
aXN0YXRlIj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgPGJvb2w+ZmFsc2U8L2Jvb2w+CiAg
ICAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAg
ICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAg
ICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIwIj4KICAgICAgICAgICAgICAgICAg
ICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDaGVja0JveCIgbmFtZT0ic29ydGVySEIyIj4KICAgICAg
ICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAg
ICAgICAgICAgICAgIDxzdHJpbmc+Q29sdW1uMTpVUEMoSU5UKCZndDs4KSkKQ29sdW1uMjpIT01F
X0NPREUoSU5UKDgpKQpDb2x1bW4zOkxFVFRFUlMoNTEyKTwvc3RyaW5nPgogICAgICAgICAgICAg
ICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgICAgPHByb3Bl
cnR5IG5hbWU9ImNoZWNrZWQiPgogICAgICAgICAgICAgICAgICAgICAgICAgICA8Ym9vbD50cnVl
PC9ib29sPgogICAgICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAg
ICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgICAgICAgICAgPC9pdGVtPgog
ICAgICAgICAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMSI+CiAgICAgICAg
ICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ2hlY2tCb3giIG5hbWU9InNvcnRlckhC
MyI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAg
ICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkNvbHVtbjE6SE9NRUNPREUoSU5UKDgpCkNv
bHVtbjI6VVBDKElOVCgmZ3Q7OCkpCkNvbHVtbjM6TEVUVEVSUyg1MTIpPC9zdHJpbmc+CiAgICAg
ICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICAg
IDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAg
ICAgICAgICAgPC9sYXlvdXQ+CiAgICAgICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAg
ICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjMi
IGNvbHVtbj0iMiI+CiAgICAgICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRR3JvdXBC
b3giIG5hbWU9Imdyb3VwQm94XzciPgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBu
YW1lPSJ0aXRsZSI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+U2VydmVyPC9zdHJp
bmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAg
ICAgICA8bGF5b3V0IGNsYXNzPSJRR3JpZExheW91dCIgbmFtZT0iZ3JpZExheW91dF8yMyI+CiAg
ICAgICAgICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIwIj4KICAgICAgICAg
ICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDaGVja0JveCIgbmFtZT0ic2F2ZU9uU2Vy
dmVyX2ltcG9ydCI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRl
eHQiPgogICAgICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPlNhdmU8L3N0cmluZz4KICAg
ICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAg
ICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAg
ICAgICAgICAgICA8L2xheW91dD4KICAgICAgICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAg
ICAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAgICAgPC9sYXlvdXQ+CiAg
ICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAg
ICAgICAgICAgICAgICA8aXRlbSByb3c9IjIiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICAg
ICA8d2lkZ2V0IGNsYXNzPSJRR3JvdXBCb3giIG5hbWU9Imdyb3VwQm94Ij4KICAgICAgICAgICAg
ICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICAgIDxz
dHJpbmc+U2F2ZSBMb2NhdGlvbiwgT3V0cHV0IEZpbGUgbmFtZSwgU2hlZXQgVGl0bGU8L3N0cmlu
Zz4KICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgIDxw
cm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPlNh
dmUgTG9jYXRpb24sIE91dHB1dCBGaWxlIG5hbWUsIFNoZWV0IFRpdGxlPC9zdHJpbmc+CiAgICAg
ICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkg
bmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5TYXZlIExvY2F0
aW9uLCBPdXRwdXQgRmlsZSBuYW1lLCBTaGVldCBUaXRsZTwvc3RyaW5nPgogICAgICAgICAgICAg
ICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFj
Y2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5TYXZlIExvY2F0aW9u
LCBPdXRwdXQgRmlsZSBuYW1lLCBTaGVldCBUaXRsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAg
ICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vz
c2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+U2F2ZSBMb2Nh
dGlvbiwgT3V0cHV0IEZpbGUgbmFtZSwgU2hlZXQgVGl0bGU8L3N0cmluZz4KICAgICAgICAgICAg
ICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0
aXRsZSI+CiAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+U2F2ZSBMb2NhdGlvbiwgT3VwdXQs
IFRpdGxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAg
ICAgICAgICAgICA8bGF5b3V0IGNsYXNzPSJRR3JpZExheW91dCIgbmFtZT0iZ3JpZExheW91dF83
Ij4KICAgICAgICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIyIiBjb2x1bW49IjAiPgogICAgICAg
ICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUxpbmVFZGl0IiBuYW1lPSJvcmRlcl9zaGVl
dF90aXRsZSI+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAi
PgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPk9yZGVyIFNoZWV0IHRpdGxlPC9zdHJp
bmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAg
ICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgICAgICAg
PHN0cmluZz5PcmRlciBTaGVldCB0aXRsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAg
IDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRz
VGhpcyI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+T3JkZXIgU2hlZXQgdGl0bGU8
L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAg
ICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAg
ICAgICAgICAgIDxzdHJpbmc+T3JkZXIgU2hlZXQgdGl0bGU8L3N0cmluZz4KICAgICAgICAgICAg
ICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBu
YW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgICAgICAgICA8c3Ry
aW5nPk9yZGVyIFNoZWV0IHRpdGxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9w
cm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAg
ICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+T3JkZXIgU2hlZXQ8L3N0cmluZz4KICAgICAg
ICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9w
ZXJ0eSBuYW1lPSJkcmFnRW5hYmxlZCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxib29sPnRy
dWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAg
ICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0icGxhY2Vob2xkZXJUZXh0Ij4KICAgICAgICAgICAg
ICAgICAgICAgICAgPHN0cmluZz5PcmRlciBTaGVldCBUaXRsZTwvc3RyaW5nPgogICAgICAgICAg
ICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5
IG5hbWU9ImNsZWFyQnV0dG9uRW5hYmxlZCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxib29s
PnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAg
ICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAg
ICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIwIj4KICAgICAgICAgICAgICAg
ICAgICAgIDx3aWRnZXQgY2xhc3M9IlFMaW5lRWRpdCIgbmFtZT0ic2F2ZV9sb2NhdGlvbiI+CiAg
ICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAg
ICAgICAgICAgICAgICA8c3RyaW5nPnNhdmUgbG9jYXRpb248L3N0cmluZz4KICAgICAgICAgICAg
ICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBu
YW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnNhdmUgbG9j
YXRpb248L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAg
ICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAg
ICAgICAgICAgICA8c3RyaW5nPnNhdmUgbG9jYXRpb248L3N0cmluZz4KICAgICAgICAgICAgICAg
ICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1l
PSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c2F2ZSBs
b2NhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAg
ICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+
CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c2F2ZSBsb2NhdGlvbjwvc3RyaW5nPgog
ICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAg
PHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmNv
ZGVzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAg
ICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZHJhZ0VuYWJsZWQiPgogICAgICAgICAgICAg
ICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJv
cGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InBsYWNlaG9sZGVy
VGV4dCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+U2F2ZSBMb2NhdGlvbjwvc3Ry
aW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAg
ICAgICAgPHByb3BlcnR5IG5hbWU9ImNsZWFyQnV0dG9uRW5hYmxlZCI+CiAgICAgICAgICAgICAg
ICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9w
ZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgICAg
ICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSIwIj4K
ICAgICAgICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFMaW5lRWRpdCIgbmFtZT0ib3Jk
ZXJzaGVldF9uYW1lIj4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9v
bFRpcCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZmlsZSB0byBnZW5lcmF0ZSBm
b3Igb3JkZXIgc2hlZXQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5
PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAg
ICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmZpbGUgdG8gZ2VuZXJhdGUgZm9yIG9yZGVyIHNo
ZWV0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAg
ICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAg
ICAgICAgICAgPHN0cmluZz5maWxlIHRvIGdlbmVyYXRlIGZvciBvcmRlciBzaGVldDwvc3RyaW5n
PgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAg
ICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgICAg
ICAgPHN0cmluZz5maWxlIHRvIGdlbmVyYXRlIGZvciBvcmRlciBzaGVldDwvc3RyaW5nPgogICAg
ICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHBy
b3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICAg
ICAgIDxzdHJpbmc+ZmlsZSB0byBnZW5lcmF0ZSBmb3Igb3JkZXIgc2hlZXQ8L3N0cmluZz4KICAg
ICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxw
cm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5vcmRl
cl9zaGVldC5odG1sPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4K
ICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZHJhZ0VuYWJsZWQiPgogICAg
ICAgICAgICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgICAgICAg
ICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InBs
YWNlaG9sZGVyVGV4dCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+T3JkZXIgU2hl
ZXQgTmFtZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAg
ICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImNsZWFyQnV0dG9uRW5hYmxlZCI+CiAg
ICAgICAgICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAg
ICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAg
ICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iNiIg
Y29sdW1uPSIwIj4KICAgICAgICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0
dG9uIiBuYW1lPSJjbGVhcl9zYXZlX2xvY2F0aW9uIj4KICAgICAgICAgICAgICAgICAgICAgICA8
cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+
ZGVsZXRlIGFsbCBmaWxlcyBpbiBzYXZlIGxvY2F0aW9uPC9zdHJpbmc+CiAgICAgICAgICAgICAg
ICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFt
ZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5kZWxldGUgYWxs
IGZpbGVzIGluIHNhdmUgbG9jYXRpb248L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8
L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1Ro
aXMiPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmRlbGV0ZSBhbGwgZmlsZXMgaW4g
c2F2ZSBsb2NhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+
CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4K
ICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5kZWxldGUgYWxsIGZpbGVzIGluIHNhdmUg
bG9jYXRpb248L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAg
ICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24i
PgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmRlbGV0ZSBhbGwgZmlsZXMgaW4gc2F2
ZSBsb2NhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAg
ICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAg
ICAgICAgICAgICA8c3RyaW5nPkNsZWFyIFNhdmUgTG9jYXRpb248L3N0cmluZz4KICAgICAgICAg
ICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgPC93aWRnZXQ+
CiAgICAgICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgICAgICAgPGl0ZW0g
cm93PSI0IiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0i
UVB1c2hCdXR0b24iIG5hbWU9ImJyb3dzZV9zYXZlX2xvY2F0aW9uIj4KICAgICAgICAgICAgICAg
ICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICAgICAg
IDxzdHJpbmc+YnJvd3NlIGZvciBhIHNhdmUgbG9jYXRpb248L3N0cmluZz4KICAgICAgICAgICAg
ICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBu
YW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBm
b3IgYSBzYXZlIGxvY2F0aW9uPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgPC9wcm9w
ZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4K
ICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgZm9yIGEgc2F2ZSBsb2NhdGlv
bjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAg
ICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAg
ICAgICAgICAgICAgPHN0cmluZz5icm93c2UgZm9yIGEgc2F2ZSBsb2NhdGlvbjwvc3RyaW5nPgog
ICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAg
PHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAg
ICAgICAgIDxzdHJpbmc+YnJvd3NlIGZvciBhIHNhdmUgbG9jYXRpb248L3N0cmluZz4KICAgICAg
ICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDxwcm9w
ZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5Ccm93c2U8
L3N0cmluZz4KICAgICAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAg
ICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAg
ICAgICAgICAgICAgPGl0ZW0gcm93PSIzIiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgICAg
ICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJ0aXRsZV9wcmVzZXRzIj4KICAgICAg
ICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAg
ICAgICAgICAgIDxzdHJpbmc+c2V0IHRpdGxlIHVzaW5nIHByZXNldDwvc3RyaW5nPgogICAgICAg
ICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3Bl
cnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c2V0
IHRpdGxlIHVzaW5nIHByZXNldDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJv
cGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+
CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c2V0IHRpdGxlIHVzaW5nIHByZXNldDwv
c3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAg
ICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAg
ICAgICAgICAgPHN0cmluZz5zZXQgdGl0bGUgdXNpbmcgcHJlc2V0PC9zdHJpbmc+CiAgICAgICAg
ICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVy
dHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgICAgICAg
PHN0cmluZz5zZXQgdGl0bGUgdXNpbmcgcHJlc2V0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAg
ICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgICAgICA8aXRlbT4KICAgICAgICAg
ICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAg
ICAgICAgPHN0cmluZz5PcmRlciBTaGVldDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgICAg
ICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAg
ICAgICAgICAgICA8aXRlbT4KICAgICAgICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9
InRleHQiPgogICAgICAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5Ib2xpZGF5PC9zdHJpbmc+
CiAgICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAg
ICAgPC9pdGVtPgogICAgICAgICAgICAgICAgICAgICAgIDxpdGVtPgogICAgICAgICAgICAgICAg
ICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgICAgICAgICA8
c3RyaW5nPlBpY2tsaXN0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICAgICAgIDwvcHJvcGVy
dHk+CiAgICAgICAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgICAgICAg
IDxpdGVtPgogICAgICAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAg
ICAgICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkF1ZGl0PC9zdHJpbmc+CiAgICAgICAgICAg
ICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICAgICAgPC9pdGVtPgog
ICAgICAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICAgICAgIDwvaXRl
bT4KICAgICAgICAgICAgICAgICAgICA8L2xheW91dD4KICAgICAgICAgICAgICAgICAgIDwvd2lk
Z2V0PgogICAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAgPC9sYXlvdXQ+
CiAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAg
ICAgICAgIDwvbGF5b3V0PgogICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgIDwvd2lk
Z2V0PgogICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICA8aXRlbSByb3c9IjIiIGNvbHVtbj0i
MCI+CiAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJnZW5fc2hl
ZXQiPgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAg
IDxzdHJpbmc+Z2VuZXJhdGUgdGhlIG9yZGVyIHNoZWV0IGluIGh0bWw8L3N0cmluZz4KICAgICAg
ICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlw
Ij4KICAgICAgICAgICAgICA8c3RyaW5nPmdlbmVyYXRlIHRoZSBvcmRlciBzaGVldCBpbiBodG1s
PC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5
IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgPHN0cmluZz5nZW5lcmF0ZSB0aGUgb3Jk
ZXIgc2hlZXQgaW4gaHRtbDwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAg
ICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgPHN0
cmluZz5nZW5lcmF0ZSB0aGUgb3JkZXIgc2hlZXQgaW4gaHRtbDwvc3RyaW5nPgogICAgICAgICAg
ICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVz
Y3JpcHRpb24iPgogICAgICAgICAgICAgIDxzdHJpbmc+Z2VuZXJhdGUgdGhlIG9yZGVyIHNoZWV0
IGluIGh0bWw8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8
cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgPHN0cmluZz5HZW5lcmF0ZSBPcmRl
ciBTaGVldDwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgPC93
aWRnZXQ+CiAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgPC9sYXlvdXQ+CiAgICAgICAgIDwv
d2lkZ2V0PgogICAgICAgIDwvaXRlbT4KICAgICAgIDwvbGF5b3V0PgogICAgICA8L3dpZGdldD4K
ICAgICAgPHdpZGdldCBjbGFzcz0iUVdpZGdldCIgbmFtZT0idGFiXzIiPgogICAgICAgPGF0dHJp
YnV0ZSBuYW1lPSJ0aXRsZSI+CiAgICAgICAgPHN0cmluZz5JbWFnZTJUZXh0PC9zdHJpbmc+CiAg
ICAgICA8L2F0dHJpYnV0ZT4KICAgICAgIDxsYXlvdXQgY2xhc3M9IlFHcmlkTGF5b3V0IiBuYW1l
PSJncmlkTGF5b3V0XzEwIj4KICAgICAgICA8aXRlbSByb3c9IjIiIGNvbHVtbj0iMiI+CiAgICAg
ICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJsb2FkIj4KICAgICAgICAgIDxw
cm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICA8c3RyaW5nPmxvYWQgaW1hZ2UgZmls
ZSBmaWxlPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPHByb3BlcnR5
IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgPHN0cmluZz5sb2FkIGltYWdlIGZpbGUgZmls
ZTwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1l
PSJ3aGF0c1RoaXMiPgogICAgICAgICAgIDxzdHJpbmc+bG9hZCBpbWFnZSBmaWxlIGZpbGU8L3N0
cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNj
ZXNzaWJsZU5hbWUiPgogICAgICAgICAgIDxzdHJpbmc+bG9hZCBpbWFnZSBmaWxlIGZpbGU8L3N0
cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNj
ZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICA8c3RyaW5nPmxvYWQgaW1hZ2UgZmlsZSBm
aWxlPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPHByb3BlcnR5IG5h
bWU9InRleHQiPgogICAgICAgICAgIDxzdHJpbmc+TG9hZCBJbWFnZTwvc3RyaW5nPgogICAgICAg
ICAgPC9wcm9wZXJ0eT4KICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgPC9pdGVtPgogICAgICAg
IDxpdGVtIHJvdz0iMiIgY29sdW1uPSIzIj4KICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hC
dXR0b24iIG5hbWU9IlNhdmUiPgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgog
ICAgICAgICAgIDxzdHJpbmc+c2F2ZTwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAg
ICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgIDxzdHJpbmc+c2F2
ZTwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1l
PSJ3aGF0c1RoaXMiPgogICAgICAgICAgIDxzdHJpbmc+c2F2ZTwvc3RyaW5nPgogICAgICAgICAg
PC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAg
ICAgICAgICAgPHN0cmluZz5zYXZlPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAg
ICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAg
PHN0cmluZz5zYXZlPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPHBy
b3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgIDxzdHJpbmc+U2F2ZTwvc3RyaW5nPgogICAg
ICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgPC9pdGVtPgogICAg
ICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSIwIiBjb2xzcGFuPSI0Ij4KICAgICAgICAgPHdpZGdl
dCBjbGFzcz0iUUdyb3VwQm94IiBuYW1lPSJncm91cEJveF80Ij4KICAgICAgICAgIDxwcm9wZXJ0
eSBuYW1lPSJ0aXRsZSI+CiAgICAgICAgICAgPHN0cmluZz5Db2x1bW5zPC9zdHJpbmc+CiAgICAg
ICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5h
bWU9ImdyaWRMYXlvdXRfMTIiPgogICAgICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSIyIj4K
ICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUZyYW1lIiBuYW1lPSJmcmFtZV81Ij4KICAgICAg
ICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJmcmFtZVNoYXBlIj4KICAgICAgICAgICAgICA8ZW51bT5R
RnJhbWU6OlN0eWxlZFBhbmVsPC9lbnVtPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAg
ICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJmcmFtZVNoYWRvdyI+CiAgICAgICAgICAgICAgPGVudW0+
UUZyYW1lOjpSYWlzZWQ8L2VudW0+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAg
ICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRMYXlvdXRfMTYiPgogICAg
ICAgICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgPHdpZGdl
dCBjbGFzcz0iUUxDRE51bWJlciIgbmFtZT0iY29sdW1uM19jb3VudCIvPgogICAgICAgICAgICAg
IDwvaXRlbT4KICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMSI+CiAgICAgICAg
ICAgICAgIDx3aWRnZXQgY2xhc3M9IlFMYWJlbCIgbmFtZT0iY29sdW1uM19sYWJlbCI+CiAgICAg
ICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgPHN0cmlu
Zz5MaW5lCkNvdW50PC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAg
ICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPGl0
ZW0gcm93PSIwIiBjb2x1bW49IjAiIHJvd3NwYW49IjIiPgogICAgICAgICAgICAgICA8d2lkZ2V0
IGNsYXNzPSJRUGxhaW5UZXh0RWRpdCIgbmFtZT0iY29sdW1uMyI+CiAgICAgICAgICAgICAgICA8
cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5jb2x1bW4z
IHRleHQ8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAg
ICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmNv
bHVtbjMgdGV4dDwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAg
ICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgIDxzdHJp
bmc+Y29sdW1uMyB0ZXh0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAg
ICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAg
ICAgICA8c3RyaW5nPmNvbHVtbjMgdGV4dDwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9w
ZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRp
b24iPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+Y29sdW1uMyB0ZXh0PC9zdHJpbmc+CiAgICAg
ICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InBs
YWNlaG9sZGVyVGV4dCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5jb2x1bW4gMzwvc3RyaW5n
PgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAg
ICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgPC9sYXlvdXQ+CiAgICAgICAgICAgIDwv
d2lkZ2V0PgogICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVt
bj0iMCI+CiAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJjb250
ZW50X3JlYWR5Ij4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAg
ICAgICAgICA8c3RyaW5nPmlmIGltYWdlIGNvbnRlbnQgaXMgcmVhZHkgdGhlbiB0aGlzIHdpbGwg
Y29weSB0aGUgY29udGVudCBpbnRvIHRoZSBjb2x1bW5zIGJlbG93PC9zdHJpbmc+CiAgICAgICAg
ICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+
CiAgICAgICAgICAgICAgPHN0cmluZz5pZiBpbWFnZSBjb250ZW50IGlzIHJlYWR5IHRoZW4gdGhp
cyB3aWxsIGNvcHkgdGhlIGNvbnRlbnQgaW50byB0aGUgY29sdW1ucyBiZWxvdzwvc3RyaW5nPgog
ICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0
c1RoaXMiPgogICAgICAgICAgICAgIDxzdHJpbmc+aWYgaW1hZ2UgY29udGVudCBpcyByZWFkeSB0
aGVuIHRoaXMgd2lsbCBjb3B5IHRoZSBjb250ZW50IGludG8gdGhlIGNvbHVtbnMgYmVsb3c8L3N0
cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFt
ZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgIDxzdHJpbmc+aWYgaW1hZ2UgY29udGVu
dCBpcyByZWFkeSB0aGVuIHRoaXMgd2lsbCBjb3B5IHRoZSBjb250ZW50IGludG8gdGhlIGNvbHVt
bnMgYmVsb3c8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8
cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICA8c3Ry
aW5nPmlmIGltYWdlIGNvbnRlbnQgaXMgcmVhZHkgdGhlbiB0aGlzIHdpbGwgY29weSB0aGUgY29u
dGVudCBpbnRvIHRoZSBjb2x1bW5zIGJlbG93PC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3Bl
cnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgIDxz
dHJpbmc+Q29udGVudCBSZWFkeTwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAg
ICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJpY29uIj4KICAgICAgICAgICAgICA8aWNvbnNldCB0
aGVtZT0iQ2hlY2siPgogICAgICAgICAgICAgICA8bm9ybWFsb2ZmPi48L25vcm1hbG9mZj4uPC9p
Y29uc2V0PgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgPC93aWRnZXQ+CiAg
ICAgICAgICAgPC9pdGVtPgogICAgICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSIxIj4KICAg
ICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUZyYW1lIiBuYW1lPSJmcmFtZV80Ij4KICAgICAgICAg
ICAgIDxwcm9wZXJ0eSBuYW1lPSJmcmFtZVNoYXBlIj4KICAgICAgICAgICAgICA8ZW51bT5RRnJh
bWU6OlN0eWxlZFBhbmVsPC9lbnVtPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAg
ICAgIDxwcm9wZXJ0eSBuYW1lPSJmcmFtZVNoYWRvdyI+CiAgICAgICAgICAgICAgPGVudW0+UUZy
YW1lOjpSYWlzZWQ8L2VudW0+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAg
PGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRMYXlvdXRfMTUiPgogICAgICAg
ICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgPHdpZGdldCBj
bGFzcz0iUUxDRE51bWJlciIgbmFtZT0iY29sdW1uMl9jb3VudCIvPgogICAgICAgICAgICAgIDwv
aXRlbT4KICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMSI+CiAgICAgICAgICAg
ICAgIDx3aWRnZXQgY2xhc3M9IlFMYWJlbCIgbmFtZT0iY29sdW1uMl9sYWJlbCI+CiAgICAgICAg
ICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5M
aW5lcwpDb3VudDwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAg
ICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgIDxpdGVt
IHJvdz0iMCIgY29sdW1uPSIwIiByb3dzcGFuPSIyIj4KICAgICAgICAgICAgICAgPHdpZGdldCBj
bGFzcz0iUVBsYWluVGV4dEVkaXQiIG5hbWU9ImNvbHVtbjIiPgogICAgICAgICAgICAgICAgPHBy
b3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+Y29sdW1uMiB0
ZXh0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAg
PHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5jb2x1
bW4yIHRleHQ8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAg
ICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICA8c3RyaW5n
PmNvbHVtbjIgdGV4dDwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAg
ICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAg
ICAgPHN0cmluZz5jb2x1bW4yIHRleHQ8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVy
dHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9u
Ij4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmNvbHVtbjIgdGV4dDwvc3RyaW5nPgogICAgICAg
ICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFj
ZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+Y29sdW1uIDI8L3N0cmluZz4K
ICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAg
ICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgIDwvbGF5b3V0PgogICAgICAgICAgICA8L3dp
ZGdldD4KICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49
IjEiPgogICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0iY2xlYXJf
Y29sdW1ucyI+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAg
ICAgPHN0cmluZz5DbGVhciBDb2x1bW5zPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5
PgogICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgPGl0
ZW0gcm93PSIxIiBjb2x1bW49IjAiPgogICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRRnJhbWUi
IG5hbWU9ImZyYW1lXzMiPgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImZyYW1lU2hhcGUi
PgogICAgICAgICAgICAgIDxlbnVtPlFGcmFtZTo6U3R5bGVkUGFuZWw8L2VudW0+CiAgICAgICAg
ICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImZyYW1lU2hhZG93
Ij4KICAgICAgICAgICAgICA8ZW51bT5RRnJhbWU6OlJhaXNlZDwvZW51bT4KICAgICAgICAgICAg
IDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8bGF5b3V0IGNsYXNzPSJRR3JpZExheW91dCIgbmFt
ZT0iZ3JpZExheW91dF8xNCI+CiAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjEi
PgogICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRTENETnVtYmVyIiBuYW1lPSJjb2x1bW4x
X2NvdW50Ii8+CiAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgIDxpdGVtIHJvdz0i
MCIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUxhYmVsIiBuYW1l
PSJjb2x1bW4xX2xhYmVsIj4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4K
ICAgICAgICAgICAgICAgICA8c3RyaW5nPkxpbmUKQ291bnQ8L3N0cmluZz4KICAgICAgICAgICAg
ICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgIDwv
aXRlbT4KICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMCIgcm93c3Bhbj0iMiI+
CiAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQbGFpblRleHRFZGl0IiBuYW1lPSJjb2x1
bW4xIj4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAg
ICAgICAgICA8c3RyaW5nPmNvbHVtbjEgdGV4dDwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9w
cm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAg
ICAgICAgICAgICAgIDxzdHJpbmc+Y29sdW1uMSB0ZXh0PC9zdHJpbmc+CiAgICAgICAgICAgICAg
ICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+
CiAgICAgICAgICAgICAgICAgPHN0cmluZz5jb2x1bW4xIHRleHQ8L3N0cmluZz4KICAgICAgICAg
ICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNz
aWJsZU5hbWUiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+Y29sdW1uMSB0ZXh0PC9zdHJpbmc+
CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5h
bWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5jb2x1
bW4xIHRleHQ8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAg
ICAgICA8cHJvcGVydHkgbmFtZT0icGxhY2Vob2xkZXJUZXh0Ij4KICAgICAgICAgICAgICAgICA8
c3RyaW5nPmNvbHVtbiAxPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAg
ICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICA8
L2xheW91dD4KICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgPC9pdGVtPgogICAgICAg
ICAgPC9sYXlvdXQ+CiAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgIDwvaXRlbT4KICAgICAgICA8
aXRlbSByb3c9IjIiIGNvbHVtbj0iMSI+CiAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0
dG9uIiBuYW1lPSJicm93c2VfaW1hZ2VfZmlsZSI+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0i
dG9vbFRpcCI+CiAgICAgICAgICAgPHN0cmluZz5icm93c2UgZm9yIGltYWdlIGZpbGUgdG8gbG9h
ZDwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1l
PSJzdGF0dXNUaXAiPgogICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGZvciBpbWFnZSBmaWxlIHRv
IGxvYWQ8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkg
bmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBmb3IgaW1hZ2UgZmls
ZSB0byBsb2FkPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPHByb3Bl
cnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBmb3Ig
aW1hZ2UgZmlsZSB0byBsb2FkPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAg
ICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgPHN0
cmluZz5icm93c2UgZm9yIGltYWdlIGZpbGUgdG8gbG9hZDwvc3RyaW5nPgogICAgICAgICAgPC9w
cm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICA8c3Ry
aW5nPkJyb3dzZTwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgPC93aWRn
ZXQ+CiAgICAgICAgPC9pdGVtPgogICAgICAgIDxpdGVtIHJvdz0iMiIgY29sdW1uPSIwIj4KICAg
ICAgICAgPHdpZGdldCBjbGFzcz0iUUxpbmVFZGl0IiBuYW1lPSJpbWFnZV9maWxlIj4KICAgICAg
ICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICA8c3RyaW5nPmltYWdlIGZp
bGU8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFt
ZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICA8c3RyaW5nPmltYWdlIGZpbGU8L3N0cmluZz4KICAg
ICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4K
ICAgICAgICAgICA8c3RyaW5nPmltYWdlIGZpbGU8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVy
dHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAg
IDxzdHJpbmc+aW1hZ2UgZmlsZTwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAg
ICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgIDxz
dHJpbmc+aW1hZ2UgZmlsZTwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAg
IDxwcm9wZXJ0eSBuYW1lPSJkcmFnRW5hYmxlZCI+CiAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9v
bD4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0icGxhY2Vo
b2xkZXJUZXh0Ij4KICAgICAgICAgICA8c3RyaW5nPkltYWdlIEZpbGUgdG8gcmVhZDwvc3RyaW5n
PgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJjbGVhckJ1
dHRvbkVuYWJsZWQiPgogICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICA8L3By
b3BlcnR5PgogICAgICAgICA8L3dpZGdldD4KICAgICAgICA8L2l0ZW0+CiAgICAgICAgPGl0ZW0g
cm93PSIwIiBjb2x1bW49IjAiIGNvbHNwYW49IjQiPgogICAgICAgICA8d2lkZ2V0IGNsYXNzPSJR
U2Nyb2xsQXJlYSIgbmFtZT0ic2Nyb2xsQXJlYV8yIj4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1l
PSJ3aWRnZXRSZXNpemFibGUiPgogICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAg
ICA8L3Byb3BlcnR5PgogICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVdpZGdldCIgbmFtZT0ic2Ny
b2xsQXJlYVdpZGdldENvbnRlbnRzXzIiPgogICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJnZW9t
ZXRyeSI+CiAgICAgICAgICAgIDxyZWN0PgogICAgICAgICAgICAgPHg+MDwveD4KICAgICAgICAg
ICAgIDx5PjA8L3k+CiAgICAgICAgICAgICA8d2lkdGg+NTIxPC93aWR0aD4KICAgICAgICAgICAg
IDxoZWlnaHQ+NDI4PC9oZWlnaHQ+CiAgICAgICAgICAgIDwvcmVjdD4KICAgICAgICAgICA8L3By
b3BlcnR5PgogICAgICAgICAgIDxsYXlvdXQgY2xhc3M9IlFHcmlkTGF5b3V0IiBuYW1lPSJncmlk
TGF5b3V0XzEzIj4KICAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjAiPgogICAgICAg
ICAgICAgPHdpZGdldCBjbGFzcz0iUUZyYW1lIiBuYW1lPSJmcmFtZV8yIj4KICAgICAgICAgICAg
ICA8cHJvcGVydHkgbmFtZT0iZnJhbWVTaGFwZSI+CiAgICAgICAgICAgICAgIDxlbnVtPlFGcmFt
ZTo6U3R5bGVkUGFuZWw8L2VudW0+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAg
ICAgICA8cHJvcGVydHkgbmFtZT0iZnJhbWVTaGFkb3ciPgogICAgICAgICAgICAgICA8ZW51bT5R
RnJhbWU6OlJhaXNlZDwvZW51bT4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAg
ICAgIDxsYXlvdXQgY2xhc3M9IlFHcmlkTGF5b3V0IiBuYW1lPSJncmlkTGF5b3V0XzExIj4KICAg
ICAgICAgICAgICAgPGl0ZW0gcm93PSIyIiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgPHdp
ZGdldCBjbGFzcz0iUVBsYWluVGV4dEVkaXQiIG5hbWU9ImltYWdlX2NvbnRlbnQiPgogICAgICAg
ICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJtaW5pbXVtU2l6ZSI+CiAgICAgICAgICAgICAgICAg
IDxzaXplPgogICAgICAgICAgICAgICAgICAgPHdpZHRoPjQwMDwvd2lkdGg+CiAgICAgICAgICAg
ICAgICAgICA8aGVpZ2h0PjQwMDwvaGVpZ2h0PgogICAgICAgICAgICAgICAgICA8L3NpemU+CiAg
ICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFt
ZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+Y29udGVudCBvZiBpbWFnZTwv
c3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHBy
b3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+Y29udGVu
dCBvZiBpbWFnZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAg
ICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgIDxz
dHJpbmc+Y29udGVudCBvZiBpbWFnZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVy
dHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAg
ICAgICAgICAgICAgICAgPHN0cmluZz5jb250ZW50IG9mIGltYWdlPC9zdHJpbmc+CiAgICAgICAg
ICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNj
ZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5jb250ZW50IG9m
IGltYWdlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAg
ICAgICA8cHJvcGVydHkgbmFtZT0idGFiQ2hhbmdlc0ZvY3VzIj4KICAgICAgICAgICAgICAgICAg
PGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAg
ICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFjZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICAg
ICA8c3RyaW5nPkltYWdlIENvbnRlbnQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3Bl
cnR5PgogICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgIDwvaXRlbT4KICAg
ICAgICAgICAgICAgPGl0ZW0gcm93PSIyIiBjb2x1bW49IjEiPgogICAgICAgICAgICAgICAgPHdp
ZGdldCBjbGFzcz0iUUdyYXBoaWNzVmlldyIgbmFtZT0iaW1hZ2VfcHJldmlldyI+CiAgICAgICAg
ICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICA8c3Ry
aW5nPnRyb3VibGUgc2hvb3QgaWYgc29tZXRoaW5nIGlzIHdyb25nPC9zdHJpbmc+CiAgICAgICAg
ICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3Rh
dHVzVGlwIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz50cm91YmxlIHNob290IGlmIHNvbWV0
aGluZyBpcyB3cm9uZzwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAg
ICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAg
IDxzdHJpbmc+dHJvdWJsZSBzaG9vdCBpZiBzb21ldGhpbmcgaXMgd3Jvbmc8L3N0cmluZz4KICAg
ICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1l
PSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+dHJvdWJsZSBzaG9v
dCBpZiBzb21ldGhpbmcgaXMgd3Jvbmc8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3Bl
cnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRp
b24iPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPnRyb3VibGUgc2hvb3QgaWYgc29tZXRoaW5n
IGlzIHdyb25nPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAg
ICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPC9s
YXlvdXQ+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAg
ICAgIDwvbGF5b3V0PgogICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgIDwvd2lkZ2V0PgogICAg
ICAgIDwvaXRlbT4KICAgICAgIDwvbGF5b3V0PgogICAgICA8L3dpZGdldD4KICAgICAgPHdpZGdl
dCBjbGFzcz0iUVdpZGdldCIgbmFtZT0idGFiXzMiPgogICAgICAgPGF0dHJpYnV0ZSBuYW1lPSJ0
aXRsZSI+CiAgICAgICAgPHN0cmluZz5TZXJ2ZXIgU2V0dGluZ3M8L3N0cmluZz4KICAgICAgIDwv
YXR0cmlidXRlPgogICAgICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRM
YXlvdXRfMTciPgogICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIwIj4KICAgICAgICAgPHdp
ZGdldCBjbGFzcz0iUVNjcm9sbEFyZWEiIG5hbWU9InNjcm9sbEFyZWFfMyI+CiAgICAgICAgICA8
cHJvcGVydHkgbmFtZT0id2lkZ2V0UmVzaXphYmxlIj4KICAgICAgICAgICA8Ym9vbD50cnVlPC9i
b29sPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFXaWRn
ZXQiIG5hbWU9InNjcm9sbEFyZWFXaWRnZXRDb250ZW50c18zIj4KICAgICAgICAgICA8cHJvcGVy
dHkgbmFtZT0iZ2VvbWV0cnkiPgogICAgICAgICAgICA8cmVjdD4KICAgICAgICAgICAgIDx4PjA8
L3g+CiAgICAgICAgICAgICA8eT4wPC95PgogICAgICAgICAgICAgPHdpZHRoPjQ0NTwvd2lkdGg+
CiAgICAgICAgICAgICA8aGVpZ2h0PjE5NzwvaGVpZ2h0PgogICAgICAgICAgICA8L3JlY3Q+CiAg
ICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICA8bGF5b3V0IGNsYXNzPSJRR3JpZExheW91
dCIgbmFtZT0iZ3JpZExheW91dF8yMCI+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1u
PSIwIj4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFHcm91cEJveCIgbmFtZT0iU2VydmVy
Q29ubmVjdCI+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRpdGxlIj4KICAgICAgICAg
ICAgICAgPHN0cmluZz5TZXJ2ZXIgQ29ubmVjdDwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJv
cGVydHk+CiAgICAgICAgICAgICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9Imdy
aWRMYXlvdXRfMTgiPgogICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMCI+CiAg
ICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9InNlcnZlcl9odHRw
Ij4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAg
ICAgICAgIDxzdHJpbmc+c2VydmVyIHBvcnQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3By
b3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAg
ICAgICAgICAgICAgICA8c3RyaW5nPnNlcnZlciBwb3J0PC9zdHJpbmc+CiAgICAgICAgICAgICAg
ICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlz
Ij4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5zZXJ2ZXIgcG9ydDwvc3RyaW5nPgogICAgICAg
ICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFj
Y2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5zZXJ2ZXIgcG9ydDwvc3Ry
aW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3Bl
cnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgIDxzdHJp
bmc+c2VydmVyIHBvcnQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAg
ICAgICAgICAgICAgIDxpdGVtPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4
dCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmh0dHA6Ly88L3N0cmluZz4KICAgICAgICAg
ICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAg
ICAgICAgPGl0ZW0+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAg
ICAgICAgICAgICAgICAgIDxzdHJpbmc+aHR0cHM6Ly88L3N0cmluZz4KICAgICAgICAgICAgICAg
ICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICA8
L3dpZGdldD4KICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICA8aXRlbSByb3c9
IjAiIGNvbHVtbj0iMiI+CiAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRTGluZUVkaXQi
IG5hbWU9InRva2VuIj4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+
CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YXV0aGVudGljYXRpb24gdG9rZW48L3N0cmluZz4K
ICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBu
YW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmF1dGhlbnRpY2F0aW9u
IHRva2VuPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAg
ICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgPHN0cmlu
Zz5hdXRoZW50aWNhdGlvbiB0b2tlbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVy
dHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAg
ICAgICAgICAgICAgICAgPHN0cmluZz5hdXRoZW50aWNhdGlvbiB0b2tlbjwvc3RyaW5nPgogICAg
ICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9
ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YXV0aGVu
dGljYXRpb24gdG9rZW48L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAg
ICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJkcmFnRW5hYmxlZCI+CiAgICAgICAgICAgICAg
ICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAg
ICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0icGxhY2Vob2xkZXJUZXh0Ij4KICAgICAgICAgICAg
ICAgICAgPHN0cmluZz5BdXRoZW50aWNhdGlvbiBUb2tlbjwvc3RyaW5nPgogICAgICAgICAgICAg
ICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImNsZWFyQnV0
dG9uRW5hYmxlZCI+CiAgICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAg
ICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAg
ICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIzIj4KICAg
ICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJ0ZXN0X2Nvbm5l
Y3Rpb24iPgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAg
ICAgICAgICAgICAgPHN0cmluZz50ZXN0IGNvbm5lY3Rpb248L3N0cmluZz4KICAgICAgICAgICAg
ICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNU
aXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPnRlc3QgY29ubmVjdGlvbjwvc3RyaW5nPgog
ICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5h
bWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+dGVzdCBjb25uZWN0aW9u
PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8
cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICA8c3RyaW5n
PnRlc3QgY29ubmVjdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAg
ICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAg
ICAgICAgICAgICAgICAgIDxzdHJpbmc+dGVzdCBjb25uZWN0aW9uPC9zdHJpbmc+CiAgICAgICAg
ICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4
dCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+Q29ubmVjdDwvc3RyaW5nPgogICAgICAgICAg
ICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAg
ICAgPC9pdGVtPgogICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMSI+CiAgICAg
ICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRTGluZUVkaXQiIG5hbWU9InNlcnZlcl9hZGRyZXNz
Ij4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAg
ICAgIDxzdHJpbmc+MTI3LjAuMC4xPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0
eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZHJhZ0VuYWJsZWQiPgogICAgICAg
ICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+
CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InBsYWNlaG9sZGVyVGV4dCI+CiAgICAg
ICAgICAgICAgICAgIDxzdHJpbmc+c2VydmVyIGFkZHJlc3M8L3N0cmluZz4KICAgICAgICAgICAg
ICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJjbGVhckJ1
dHRvbkVuYWJsZWQiPgogICAgICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAg
ICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAg
ICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iNCI+CiAg
ICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0ic2F2ZV9zZXJ2
ZXIiPgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAg
ICAgICAgICAgPHN0cmluZz5zYXZlIHRvIGNvbmZpZzwvc3RyaW5nPgogICAgICAgICAgICAgICAg
IDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+
CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c2F2ZSB0byBjb25maWc8L3N0cmluZz4KICAgICAg
ICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3
aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPnNhdmUgdG8gY29uZmlnPC9zdHJp
bmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVy
dHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPnNhdmUg
dG8gY29uZmlnPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAg
ICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAg
ICAgICAgICAgPHN0cmluZz5zYXZlIHRvIGNvbmZpZzwvc3RyaW5nPgogICAgICAgICAgICAgICAg
IDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAg
ICAgICAgICAgICAgICA8c3RyaW5nPlNhdmUKQ29uZmlnPC9zdHJpbmc+CiAgICAgICAgICAgICAg
ICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICA8
L2l0ZW0+CiAgICAgICAgICAgICAgPC9sYXlvdXQ+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAg
ICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICA8aXRlbSByb3c9IjEiIGNvbHVtbj0iMCI+CiAg
ICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRR3JvdXBCb3giIG5hbWU9ImV4cG9ydF9mcm9tX3Nl
cnZlciI+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRpdGxlIj4KICAgICAgICAgICAg
ICAgPHN0cmluZz5TZXJ2ZXIgdG8gRmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVy
dHk+CiAgICAgICAgICAgICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRM
YXlvdXRfMTkiPgogICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMCI+CiAgICAg
ICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRTGluZUVkaXQiIG5hbWU9InNlcnZlcl9leHBvcnRf
ZmlsZSI+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAg
ICAgICAgICAgICA8c3RyaW5nPmZpbGVuYW1lIGZvciBzZXJ2ZXIgdG8gZXhwb3J0IHRvPC9zdHJp
bmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVy
dHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5maWxlbmFtZSBm
b3Igc2VydmVyIHRvIGV4cG9ydCB0bzwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVy
dHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAg
ICAgICAgICAgIDxzdHJpbmc+ZmlsZW5hbWUgZm9yIHNlcnZlciB0byBleHBvcnQgdG88L3N0cmlu
Zz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0
eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZmlsZW5h
bWUgZm9yIHNlcnZlciB0byBleHBvcnQgdG88L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3By
b3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3Jp
cHRpb24iPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmZpbGVuYW1lIGZvciBzZXJ2ZXIgdG8g
ZXhwb3J0IHRvPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAg
ICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+
c2VydmVyX2V4cG9ydC5jc3Y8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5Pgog
ICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJkcmFnRW5hYmxlZCI+CiAgICAgICAgICAg
ICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAg
ICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0icGxhY2Vob2xkZXJUZXh0Ij4KICAgICAgICAg
ICAgICAgICAgPHN0cmluZz5maWxlX3BhdGhfZm9yX3NlcnZlcl9leHBvcnQvPC9zdHJpbmc+CiAg
ICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFt
ZT0iY2xlYXJCdXR0b25FbmFibGVkIj4KICAgICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9v
bD4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPC93aWRnZXQ+
CiAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1
bW49IjEiPgogICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9
ImJyb3dzZV9zZXJ2ZXJfZXhwb3J0Ij4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0i
dG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGV4cG9ydCBmaWxlPC9z
dHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJv
cGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2Ug
ZXhwb3J0IGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAg
ICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICA8
c3RyaW5nPmJyb3dzZSBleHBvcnQgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJv
cGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4K
ICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgZXhwb3J0IGZpbGU8L3N0cmluZz4KICAg
ICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1l
PSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dz
ZSBleHBvcnQgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAg
ICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICA8c3Ry
aW5nPkJyb3dzZSBFeHBvcnQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5Pgog
ICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAg
ICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjIiPgogICAgICAgICAgICAgICAgPHdpZGdldCBj
bGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9ImV4cG9ydF90b19maWxlIj4KICAgICAgICAgICAgICAg
ICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZXhw
b3J0IHNlcnZlciB0byBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4K
ICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAg
ICAgICAgPHN0cmluZz5leHBvcnQgc2VydmVyIHRvIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAg
ICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1Ro
aXMiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmV4cG9ydCBzZXJ2ZXIgdG8gZmlsZTwvc3Ry
aW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3Bl
cnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5leHBv
cnQgc2VydmVyIHRvIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5Pgog
ICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgog
ICAgICAgICAgICAgICAgICA8c3RyaW5nPmV4cG9ydCBzZXJ2ZXIgdG8gZmlsZTwvc3RyaW5nPgog
ICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5h
bWU9InRleHQiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPkV4cG9ydDwvc3RyaW5nPgogICAg
ICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAg
ICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgIDwvbGF5b3V0PgogICAgICAgICAgICAgPC93
aWRnZXQ+CiAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICA8L2xheW91dD4KICAgICAgICAg
IDwvd2lkZ2V0PgogICAgICAgICA8L3dpZGdldD4KICAgICAgICA8L2l0ZW0+CiAgICAgICA8L2xh
eW91dD4KICAgICAgPC93aWRnZXQ+CiAgICAgPC93aWRnZXQ+CiAgICA8L2l0ZW0+CiAgIDwvbGF5
b3V0PgogIDwvd2lkZ2V0PgogIDx3aWRnZXQgY2xhc3M9IlFNZW51QmFyIiBuYW1lPSJtZW51YmFy
Ij4KICAgPHByb3BlcnR5IG5hbWU9Imdlb21ldHJ5Ij4KICAgIDxyZWN0PgogICAgIDx4PjA8L3g+
CiAgICAgPHk+MDwveT4KICAgICA8d2lkdGg+OTkxPC93aWR0aD4KICAgICA8aGVpZ2h0PjMyPC9o
ZWlnaHQ+CiAgICA8L3JlY3Q+CiAgIDwvcHJvcGVydHk+CiAgIDx3aWRnZXQgY2xhc3M9IlFNZW51
IiBuYW1lPSJtZW51RmlsZSI+CiAgICA8cHJvcGVydHkgbmFtZT0idGl0bGUiPgogICAgIDxzdHJp
bmc+JmFtcDtGaWxlPC9zdHJpbmc+CiAgICA8L3Byb3BlcnR5PgogICAgPGFkZGFjdGlvbiBuYW1l
PSJhY3Rpb25fRXhpdCIvPgogICA8L3dpZGdldD4KICAgPHdpZGdldCBjbGFzcz0iUU1lbnUiIG5h
bWU9Im1lbnVfSGVscCI+CiAgICA8cHJvcGVydHkgbmFtZT0idGl0bGUiPgogICAgIDxzdHJpbmc+
JmFtcDtIZWxwPC9zdHJpbmc+CiAgICA8L3Byb3BlcnR5PgogICAgPGFkZGFjdGlvbiBuYW1lPSJh
Y3Rpb25fQWJvdXQiLz4KICAgPC93aWRnZXQ+CiAgIDxhZGRhY3Rpb24gbmFtZT0ibWVudUZpbGUi
Lz4KICAgPGFkZGFjdGlvbiBuYW1lPSJtZW51X0hlbHAiLz4KICA8L3dpZGdldD4KICA8d2lkZ2V0
IGNsYXNzPSJRU3RhdHVzQmFyIiBuYW1lPSJzdGF0dXNiYXIiLz4KICA8YWN0aW9uIG5hbWU9ImFj
dGlvbl9FeGl0Ij4KICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgPHN0cmluZz4mYW1wO0V4
aXQ8L3N0cmluZz4KICAgPC9wcm9wZXJ0eT4KICA8L2FjdGlvbj4KICA8YWN0aW9uIG5hbWU9ImFj
dGlvbl9BYm91dCI+CiAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgIDxzdHJpbmc+JmFtcDtB
Ym91dDwvc3RyaW5nPgogICA8L3Byb3BlcnR5PgogIDwvYWN0aW9uPgogPC93aWRnZXQ+CiA8cmVz
b3VyY2VzLz4KIDxjb25uZWN0aW9ucz4KICA8Y29ubmVjdGlvbj4KICAgPHNlbmRlcj5hY3Rpb25f
RXhpdDwvc2VuZGVyPgogICA8c2lnbmFsPnRyaWdnZXJlZCgpPC9zaWduYWw+CiAgIDxyZWNlaXZl
cj5Ib21lMkJhcjwvcmVjZWl2ZXI+CiAgIDxzbG90PmNsb3NlKCk8L3Nsb3Q+CiAgIDxoaW50cz4K
ICAgIDxoaW50IHR5cGU9InNvdXJjZWxhYmVsIj4KICAgICA8eD4tMTwveD4KICAgICA8eT4tMTwv
eT4KICAgIDwvaGludD4KICAgIDxoaW50IHR5cGU9ImRlc3RpbmF0aW9ubGFiZWwiPgogICAgIDx4
PjM5OTwveD4KICAgICA8eT4yOTk8L3k+CiAgICA8L2hpbnQ+CiAgIDwvaGludHM+CiAgPC9jb25u
ZWN0aW9uPgogIDxjb25uZWN0aW9uPgogICA8c2VuZGVyPnRpdGxlX3ByZXNldHM8L3NlbmRlcj4K
ICAgPHNpZ25hbD5jdXJyZW50VGV4dENoYW5nZWQoUVN0cmluZyk8L3NpZ25hbD4KICAgPHJlY2Vp
dmVyPm9yZGVyX3NoZWV0X3RpdGxlPC9yZWNlaXZlcj4KICAgPHNsb3Q+c2V0VGV4dChRU3RyaW5n
KTwvc2xvdD4KICAgPGhpbnRzPgogICAgPGhpbnQgdHlwZT0ic291cmNlbGFiZWwiPgogICAgIDx4
PjM4NjwveD4KICAgICA8eT4yNzU8L3k+CiAgICA8L2hpbnQ+CiAgICA8aGludCB0eXBlPSJkZXN0
aW5hdGlvbmxhYmVsIj4KICAgICA8eD4zODY8L3g+CiAgICAgPHk+MTkzPC95PgogICAgPC9oaW50
PgogICA8L2hpbnRzPgogIDwvY29ubmVjdGlvbj4KIDwvY29ubmVjdGlvbnM+CjwvdWk+Cg==
    '''

    icon='''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'''
    def setIconWindow(self):
        bits=base64.b64decode(self.icon)
        pixmap=QPixmap()
        pixmap.loadFromData(bits)
        icon=QIcon(pixmap)
        self.window.setWindowIcon(icon)

    def __init__(self,parent=None):
        if os.geteuid() == 0:
            self.window=uic.loadUi("main.ui")
            exit("you should not be root!")
        self.app=QApplication(sys.argv)
        super().__init__()
        if len(sys.argv) > 1:
            if sys.argv[1] == 'debug':
                self.window=uic.loadUi("main.ui")
            else:
                self.window=uic.loadUi(StringIO(base64.b64decode(self.ui).decode('utf-8')))
                self.setIconWindow()
        else:
            self.window=uic.loadUi(StringIO(base64.b64decode(self.ui).decode('utf-8')))
            self.setIconWindow()

            #self.window=uic.loadUi("main.ui")
        self.threadpool=QThreadPool()
        self.setup_external_worker()
        self.setup_buttons()
        self.load_server_config()
        self.poller=QTimer(self)
        self.poller.timeout.connect(self.run_pollthread)
        self.poller.start(1000)

        self.window.show()
        self.app.exec()

Window()
