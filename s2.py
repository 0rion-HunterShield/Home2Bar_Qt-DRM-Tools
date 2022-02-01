#! /usr/bin/env python3
import platform

from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import pyqtSlot,pyqtSignal
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView
from datetime import datetime
from copy import deepcopy as copy
from PIL import Image,ImageDraw
import pyzbar.pyzbar as zbar
from io import BytesIO
from cryptography.fernet import Fernet
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from pathlib import Path
from barcode import generate,Code128,writer
from barcode import writer as WRITER
from pyzbar.pyzbar import decode
from PIL import Image
import shutil,csv,string,requests,time,sys,os,pyqrcode,base64,json,cairosvg,pyqrcode,random,pickle,shutil
from io import BytesIO,StringIO
from PIL.ImageQt import ImageQt
import lzma,tarfile
from cairosvg import svg2png
#import pyocr
#import pyocr.builders
import pytesseract,random
#local import
from qrtools import qrtools
from ast import literal_eval as evaluate
if len(sys.argv) > 1:
    from client_model import HolzCraftsFrameEnum
    from modsvg import Modify
    from file2qr import File2QR
else:
    	
	import json,os,sys,enum
	
	
	class HolzCraftsFrameEnum(enum.Enum):
		product_type=[('Frame', 'Frame'), ('Stand', 'Stand'), ('Ornament', 'Ornament'), ('Name-Chain', 'Name-Chain'), ('Name-Tag', 'Name-Tag'), ('Oven-Rack Push-Pull', 'Oven-Rack Push-Pull'), ('Trophy', 'Trophy'), ('Cutting Board', 'Cutting Board'), ('Quick Conversion Stick', 'Quick Conversion Stick'), ('Generated_SKU', 'Generated_SKU'), ('Wall Deco/Plaque', 'Wall Deco/Plaque'), ('Wall Deco/Name Letters', 'Wall Deco/Name Letters'), ('Sign', 'Sign'), ('Python Code', 'Python Code'), ('HTML CODE', 'HTML CODE'), ('Spread Sheet', 'Spread Sheet'), ('SVG FILE', 'SVG FILE'), ('Product-Plan/Product-Demo', 'Product-Plan/Product-Demo'), ('W-2', 'W-2'), ('1099-INT', '1099-INT'), ('1099-C', '1099-C'), ('General Document', 'General Document')]
		size=[('Other', 'Other'), ('Other-Check_Diameter', 'Other-Check_Diameter'), ('2x2', '2x2'), ('3x3', '3x3'), ('3x5', '3x5'), ('3.5x5', '3.5x5'), ('4x4', '4x4'), ('4x6', '4x6'), ('4x10', '4x10'), ('5x5', '5x5'), ('5x7', '5x7'), ('6x6', '6x6'), ('8x6', '8x6'), ('7x7', '7x7'), ('8x8', '8x8'), ('8x10', '8x10'), ('8.5x10', '8.5x10'), ('8x12', '8x12'), ('9x12', '9x12'), ('10x13', '10x13'), ('10x12', '10x12'), ('11x14', '11x14'), ('12x12', '12x12')]
		can_hold_glass=[('yes', 'yes'), ('no', 'no'), ('Other', 'Other')]
		has_glass=[('yes', 'yes'), ('no', 'no'), ('plexiglass', 'plexiglass'), ('lexan', 'lexan'), ('acrylic', 'acrylic'), ('Other', 'Other')]
		can_hold_canvas=[('yes', 'yes'), ('no', 'no'), ('Other', 'Other')]
		has_canvas=[('yes', 'yes'), ('no', 'no'), ('ChipBoard', 'ChipBoard'), ('masonite', 'masonite'), ('Other', 'Other')]
		orientation=[('portrait', 'portrait'), ('landscape', 'landscape'), ('Other', 'Other')]
		wood_type=[('maple', 'maple'), ('redwood', 'redwood'), ('red oak', 'red oak'), ('alder', 'alder'), ('poplar', 'poplar'), ('birch', 'birch'), ('fir', 'fir'), ('pine', 'pine'), ('oak', 'oak'), ('cherry', 'cherry'), ('walnut', 'walnut'), ('mahogany', 'mahogany'), ('cherry-redoak', 'cherry-redoak'), ('cherry-mahogany', 'cherry-mahogany'), ('cherry-walnut', 'cherry-walnut'), ('maple-walnut', 'maple-walnut'), ('maple-cherry', 'maple-cherry'), ('maple-mahogany', 'maple-mahogany'), ('constuction-lumber', 'constuction-lumber'), ('Other', 'Other'), ('Other(See Comments)', 'Other(See Comments)')]
		front_outer_profile=[('Chamfer', 'Chamfer'), ('Double Roman Ogee', 'Double Roman Ogee'), ('Classical', 'Classical'), ('Roman Ogee', 'Roman Ogee'), ('Cove', 'Cove'), ('Classical Cove', 'Classical Cove'), ('Round Over', 'Round Over'), ('Beading', 'Beading'), ('None', 'None'), ('Other', 'Other')]
		front_inner_profile=[('None', 'None'), ('Chamfer', 'Chamfer'), ('Other', 'Other')]
		rear_inner_profile=[('Round Over', 'Round Over'), ('Beading', 'Beading'), ('Chamfer', 'Chamfer'), ('None', 'None'), ('Other', 'Other')]
		center_inner_profile=[('Chamfer', 'Chamfer'), ('Double Roman Ogee', 'Double Roman Ogee'), ('Classical', 'Classical'), ('Roman Ogee', 'Roman Ogee'), ('Cove', 'Cove'), ('Classical Cove', 'Classical Cove'), ('Round Over', 'Round Over'), ('Beading', 'Beading'), ('None', 'None'), ('Other', 'Other')]
		center_outer_profile=[('Chamfer', 'Chamfer'), ('Double Roman Ogee', 'Double Roman Ogee'), ('Classical', 'Classical'), ('Roman Ogee', 'Roman Ogee'), ('Cove', 'Cove'), ('Classical Cove', 'Classical Cove'), ('Round Over', 'Round Over'), ('Beading', 'Beading'), ('None', 'None'), ('Other', 'Other')]
		finish_type=[('linseed', 'linseed'), ('chalk-paint', 'chalk-paint'), ('None', 'None'), ('Other', 'Other'), ('polyurathane-water gloss', 'polyurathane-water gloss'), ('polyurathane-water semi-gloss', 'polyurathane-water semi-gloss'), ('polyurathane-water satin', 'polyurathane-water satin'), ('polyurathane-water matte', 'polyurathane-water matte'), ('polyurathane-water Other', 'polyurathane-water Other'), ('polyurathane-oil gloss', 'polyurathane-oil gloss'), ('polyurathane-oil semi-gloss', 'polyurathane-oil semi-gloss'), ('polyurathane-oil satin', 'polyurathane-oil satin'), ('polyurathane-oil matte', 'polyurathane-oil matte'), ('polyurathane-oil Other', 'polyurathane-oil Other'), ('spar-urathane-water gloss', 'spar-urathane-water gloss'), ('spar-urathane-water semi-gloss', 'spar-urathane-water semi-gloss'), ('spar-urathane-water satin', 'spar-urathane-water satin'), ('spar-urathane-water matte', 'spar-urathane-water matte'), ('spar-urathane-water Other', 'spar-urathane-water Other'), ('spar-urathane-oil gloss', 'spar-urathane-oil gloss'), ('spar-urathane-oil semi-gloss', 'spar-urathane-oil semi-gloss'), ('spar-urathane-oil satin', 'spar-urathane-oil satin'), ('spar-urathane-oil matte', 'spar-urathane-oil matte'), ('spar-urathane-oil Other', 'spar-urathane-oil Other'), ('Other gloss', 'Other gloss'), ('Other semi-gloss', 'Other semi-gloss'), ('Other satin', 'Other satin'), ('Other matte', 'Other matte'), ('Other Other', 'Other Other')]
		stackable=[('yes', 'yes'), ('no', 'no'), ('Other', 'Other')]
		custom_engraved=[('yes', 'yes'), ('no', 'no'), ('Other', 'Other')]
		sold=[('yes', 'yes'), ('no', 'no'), ('Other', 'Other')]
		stainable=[('yes', 'yes'), ('no', 'no'), ('Other', 'Other')]
		sku=enum.auto()
		price=enum.auto()
		frame_shape=[('square', 'square'), ('hexagonal', 'hexagonal'), ('octoganal', 'octoganal'), ('Other', 'Other')]
		other_frame_size_diameter_unit=[('inch', 'inch'), ('foot', 'foot'), ('yard', 'yard'), ('centimeter', 'centimeter'), ('meter', 'meter'), ('millimeter', 'millimeter'), ('Other', 'Other')]
		item_weight_unit=[('lb', 'lb'), ('oz', 'oz'), ('gram', 'gram'), ('kg', 'kg'), ('Other', 'Other')]
		item_weight=enum.auto()
		stain=enum.auto()
		comments=enum.auto()
		other_frame_size_diameter=enum.auto()
		sold_to=enum.auto()
		paid_for=[('yes', 'yes'), ('no', 'no'), ('Other', 'Other')]
		amount_paid=enum.auto()
		id=enum.auto()
		front=enum.auto()
	
		corner=enum.auto()
	
		rear=enum.auto()
	
		engraving_zip=enum.auto()
	
		def __fields__(self):
			return ['product_type', 'size', 'can_hold_glass', 'has_glass', 'can_hold_canvas', 'has_canvas', 'orientation', 'wood_type', 'front_outer_profile', 'front_inner_profile', 'rear_inner_profile', 'center_inner_profile', 'center_outer_profile', 'finish_type', 'stackable', 'custom_engraved', 'sold', 'stainable', 'sku', 'price', 'frame_shape', 'other_frame_size_diameter_unit', 'item_weight_unit', 'item_weight', 'stain', 'comments', 'other_frame_size_diameter', 'sold_to', 'paid_for', 'amount_paid', 'id']
	import lxml,os,sys,json,base64
	from io import BytesIO
	from lxml import etree
	from pathlib import Path
	class Modify:
	    svgdata='''PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoKPHN2ZwogICB3aWR0aD0iMjEwbW0iCiAgIGhlaWdodD0iMjk3bW0iCiAgIHZpZXdCb3g9IjAgMCAyMTAgMjk3IgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmc0MDk1NyIKICAgaW5rc2NhcGU6dmVyc2lvbj0iMS4xLjEgKDNiZjVhZTBkMjUsIDIwMjEtMDktMjAsIGN1c3RvbSkiCiAgIHNvZGlwb2RpOmRvY25hbWU9InVwY190ZW1wbGF0ZS5zdmciCiAgIHhtbG5zOmlua3NjYXBlPSJodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy9uYW1lc3BhY2VzL2lua3NjYXBlIgogICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5ldC9EVEQvc29kaXBvZGktMC5kdGQiCiAgIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHNvZGlwb2RpOm5hbWVkdmlldwogICAgIGlkPSJuYW1lZHZpZXc0MDk1OSIKICAgICBwYWdlY29sb3I9IiNmZmZmZmYiCiAgICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiCiAgICAgYm9yZGVyb3BhY2l0eT0iMS4wIgogICAgIGlua3NjYXBlOnBhZ2VzaGFkb3c9IjIiCiAgICAgaW5rc2NhcGU6cGFnZW9wYWNpdHk9IjAuMCIKICAgICBpbmtzY2FwZTpwYWdlY2hlY2tlcmJvYXJkPSIwIgogICAgIGlua3NjYXBlOmRvY3VtZW50LXVuaXRzPSJtbSIKICAgICBzaG93Z3JpZD0iZmFsc2UiCiAgICAgaW5rc2NhcGU6c25hcC1nbG9iYWw9InRydWUiCiAgICAgaW5rc2NhcGU6em9vbT0iMS4wNDQ0MjA5IgogICAgIGlua3NjYXBlOmN4PSIzMjQuNTgxNzgiCiAgICAgaW5rc2NhcGU6Y3k9IjU1MC4wNjU1OSIKICAgICBpbmtzY2FwZTp3aW5kb3ctd2lkdGg9IjE5MjAiCiAgICAgaW5rc2NhcGU6d2luZG93LWhlaWdodD0iMTAxNSIKICAgICBpbmtzY2FwZTp3aW5kb3cteD0iMCIKICAgICBpbmtzY2FwZTp3aW5kb3cteT0iMCIKICAgICBpbmtzY2FwZTp3aW5kb3ctbWF4aW1pemVkPSIxIgogICAgIGlua3NjYXBlOmN1cnJlbnQtbGF5ZXI9Imc5OTAiIC8+CiAgPGRlZnMKICAgICBpZD0iZGVmczQwOTU0Ij4KICAgIDxyZWN0CiAgICAgICB4PSIxNjguMTY2MDEiCiAgICAgICB5PSI4MC4yOTAxMTIiCiAgICAgICB3aWR0aD0iMjMzLjkzNDAzIgogICAgICAgaGVpZ2h0PSI0NS44ODkyNzYiCiAgICAgICBpZD0icmVjdDI1NzEiIC8+CiAgICA8cmVjdAogICAgICAgeD0iMTMyLjQ4MDI0IgogICAgICAgeT0iMzY4LjcwMDY2IgogICAgICAgd2lkdGg9IjY3NC4xNDA2IgogICAgICAgaGVpZ2h0PSI1Mi45NTAzODYiCiAgICAgICBpZD0icmVjdDI3OTk4IiAvPgogICAgPHJlY3QKICAgICAgIHg9IjE5NS4xNzM4NCIKICAgICAgIHk9IjIwOS45MDA5OSIKICAgICAgIHdpZHRoPSIzNzcuMTgxOTkiCiAgICAgICBoZWlnaHQ9IjUyLjE0MDkxNCIKICAgICAgIGlkPSJyZWN0MTc2NjAiIC8+CiAgICA8cmVjdAogICAgICAgeD0iMTA4LjEwMDM4IgogICAgICAgeT0iMjA3LjkzNzk5IgogICAgICAgd2lkdGg9IjczLjI5MDY1MSIKICAgICAgIGhlaWdodD0iNDkuMzIxMjk4IgogICAgICAgaWQ9InJlY3QyODcyIiAvPgogICAgPHJlY3QKICAgICAgIHg9IjEzMy42NzY3MSIKICAgICAgIHk9IjQyNS4xMTk2OSIKICAgICAgIHdpZHRoPSI0NjYuMzYwNDMiCiAgICAgICBoZWlnaHQ9Ijg0LjI5ODI0NiIKICAgICAgIGlkPSJyZWN0NDQyNTciIC8+CiAgICA8cmVjdAogICAgICAgeD0iMTMzLjY3NjcxIgogICAgICAgeT0iNDI1LjExOTY5IgogICAgICAgd2lkdGg9IjQ2Ni4zNjA0MyIKICAgICAgIGhlaWdodD0iODQuMjk4MjQ2IgogICAgICAgaWQ9InJlY3QyNSIgLz4KICAgIDxyZWN0CiAgICAgICB4PSIxMzMuNjc2NzEiCiAgICAgICB5PSI0MjUuMTE5NjkiCiAgICAgICB3aWR0aD0iNDY2LjM2MDQzIgogICAgICAgaGVpZ2h0PSI4NC4yOTgyNDYiCiAgICAgICBpZD0icmVjdDYyIiAvPgogICAgPHJlY3QKICAgICAgIHg9IjE2OC4xNjYwMSIKICAgICAgIHk9IjgwLjI5MDExMiIKICAgICAgIHdpZHRoPSIyMzMuOTM0MDMiCiAgICAgICBoZWlnaHQ9IjQ1Ljg4OTI3NiIKICAgICAgIGlkPSJyZWN0MTk4ODkiIC8+CiAgICA8cmVjdAogICAgICAgeD0iMTY4LjE2NjAxIgogICAgICAgeT0iODAuMjkwMTEyIgogICAgICAgd2lkdGg9IjIzMy45MzQwMyIKICAgICAgIGhlaWdodD0iNDUuODg5Mjc2IgogICAgICAgaWQ9InJlY3QyMDU3NCIgLz4KICAgIDxyZWN0CiAgICAgICB4PSIxNjguMTY2MDEiCiAgICAgICB5PSI4MC4yOTAxMTIiCiAgICAgICB3aWR0aD0iMjMzLjkzNDAzIgogICAgICAgaGVpZ2h0PSI0NS44ODkyNzYiCiAgICAgICBpZD0icmVjdDk3MCIgLz4KICA8L2RlZnM+CiAgPGcKICAgICBpbmtzY2FwZTpsYWJlbD0iTGF5ZXIgMSIKICAgICBpbmtzY2FwZTpncm91cG1vZGU9ImxheWVyIgogICAgIGlkPSJsYXllcjEiPgogICAgPGcKICAgICAgIGlkPSJnOTQ4Ij4KICAgICAgPHRleHQKICAgICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yMzc3NjYxNiwwLDAsMC4zMjEyMDA3OSwyNC41OTUyNDcsNTkuNDc0MDc3KSIKICAgICAgICAgaWQ9InRleHQyMDU1MiIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZTo0MHB4O2xpbmUtaGVpZ2h0OjEuMjU7Zm9udC1mYW1pbHk6J0Jsb29kIENyb3cgSXRhbGljJzstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidCbG9vZCBDcm93IEl0YWxpYywgJztsZXR0ZXItc3BhY2luZzowcHg7d29yZC1zcGFjaW5nOjBweDt3aGl0ZS1zcGFjZTpwcmU7c2hhcGUtaW5zaWRlOnVybCgjcmVjdDIwNTc0KSIKICAgICAgICAgaW5rc2NhcGU6ZXhwb3J0LWZpbGVuYW1lPSIvc3J2L3NhbWJhL2NvbW1vbi9TdG9yZS9Ib2x6Y3JhZnRzIHJlbW90ZS9zdmcvcHJvZHVjdHMvZnJhbWVzLXVwYy8xMjkzOTg0MTQ5MDkucG5nIgogICAgICAgICBpbmtzY2FwZTpleHBvcnQteGRwaT0iMjg0LjQ3IgogICAgICAgICBpbmtzY2FwZTpleHBvcnQteWRwaT0iMjg0LjQ3Ij48dHNwYW4KICAgICAgICAgICB4PSIxNjguMTY2MDIiCiAgICAgICAgICAgeT0iMTE3Ljg5OTcxIgogICAgICAgICAgIGlkPSJ0c3BhbjI1ODEiPjx0c3BhbgogICAgICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyNS42ODE5cHg7Zm9udC1mYW1pbHk6J0FsdGVuZ2xpc2NoIE1GJzstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBbHRlbmdsaXNjaCBNRiciCiAgICAgICAgICAgICBpZD0idHNwYW4yNTc5Ij5Ib2x6Q3JhZnRzPC90c3Bhbj48L3RzcGFuPjwvdGV4dD4KICAgICAgPHRleHQKICAgICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgICAgc3R5bGU9ImZvbnQtc3R5bGU6bm9ybWFsO2ZvbnQtdmFyaWFudDpub3JtYWw7Zm9udC13ZWlnaHQ6bm9ybWFsO2ZvbnQtc3RyZXRjaDpub3JtYWw7Zm9udC1zaXplOjcuNjAzNjhweDtsaW5lLWhlaWdodDoxLjI1O2ZvbnQtZmFtaWx5OkFsdGUtU2Nod2FiYWNoZXI7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjpBbHRlLVNjaHdhYmFjaGVyO2xldHRlci1zcGFjaW5nOjBweDt3b3JkLXNwYWNpbmc6MHB4O3N0cm9rZS13aWR0aDowLjE5MDA5MyIKICAgICAgICAgeD0iMzEuMTE0MDY1IgogICAgICAgICB5PSI5My43NDg3MTEiCiAgICAgICAgIGlkPSJ1cGMxIgogICAgICAgICB0cmFuc2Zvcm09InNjYWxlKDAuOTY2ODExNTgsMS4wMzQzMjc3KSIKICAgICAgICAgaW5rc2NhcGU6ZXhwb3J0LWZpbGVuYW1lPSIvc3J2L3NhbWJhL2NvbW1vbi9TdG9yZS9Ib2x6Y3JhZnRzIHJlbW90ZS9zdmcvcHJvZHVjdHMvZnJhbWVzLXVwYy8xMjkzOTg0MTQ5MDkucG5nIgogICAgICAgICBpbmtzY2FwZTpleHBvcnQteGRwaT0iMjg0LjQ3IgogICAgICAgICBpbmtzY2FwZTpleHBvcnQteWRwaT0iMjg0LjQ3Ij48dHNwYW4KICAgICAgICAgICBpZD0idHNwYW4yMDU2NiIKICAgICAgICAgICBzdHlsZT0iZm9udC1zdHlsZTpub3JtYWw7Zm9udC12YXJpYW50Om5vcm1hbDtmb250LXdlaWdodDpub3JtYWw7Zm9udC1zdHJldGNoOm5vcm1hbDtmb250LWZhbWlseTpBbmNvbmEtTmFycm93Oy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246QW5jb25hLU5hcnJvdztzdHJva2Utd2lkdGg6MC4xOTAwOTMiCiAgICAgICAgICAgeD0iMzEuMTE0MDY1IgogICAgICAgICAgIHk9IjkzLjc0ODcxMSIKICAgICAgICAgICBzb2RpcG9kaTpyb2xlPSJsaW5lIj4xMjkzOTg0MTQ5MDk8L3RzcGFuPjwvdGV4dD4KICAgICAgPHRleHQKICAgICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgICAgc3R5bGU9ImZvbnQtc3R5bGU6bm9ybWFsO2ZvbnQtdmFyaWFudDpub3JtYWw7Zm9udC13ZWlnaHQ6bm9ybWFsO2ZvbnQtc3RyZXRjaDpub3JtYWw7Zm9udC1zaXplOjcuMTkzMjFweDtsaW5lLWhlaWdodDoxLjI1O2ZvbnQtZmFtaWx5OkFuY29uYS1OYXJyb3c7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjpBbmNvbmEtTmFycm93O2xldHRlci1zcGFjaW5nOjBweDt3b3JkLXNwYWNpbmc6MHB4O3N0cm9rZS13aWR0aDowLjE3OTgzIgogICAgICAgICB4PSIxMjkuNjUzNzYiCiAgICAgICAgIHk9Ijk0LjU4NzY4NSIKICAgICAgICAgaWQ9InBob25lMSIKICAgICAgICAgdHJhbnNmb3JtPSJzY2FsZSgwLjk3NTQ2Mzc2LDEuMDI1MTUzNCkiCiAgICAgICAgIGlua3NjYXBlOmV4cG9ydC1maWxlbmFtZT0iL3Nydi9zYW1iYS9jb21tb24vU3RvcmUvSG9semNyYWZ0cyByZW1vdGUvc3ZnL3Byb2R1Y3RzL2ZyYW1lcy11cGMvMTI5Mzk4NDE0OTA5LnBuZyIKICAgICAgICAgaW5rc2NhcGU6ZXhwb3J0LXhkcGk9IjI4NC40NyIKICAgICAgICAgaW5rc2NhcGU6ZXhwb3J0LXlkcGk9IjI4NC40NyI+PHRzcGFuCiAgICAgICAgICAgc29kaXBvZGk6cm9sZT0ibGluZSIKICAgICAgICAgICBpZD0idHNwYW4yMDU1OCIKICAgICAgICAgICBzdHlsZT0iZm9udC1zdHlsZTpub3JtYWw7Zm9udC12YXJpYW50Om5vcm1hbDtmb250LXdlaWdodDpub3JtYWw7Zm9udC1zdHJldGNoOm5vcm1hbDtmb250LWZhbWlseTpBbmNvbmEtTmFycm93Oy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246QW5jb25hLU5hcnJvdztzdHJva2Utd2lkdGg6MC4xNzk4MyIKICAgICAgICAgICB4PSIxMjkuNjUzNzYiCiAgICAgICAgICAgeT0iOTQuNTg3Njg1Ij4oODA0KSA4NTQtNDA1NyAoVGV4dCk8L3RzcGFuPjwvdGV4dD4KICAgICAgPHRleHQKICAgICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgICAgc3R5bGU9ImZvbnQtc3R5bGU6bm9ybWFsO2ZvbnQtdmFyaWFudDpub3JtYWw7Zm9udC13ZWlnaHQ6bm9ybWFsO2ZvbnQtc3RyZXRjaDpub3JtYWw7Zm9udC1zaXplOjguMzcwMDlweDtsaW5lLWhlaWdodDoxLjI1O2ZvbnQtZmFtaWx5OkFuY29uYS1OYXJyb3c7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjpBbmNvbmEtTmFycm93O2xldHRlci1zcGFjaW5nOjBweDt3b3JkLXNwYWNpbmc6MHB4O3N0cm9rZS13aWR0aDowLjIwOTI1MyIKICAgICAgICAgeD0iOTcuNzUyMTgyIgogICAgICAgICB5PSI5Ni45NjY4OTYiCiAgICAgICAgIGlkPSJ0ZXh0MjQzNzEiCiAgICAgICAgIGlua3NjYXBlOmV4cG9ydC1maWxlbmFtZT0iL3Nydi9zYW1iYS9jb21tb24vU3RvcmUvSG9semNyYWZ0cyByZW1vdGUvc3ZnL3Byb2R1Y3RzL2ZyYW1lcy11cGMvMTI5Mzk4NDE0OTA5LnBuZyIKICAgICAgICAgaW5rc2NhcGU6ZXhwb3J0LXhkcGk9IjI4NC40NyIKICAgICAgICAgaW5rc2NhcGU6ZXhwb3J0LXlkcGk9IjI4NC40NyI+PHRzcGFuCiAgICAgICAgICAgc29kaXBvZGk6cm9sZT0ibGluZSIKICAgICAgICAgICBpZD0idHNwYW4yNDM2OSIKICAgICAgICAgICBzdHlsZT0iZm9udC1zdHlsZTpub3JtYWw7Zm9udC12YXJpYW50Om5vcm1hbDtmb250LXdlaWdodDpub3JtYWw7Zm9udC1zdHJldGNoOm5vcm1hbDtmb250LWZhbWlseTpBbmNvbmEtTmFycm93Oy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246QW5jb25hLU5hcnJvdztzdHJva2Utd2lkdGg6MC4yMDkyNTMiCiAgICAgICAgICAgeD0iOTcuNzUyMTgyIgogICAgICAgICAgIHk9Ijk2Ljk2Njg5NiI+QGdtYWlsLmNvbTwvdHNwYW4+PC90ZXh0PgogICAgPC9nPgogICAgPGcKICAgICAgIGlkPSJnOTkwIgogICAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCw5LjI2MzQyMDYpIj4KICAgICAgPHRleHQKICAgICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMC4yMzc3NjYxNiwwLDAsMC4zMjEyMDA3OSwyNC41OTUyNDcsODAuMjc2MTA0KSIKICAgICAgICAgaWQ9InRleHQ5NTQiCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6NDBweDtsaW5lLWhlaWdodDoxLjI1O2ZvbnQtZmFtaWx5OidCbG9vZCBDcm93IEl0YWxpYyc7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonQmxvb2QgQ3JvdyBJdGFsaWMsICc7bGV0dGVyLXNwYWNpbmc6MHB4O3dvcmQtc3BhY2luZzowcHg7d2hpdGUtc3BhY2U6cHJlO3NoYXBlLWluc2lkZTp1cmwoI3JlY3Q5NzApIgogICAgICAgICBpbmtzY2FwZTpleHBvcnQtZmlsZW5hbWU9Ii9zcnYvc2FtYmEvY29tbW9uL1N0b3JlL0hvbHpjcmFmdHMgcmVtb3RlL3N2Zy9wcm9kdWN0cy9mcmFtZXMtdXBjLzEyOTM5ODQxNDkwOS5wbmciCiAgICAgICAgIGlua3NjYXBlOmV4cG9ydC14ZHBpPSIyODQuNDciCiAgICAgICAgIGlua3NjYXBlOmV4cG9ydC15ZHBpPSIyODQuNDciPjx0c3BhbgogICAgICAgICAgIHg9IjE2OC4xNjYwMiIKICAgICAgICAgICB5PSIxMTcuODk5NzEiCiAgICAgICAgICAgaWQ9InRzcGFuMjU4NSI+PHRzcGFuCiAgICAgICAgICAgICBzdHlsZT0iZm9udC1zaXplOjI1LjY4MTlweDtmb250LWZhbWlseTonQWx0ZW5nbGlzY2ggTUYnOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FsdGVuZ2xpc2NoIE1GJyIKICAgICAgICAgICAgIGlkPSJ0c3BhbjI1ODMiPkhvbHpDcmFmdHM8L3RzcGFuPjwvdHNwYW4+PC90ZXh0PgogICAgICA8dGV4dAogICAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgICBzdHlsZT0iZm9udC1zdHlsZTpub3JtYWw7Zm9udC12YXJpYW50Om5vcm1hbDtmb250LXdlaWdodDpub3JtYWw7Zm9udC1zdHJldGNoOm5vcm1hbDtmb250LXNpemU6Ny42MDM2OHB4O2xpbmUtaGVpZ2h0OjEuMjU7Zm9udC1mYW1pbHk6QWx0ZS1TY2h3YWJhY2hlcjstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOkFsdGUtU2Nod2FiYWNoZXI7bGV0dGVyLXNwYWNpbmc6MHB4O3dvcmQtc3BhY2luZzowcHg7c3Ryb2tlLXdpZHRoOjAuMTkwMDkzIgogICAgICAgICB4PSI2Ni4zMjc2NiIKICAgICAgICAgeT0iMTA1LjgwNTY0IgogICAgICAgICBpZD0idXBjMiIKICAgICAgICAgdHJhbnNmb3JtPSJzY2FsZSgwLjk2NjgxMTU4LDEuMDM0MzI3NykiCiAgICAgICAgIGlua3NjYXBlOmV4cG9ydC1maWxlbmFtZT0iL3Nydi9zYW1iYS9jb21tb24vU3RvcmUvSG9semNyYWZ0cyByZW1vdGUvc3ZnL3Byb2R1Y3RzL2ZyYW1lcy11cGMvMTI5Mzk4NDE0OTA5LnBuZyIKICAgICAgICAgaW5rc2NhcGU6ZXhwb3J0LXhkcGk9IjI4NC40NyIKICAgICAgICAgaW5rc2NhcGU6ZXhwb3J0LXlkcGk9IjI4NC40NyI+PHRzcGFuCiAgICAgICAgICAgaWQ9InRzcGFuOTU2IgogICAgICAgICAgIHN0eWxlPSJmb250LXN0eWxlOm5vcm1hbDtmb250LXZhcmlhbnQ6bm9ybWFsO2ZvbnQtd2VpZ2h0Om5vcm1hbDtmb250LXN0cmV0Y2g6bm9ybWFsO2ZvbnQtZmFtaWx5OkFuY29uYS1OYXJyb3c7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjpBbmNvbmEtTmFycm93O3N0cm9rZS13aWR0aDowLjE5MDA5MyIKICAgICAgICAgICB4PSI2Ni4zMjc2NiIKICAgICAgICAgICB5PSIxMDUuODA1NjQiCiAgICAgICAgICAgc29kaXBvZGk6cm9sZT0ibGluZSI+MTI5Mzk4NDE0OTA5PC90c3Bhbj48L3RleHQ+CiAgICAgIDx0ZXh0CiAgICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICAgIHN0eWxlPSJmb250LXN0eWxlOm5vcm1hbDtmb250LXZhcmlhbnQ6bm9ybWFsO2ZvbnQtd2VpZ2h0Om5vcm1hbDtmb250LXN0cmV0Y2g6bm9ybWFsO2ZvbnQtc2l6ZTo3LjE5MzIxcHg7bGluZS1oZWlnaHQ6MS4yNTtmb250LWZhbWlseTpBbmNvbmEtTmFycm93Oy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246QW5jb25hLU5hcnJvdztsZXR0ZXItc3BhY2luZzowcHg7d29yZC1zcGFjaW5nOjBweDtzdHJva2Utd2lkdGg6MC4xNzk4Mzt0ZXh0LWFuY2hvcjplbmQ7dGV4dC1hbGlnbjplbmQiCiAgICAgICAgIHg9IjEyOC45NTU2MSIKICAgICAgICAgeT0iMTIyLjM2ODA0IgogICAgICAgICBpZD0icGhvbmUyIgogICAgICAgICB0cmFuc2Zvcm09InNjYWxlKDAuOTc1NDYzNzYsMS4wMjUxNTM0KSIKICAgICAgICAgaW5rc2NhcGU6ZXhwb3J0LWZpbGVuYW1lPSIvc3J2L3NhbWJhL2NvbW1vbi9TdG9yZS9Ib2x6Y3JhZnRzIHJlbW90ZS9zdmcvcHJvZHVjdHMvZnJhbWVzLXVwYy8xMjkzOTg0MTQ5MDkucG5nIgogICAgICAgICBpbmtzY2FwZTpleHBvcnQteGRwaT0iMjg0LjQ3IgogICAgICAgICBpbmtzY2FwZTpleHBvcnQteWRwaT0iMjg0LjQ3Ij48dHNwYW4KICAgICAgICAgICBzb2RpcG9kaTpyb2xlPSJsaW5lIgogICAgICAgICAgIGlkPSJ0c3Bhbjk2MCIKICAgICAgICAgICBzdHlsZT0iZm9udC1zdHlsZTpub3JtYWw7Zm9udC12YXJpYW50Om5vcm1hbDtmb250LXdlaWdodDpub3JtYWw7Zm9udC1zdHJldGNoOm5vcm1hbDtmb250LWZhbWlseTpBbmNvbmEtTmFycm93Oy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246QW5jb25hLU5hcnJvdztzdHJva2Utd2lkdGg6MC4xNzk4Mzt0ZXh0LWFuY2hvcjplbmQ7dGV4dC1hbGlnbjplbmQiCiAgICAgICAgICAgeD0iODIuMDE5OTgxIgogICAgICAgICAgIHk9IjEyMi4zNjgwNCI+KDgwNCkgODU0LTQwNTcgKFRleHQpPC90c3Bhbj48L3RleHQ+CiAgICAgIDx0ZXh0CiAgICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICAgIHN0eWxlPSJmb250LXN0eWxlOm5vcm1hbDtmb250LXZhcmlhbnQ6bm9ybWFsO2ZvbnQtd2VpZ2h0Om5vcm1hbDtmb250LXN0cmV0Y2g6bm9ybWFsO2ZvbnQtc2l6ZTo4LjM3MDA5cHg7bGluZS1oZWlnaHQ6MS4yNTtmb250LWZhbWlseTpBbmNvbmEtTmFycm93Oy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246QW5jb25hLU5hcnJvdztsZXR0ZXItc3BhY2luZzowcHg7d29yZC1zcGFjaW5nOjBweDtzdHJva2Utd2lkdGg6MC4yMDkyNTMiCiAgICAgICAgIHg9Ijk3Ljc1MjE4MiIKICAgICAgICAgeT0iMTE3Ljc2ODkyIgogICAgICAgICBpZD0idGV4dDk2NiIKICAgICAgICAgaW5rc2NhcGU6ZXhwb3J0LWZpbGVuYW1lPSIvc3J2L3NhbWJhL2NvbW1vbi9TdG9yZS9Ib2x6Y3JhZnRzIHJlbW90ZS9zdmcvcHJvZHVjdHMvZnJhbWVzLXVwYy8xMjkzOTg0MTQ5MDkucG5nIgogICAgICAgICBpbmtzY2FwZTpleHBvcnQteGRwaT0iMjg0LjQ3IgogICAgICAgICBpbmtzY2FwZTpleHBvcnQteWRwaT0iMjg0LjQ3Ij48dHNwYW4KICAgICAgICAgICBzb2RpcG9kaTpyb2xlPSJsaW5lIgogICAgICAgICAgIGlkPSJ0c3Bhbjk2NCIKICAgICAgICAgICBzdHlsZT0iZm9udC1zdHlsZTpub3JtYWw7Zm9udC12YXJpYW50Om5vcm1hbDtmb250LXdlaWdodDpub3JtYWw7Zm9udC1zdHJldGNoOm5vcm1hbDtmb250LWZhbWlseTpBbmNvbmEtTmFycm93Oy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246QW5jb25hLU5hcnJvdztzdHJva2Utd2lkdGg6MC4yMDkyNTMiCiAgICAgICAgICAgeD0iOTcuNzUyMTgyIgogICAgICAgICAgIHk9IjExNy43Njg5MiI+QGdtYWlsLmNvbTwvdHNwYW4+PC90ZXh0PgogICAgPC9nPgogIDwvZz4KPC9zdmc+Cg=='''
	    phone_number='(804) 854-4057'
	    upc='123456789012'
	    filename="upc_template.svg"
	    outfile='test.svg'
	    parsed=None
	    #editable_conditions=['tspan1042','tspan20558','span20566','tspan24369','tspan1046','tspan956','tspan960','tspan964']
	    condition_upc=['upc1','upc2']
	    condition_phone=['phone1','phone2']
	    def __init__(self,upc=None,phone_number=None,outfile_name=None,filename=None,debug=False):
	        if upc:
	            self.upc=upc
	        if phone_number:
	            self.phone_number=phone_number
	        if outfile_name:
	            self.outfile=outfile_name
	        if filename:
	            self.filename=filename
	        self.read(debug)
	        self.replace()
	        self.writer()
	    def read(self,debug):
	        if debug:
	            with open(Path(self.filename),"r") as file:
	                self.parsed=etree.parse(file)
	        else:
	            self.parsed=etree.parse(BytesIO(base64.b64decode(self.svgdata.encode())))
	
	
	    def replace(self):
	        if self.parsed:
	            for i in self.parsed.iter():
	                #print(i.findall('/'))
	                if i.attrib['id'] in self.condition_upc:
	                    #print(i.attrib,i.text)
	                    for i in i.iter():
	                        if i.tag == "{http://www.w3.org/2000/svg}tspan":
	                            i.text=self.upc                           
	            for i in self.parsed.iter():
	                if i.attrib['id'] in self.condition_phone:
	                    for i in i.iter():
	                        if i.tag == "{http://www.w3.org/2000/svg}tspan":
	                            i.text=self.phone_number                           
	
	
	    def writer(self):
	        self.parsed.write(self.outfile)
	if __name__ == "__main__":
	    Modify()
	import os,sys,json,csv,pyqrcode
	from pyzbar import pyzbar as zbar
	import barcode
	from pathlib import Path
	import bz2,zlib,gzip
	
	class File2QR:
	    outfile="{chunk}.{ext}"
	    infile="drawing.svg"
	    '''
	    first byte of each qrcode is compression algorithm
	    b=bz2
	    z=zlib
	    g=gzip
	    bytes 2-12 of each qrcode is the order number
	    '''
	    chunk_digits=10
	    bz2=None
	    zlib=None
	    gzip=None
	    chunks={}
	    qr_chunks={}
	    in_mem=False
	    def __init__(self,*args,**kwargs):
	        if 'infile' in kwargs.keys():
	            self.infile=kwargs.get('infile')
	        if 'outfile' in kwargs.keys():
	            self.outfile=kwargs.get('outfile')
	        if 'in_mem' in kwargs.keys():
	            self.in_mem=kwargs.get('in_mem')
	
	        data=b''
	        with open(self.infile,'rb') as ifile:
	            data=ifile.read()
	        self.bz2=bz2.compress(data,compresslevel=9)
	        self.gzip=gzip.compress(data,compresslevel=9)
	        self.zlib=zlib.compress(data,level=9)
	        smallest_key=''
	        for num,i in enumerate(['bz2','zlib','gzip']):
	            print(i,len(self.__dict__[i]))
	            if num == 0:
	                last_size=len(self.__dict__[i])
	                smallest_key=i
	            else:
	                if len(self.__dict__[i]) < len(self.__dict__[smallest_key]):
	                    smallest_key=i
	        with open(self.infile,'rb') as ifile:
	            count=0
	            while True:
	                data=ifile.read(2048)
	                if not data:
	                    break
	                self.chunks['{compress}_{num}'.format(compress=smallest_key,num=count)]=smallest_key[0].encode()+'{num}'.format(num=count).zfill(self.chunk_digits).encode()+bz2.compress(data,compresslevel=9)
	                print(count)
	                count+=1        
	        for num,key in enumerate(self.chunks.keys()):
	            print(key)
	            self.qr_chunks[key]=pyqrcode.QRCode(self.chunks[key])
	        #qr=pyqrcode.QRCode(self.__dict__[smallest_key])
	        if not self.in_mem:
	            for num,key in enumerate(self.qr_chunks.keys()):
	                if not Path("OUT").exists():
	                    Path("OUT").mkdir()
	                self.qr_chunks[key].png(str(Path("OUT")/Path(self.outfile.format(chunk=key,ext='png'))),scale=4)
	'''            
	if __name__ == "__main__":
	    File2QR(in_mem=True)
	'''

class Signals(QObject):
    error=pyqtSignal(tuple)
    result=pyqtSignal(object)
    finished=pyqtSignal()
    stop=pyqtSignal()
    update=pyqtSignal(object)

class File2QRWorker(QRunnable):
    def __init__(self,*args,**kwargs):
        super(File2QRWorker,self).__init__()
        self.args=args
        self.kwargs=kwargs
        self.signals=Signals()
        self.running=True
        self.destination=self.kwargs.get('destination')
        self.source=self.kwargs.get('source')
        self.progress=self.kwargs.get('progress')

    def read_source(self):
        if not Path(self.destination).exists():
            Path(self.destination).mkdir()
        size=os.stat(self.source).st_size
        self.signals.result.emit("updating progress size to {}\n".format(size))
        self.progress.setMaximum(size)
        with open(self.source,'rb') as src:
            counter=0
            while True:
                told=src.tell()
                chunk=src.read(2048)
                if not chunk:
                    break
                counter+=1
                self.signals.result.emit("Compressing Chunk\n")
                compress=lzma.compress(chunk)
                self.signals.result.emit("Base64 Encoding Chunk {}\n".format(told))
                b64=base64.b64encode(compress)
                self.signals.result.emit("encoding chunk in JSON")
                JSON={'chunk_data':b64.decode('utf-8'),'chunk_number':counter}
                JSON=json.dumps(JSON)
                self.signals.update.emit(told)
                name="{destination}/{src}{counter}.svg".format(destination=self.destination,src=Path(self.source).name,counter=counter)
                self.signals.result.emit("Creating QR Code Chunk as {name}\n".format(name=name))
                print(len(JSON),JSON)
                qr=pyqrcode.QRCode(JSON,version=40,error='L')
                qr.svg(name)
        self.signals.result.emit("compressing desintation directory to file\n")
        if not Path("tmp").exists():
            Path("tmp").mkdir()
        output_name=Path("./tmp")/Path(self.source+".qr.tar.xz").name
        self.signals.result.emit("creating tarfile called {}\n".format(output_name))
        with open(output_name,mode="wb") as fob:
            with tarfile.TarFile(fileobj=fob,mode='w') as tar:
                for file in Path(self.destination).iterdir():
                    tar.add(file)
        self.signals.result.emit("deleting src qr directory {}\n".format(self.destination))
        shutil.rmtree(self.destination)
        self.signals.result.emit("moving tmp to {}\n".format(self.destination))
        Path("./tmp").rename(self.destination)
        self.signals.result.emit("updating progress size to 100\n")

    @pyqtSlot()
    def STOP(self):
        self.running=False
    @pyqtSlot()
    def run(self):
        if self.source == '':
            message="{time} [ERROR] there is no source file!\n".format(time=datetime.now().ctime())
            self.signals.result.emit(message)
        else:
            #result for plaintext viewer
            #update for progress bar
            self.signals.result.emit("starting\n")
            self.signals.update.emit(1)
            self.read_source()


            self.signals.update.emit(100)
            self.signals.result.emit("done!\n")
            self.signals.finished.emit()
class QR2FileWorker(QRunnable):
    def __init__(self,*args,**kwargs):
        super(QR2FileWorker,self).__init__()
        self.args=args
        self.kwargs=kwargs
        self.signals=Signals()
        self.running=True
        self.destination=self.kwargs.get('destination')
        self.source=self.kwargs.get('source')
        self.progress=self.kwargs.get('progress')
    @pyqtSlot()
    def STOP(self):
        self.running=False
    source_data=[]
    def read_tar(self):
        tarball=tarfile.open(self.source,mode='r')
        members=tarball.getmembers()
        size=len(members)
        self.signals.result.emit("updating progress size to {}\n".format(size))
        self.progress.setMaximum(size)
        for member in members:
            try:
                print(Path(member.name).suffix)
                if Path(member.name).suffix == '.svg':
                    self.signals.result.emit("extracting member {}".format(member.name))
                    fileobj=tarball.extractfile(member)
                    self.signals.result.emit("reading member {}".format(member.name))
                    data=fileobj.read()
                    self.signals.result.emit("converting member to '{}' svg and saving to 'tmp.png'".format(member.name))
                    svg2png(bytestring=data,write_to="tmp.png",scale=10)

                    self.signals.result.emit("opening with PIL {}".format(member.name))
                    img=Image.open("tmp.png")
                    self.signals.result.emit("opening background {}".format(member.name))
                    img_new=Image.new(size=img.size,mode="RGB",color="WHITE")
                    self.signals.result.emit("pasting on background {}".format(member.name))
                    img_new.paste(img,(0,0),img)
                    self.signals.result.emit("converting RGBA to RGB {}".format(member.name))
                    img_new.convert("RGB")
                    self.signals.result.emit("saving to tmp.png {}".format(member.name))
                    img_new.save("tmp.png")

                    print(img)
                    self.signals.result.emit("decoding QRCODE")
                    a=zbar.decode(img_new)

                    jsonData=json.loads(a[0].data.decode())

                    jsonData['chunk_data']=base64.b64decode(jsonData['chunk_data'])

                    self.source_data.append(jsonData)


                    fileobj.close()
                    try:
                        Path("tmp.png").unlink()
                    except Exception as e:
                        print(e)
                    self.signals.result.emit("closing tarball {}".format(tarball.name))
            except Exception as e:
                print(e,member.name,'ERROR >>>')
                raise e
                break
            self.progress.setValue(self.progress.value()+1)
        #begin decompress
        self.signals.result.emit("handling decoded data")
        ordered=[None for i in range(len(self.source_data))]
        for chunk in self.source_data:
            print(int(chunk.get('chunk_number'))-1)
            ordered[int(chunk.get('chunk_number'))-1]=chunk.get('chunk_data')
        #print(ordered)
        if self.destination == '':
            self.destination=self.source.replace(".qr.tar.xz","")

        with open(self.destination,'wb') as OF:
            for member in ordered:
                #decompress
                data=lzma.decompress(member)
                OF.write(data)
        tarball.close()
        self.signals.result.emit("done!")
        self.signals.result.emit("updating progress size to {}\n".format(100))
        self.progress.setMaximum(100)

    @pyqtSlot()
    def run(self):
        if self.source == '':
            message="{time} [ERROR] there is no source file!\n".format(time=datetime.now().ctime())
            self.signals.result.emit(message)
        else:
            #result for plaintext viewer
            #update for progress bar
            self.signals.result.emit("starting\n")
            self.signals.update.emit(1)
            self.read_tar()


            self.signals.update.emit(0)
            self.signals.result.emit("done!\n")
            self.signals.finished.emit()

class PollingWorker(QRunnable):
    '''worker thread'''
    def __init__(self,*args,**kwargs):
        super(PollingWorker,self).__init__()
        self.args=args
        self.kwargs=kwargs
        self.running=True
        self.signals=Signals()

    @pyqtSlot()
    def STOP(self):
        self.running=False

    @pyqtSlot()
    def run(self):
        self.signals.result.emit({})
        self.signals.update.emit('')
        self.signals.result.emit('')
class Window(QMainWindow,QWidget):
    version="HCA5"
    def download_engraving_zip(self):
        if self.file_engraving_zip.get("file"):
            filename,extension=QFileDialog.getSaveFileName()
            print(self.file_engraving_zip,filename,extension)
            if filename != '':
                with open('tmpfile','wb') as tmpfile:
                    bitted=base64.b64decode(self.file_engraving_zip.get('file').encode())
                    tmpfile.write(bitted)
                    self.files2qr_worker=File2QRWorker(progress=self.window_2.files2qr_progress,destination=filename,source='tmpfile')
                    self.files2qr_worker.signals.result.connect(self.update_files2qr_stage_viewer)
                    self.files2qr_worker.signals.update.connect(self.update_files2qr_progress)
                    self.files2qr_worker.run()
        else:
            QMessageBox.warning(None,"No File","No File {}".format("engraving_zip"))

    def download_rear(self):
        if self.file_rear.get("file"):
            filename,extension=QFileDialog.getSaveFileName()
            print(self.file_rear,filename,extension)
            if filename != '':
                with open('tmpfile','wb') as tmpfile:
                    bitted=base64.b64decode(self.file_rear.get('file').encode())
                    tmpfile.write(bitted)
                    self.files2qr_worker=File2QRWorker(progress=self.window_2.files2qr_progress,destination=filename,source='tmpfile')
                    self.files2qr_worker.signals.result.connect(self.update_files2qr_stage_viewer)
                    self.files2qr_worker.signals.update.connect(self.update_files2qr_progress)
                    self.files2qr_worker.run()
        else:
            QMessageBox.warning(None,"No File","No File {}".format("rear"))

    def download_front(self):
        if self.file_front.get("file"):
            filename,extension=QFileDialog.getSaveFileName()
            print(self.file_front,filename,extension)
            if filename != '':
                with open('tmpfile','wb') as tmpfile:
                    bitted=base64.b64decode(self.file_front.get('file').encode())
                    tmpfile.write(bitted)
                    self.files2qr_worker=File2QRWorker(progress=self.window_2.files2qr_progress,destination=filename,source='tmpfile')
                    self.files2qr_worker.signals.result.connect(self.update_files2qr_stage_viewer)
                    self.files2qr_worker.signals.update.connect(self.update_files2qr_progress)
                    self.files2qr_worker.run()
        else:
            QMessageBox.warning(None,"No File","No File {}".format("front"))

    def download_corner(self):
        if self.file_corner.get("file"):
            filename,extension=QFileDialog.getSaveFileName()
            if filename != '':
                print(self.file_corner,filename,extension)
                with open('tmpfile','wb') as tmpfile:
                    bitted=base64.b64decode(self.file_corner.get('file').encode())
                    tmpfile.write(bitted)
                    self.files2qr_worker=File2QRWorker(progress=self.window_2.files2qr_progress,destination=filename,source='tmpfile')
                    self.files2qr_worker.signals.result.connect(self.update_files2qr_stage_viewer)
                    self.files2qr_worker.signals.update.connect(self.update_files2qr_progress)
                    self.files2qr_worker.run()
        else:
            QMessageBox.warning(None,"No File","No File {}".format("corner"))

    def update_files2qr_stage_viewer(self,text):
        self.window_2.files2qr_stage_viewer.setPlainText(self.window_2.files2qr_stage_viewer.toPlainText()+text)
    def update_files2qr_progress(self,value):
        self.window_2.files2qr_progress.setValue(value)
    #start QR2file start
    def qr2file_start(self):
        self.qr2file_worker=QR2FileWorker(source=self.window.qr2file_source.text(),destination=self.window.qr2file_destination.text(),progress=self.window.qr2file_progress)
        self.qr2file_worker.signals.result.connect(lambda text:self.window.qr2file_stage_viewer.setPlainText(self.window.qr2file_stage_viewer.toPlainText()+text))
        self.qr2file_worker.signals.update.connect(lambda x:self.window.qr2file_progress.setValue(int(x)))
        self.qr2file_worker.signals.finished.connect(lambda :self.window.qr2file_stage_viewer.setPlainText(''))
        self.qr2file_worker.run()
        del(self.qr2file_worker)
    def qr2file_source_browse(self):
        filters="QR Package (*.qr.tar.xz);;All Files(*)"
        save_file,extension=QFileDialog.getOpenFileName(filter=filters)
        if save_file != '':
            self.window.qr2file_source.setText(save_file)
    def qr2file_destination_browse(self):
        save_file=QFileDialog.getSaveFileName(filter="All Files(*)")
        print(save_file)
        if save_file[0] != "":
            self.window.qr2file_destination.setText(save_file)
        #end QR2file end
    #start file2qr tab
    def setup_file2qr_worker(self):
        self.file2qr_worker=File2QRWorker(source=self.window.file2qr_source.text(),destination=self.window.file2qr_destination.text(),progress=self.window.file2qr_progress)
        self.file2qr_worker.signals.result.connect(lambda text:self.window.file2qr_stage_viewer.setPlainText(self.window.file2qr_stage_viewer.toPlainText()+text))
        self.file2qr_worker.signals.update.connect(lambda x:self.window.file2qr_progress.setValue(int(x)))
        self.file2qr_worker.signals.finished.connect(self.file2qr_reset)
        self.file2qr_worker.run()
        del(self.file2qr_worker)
    def file2qr_reset(self):
        self.window.file2qr_stage_viewer.setPlainText('')
        self.window.file2qr_progress.setValue(0)
        self.window.file2qr_source.setText('')
        self.window.file2qr_destination.setText("./qrs")
    def file2qr_source_browse(self):
        ext=['*']
        filters=';;'.join(['{e} Files(*.{e})'.format(e=i) for i in ext])
        save_file,extension=QFileDialog.getOpenFileName(filter=filters)
        if save_file != '':
            self.window.file2qr_source.setText(save_file)
    def file2qr_destination_browse(self):
        save_file=QFileDialog.getExistingDirectory()
        print(save_file)
        if save_file != "":
            self.window.file2qr_destination.setText(save_file)
    #end file2qrtab
    #file is for test file mode
    def test_content(self,file=None):
        codeIO=StringIO()
        format=self.window.formatEditor_contentFormat.currentText()
        print("using {}".format(format))
        if format == 'CSV':
            try:
                writer=csv.writer(codeIO,delimiter=',')
                if file == None:
                    writer.writerows([i.split(",") for i in self.window.formatEditor_editor.toPlainText().splitlines()])
                    codeIO.seek(0)
                    return codeIO,'CSV'
                else:
                    data=[i.split(',') for i in file.read().splitlines()]
                    self.window.statusBar().showMessage("all good")
            except Exception as e:
                print(str(e))
                self.window.statusBar().showMessage(str(e))
        elif format == 'JSON':
            try:
                if file == None:
                    writer=json.loads(self.window.formatEditor_editor.toPlainText())
                    return writer,'JSON'
                else:
                    result=json.load(file)
                    self.window.statusBar().showMessage("all good")
            except Exception as e:
                print(e)
                self.window.statusBar().showMessage(str(e))
        elif format == "PNG":
            try:
                img=Image.new('RGB',(800,600),(255, 255, 255))
                data=ImageDraw.Draw(img)
                if file == None:
                    if self.window.formatEditor_pngOptions.currentText() == "Plain":
                        size=data.textsize(self.window.formatEditor_editor.toPlainText())
                        data.text(size,self.window.formatEditor_editor.toPlainText(),(0,0,0))
                    elif self.window.formatEditor_pngOptions.currentText() == "QR":
                        img=pyqrcode.QRCode(self.window.formatEditor_editor.toPlainText())
                        img.png(self.window.formatEditor_saveLocation.text(),scale=4)
                        return
                    elif self.window.formatEditor_pngOptions.currentText() == "Code128":
                        img=Code128(self.window.formatEditor_editor.toPlainText(),writer=WRITER.ImageWriter()).save(Path(self.window.formatEditor_saveLocation.text()).stem)
                        return
                    return img,'PNG'
                else:
                    print(file)
                    image=Image.open(file)
                    self.window.statusBar().showMessage("all good")
            except Exception as e:
                print(e)
                self.window.statusBar().showMessage(str(e))
        elif format == "*":
            with open(self.window.formatEditor_saveLocation.text(),"r") as x:
                self.window.formatEditor_editor.setPlainText(x.read())
        else:
            print("invalid format")
            raise Exception("Invalid Format")
    def random_data(self):
        self.window.formatEditor_editor.setPlainText(base64.b64encode(os.urandom(self.window.formatEditor_rdSize.value())).decode('utf-8'))
    def test_content_content(self):
        obj=self.test_content()
        print(obj)
    def formatEditor_browse(self):

        AllItems = [self.window.formatEditor_contentFormat.itemText(i) for i in range(self.window.formatEditor_contentFormat.count())]
        print(AllItems)
        index=0
        for num,i in enumerate(AllItems):
            if i == self.window.formatEditor_contentFormat.currentText():
                index=num
                break
        filters=[]
        filters.append('{x} Files(*.{x})'.format(x=AllItems.pop(index)))
        for i in AllItems:
            filters.append('{x} Files(*.{x})'.format(x=i))
        filters=';;'.join(filters)
        print(filters)
        "CSV Files(*.CSV);;JSON Files(*.JSON);;PNG Files(*.PNG)"
        save_file,extension=QFileDialog.getSaveFileName(filter=filters)
        print(save_file,extension)
        def run_exporter(filename,mode):
            print(filename,mode)
            if filename != '':
                if mode == "JSON Files(*.JSON)":
                    self.window.formatEditor_saveLocation.setText(Path(filename).stem+".json")
                elif mode == "CSV Files(*.CSV)":
                    self.window.formatEditor_saveLocation.setText(Path(filename).stem+".csv")
                elif mode == "PNG Files(*.PNG)":
                    self.window.formatEditor_saveLocation.setText(Path(filename).stem+".png")
                else:
                    self.window.formatEditor_saveLocation.setText(str(Path(filename)))




        run_exporter(save_file,extension)
    def formatEditor_delete(self):
        try:
            Path(self.window.formatEditor_saveLocation.text()).unlink()
            self.window.statusBar().showMessage("successfully deleted -> {}".format(self.window.formatEditor_saveLocation.text()))
        except Exception as e:
            self.window.statusBar().showMessage(str(e))
            print(e)
    def formatEditor_save(self):
        try:
            eo=self.test_content()
        except Exception as e:
            print(e)
            eo=[self.window.formatEditor_editor.toPlainText(),self.window.formatEditor_contentFormat.currentText()]

        if eo == None:
            self.window.statusBar().showMessage("nothing to save")
            return
        content,mode=eo
        if mode == 'PNG':
            try:
                content.save(self.window.formatEditor_saveLocation.text())
                self.window.statusBar().showMessage("saved successfully {}".format(self.window.formatEditor_saveLocation.text()))
                print("save successfull {}".format(self.window.formatEditor_saveLocation.text()))
            except Exception as e:
                print(e)
                self.window.statusBar().showMessage(str(e))
        elif mode == 'CSV':
            try:
                with open(self.window.formatEditor_saveLocation.text(),'w') as out:
                    out.write(content.read())
                self.window.statusBar().showMessage("saved successfully {}".format(self.window.formatEditor_saveLocation.text()))
                print("save successfull {}".format(self.window.formatEditor_saveLocation.text()))
            except Exception as e:
                print(e)
                self.window.statusBar().showMessage(str(e))
        elif mode == 'JSON':
            try:
                with open(self.window.formatEditor_saveLocation.text(),'w') as out:
                    json.dump(content,out)
                self.window.statusBar().showMessage("saved successfully {}".format(self.window.formatEditor_saveLocation.text()))
                print("save successfull {}".format(self.window.formatEditor_saveLocation.text()))
            except Exception as e:
                print(e)
                self.window.statusBar().showMessage(str(e))
        elif mode == '*':
            try:
                with open(self.window.formatEditor_saveLocation.text(),'w') as out:
                    out.write(self.window.formatEditor_editor.toPlainText())
                self.window.statusBar().showMessage("saved successfully {}".format(self.window.formatEditor_saveLocation.text()))
                print("save successfull {}".format(self.window.formatEditor_saveLocation.text()))
            except Exception as e:
                print(e)
                self.window.statusBar().showMessage(str(e))
    #ocr tab start
    def process_image(self,image_file):
        text=''
        try:
            with open(image_file,'rb') as file:
                text=pytesseract.image_to_string(Image.open(file))
            return text
        except Exception as e:
            print(e)
            self.window.statusBar().showMessage(str(e))
    def ocr_browse_open(self,button):
        ext=['PNG','JPG','JPEG']
        filters=';;'.join(['{e} Files(*.{e})'.format(e=i) for i in ext])
        save_file,extension=QFileDialog.getOpenFileName(filter=filters)
        print(save_file,extension)
        def run_exporter(filename,mode):
            print(filename,mode)
            if filename != '':
                if mode == "JPG Files(*.JPG)":
                    self.window.ocr_location.setText(Path(filename).name)
                elif mode == "JPEG Files(*.JPEG)":
                    self.window.ocr_location.setText(Path(filename).name)
                elif mode == "PNG Files(*.PNG)":
                    self.window.ocr_location.setText(Path(filename).name)
                elif mode == "TXT Files(*.TXT)":
                    self.window.ocr_saveLocation.setText(Path(filename).stem+".txt")
        run_exporter(save_file,extension)
    def ocr_browse_save(self,button):
        ext=['TXT',]
        filters=';;'.join(['{e} Files(*.{e})'.format(e=i) for i in ext])
        save_file,extension=QFileDialog.getSaveFileName(filter=filters)
        print(save_file,extension)
        def run_exporter(filename,mode):
            print(filename,mode)
            if filename != '':
                if mode == "JPG Files(*.JPG)":
                    self.window.ocr_saveLocation.setText(Path(filename).stem+".jpg")
                elif mode == "JPEG Files(*.JPEG)":
                    self.window.ocr_saveLocation.setText(Path(filename).stem+".jpeg")
                elif mode == "PNG Files(*.PNG)":
                    self.window.ocr_saveLocation.setText(Path(filename).stem+".png")
                elif mode == "TXT Files(*.TXT)":
                    self.window.ocr_saveLocation.setText(Path(filename).stem+".txt")
        run_exporter(save_file,extension)
    def ocr_save(self,button):
        try:
            with open(self.window.ocr_saveLocation.text(),"w") as out:
                out.write(self.window.ocr_editor.toPlainText())
        except Exception as e:
            print(e)
            self.window.statusBar().showMessage(str(e))
    def ocr_process(self,button):
        try:
            text=self.process_image(self.window.ocr_location.text())
            self.window.ocr_editor.setPlainText(text)

            self.ocr_img=Image.open(self.window.ocr_location.text())
            self.ocr_qim=ImageQt(self.ocr_img)
            self.ocr_pix.setPixmap(QPixmap.fromImage(self.ocr_qim))
            #self.ocr_scene=QGraphicsScene()
            #self.ocr_scene.addPixmap(self.ocr_pix)
            #view=self.window.ocr_imageView
            #view.setScene(self.ocr_scene)
        except Exception as e:
            print(e)
            self.window.statusBar().showMessage(str(e))
            self.ocr_img=Image.new(size=(580,580),mode='RGBA',color=(255,0,0))
            self.ocr_qim=ImageQt(self.ocr_img)
            self.ocr_pix.setPixmap(QPixmap.fromImage(self.ocr_qim))
    #ocr tab end
    #import tab start
    def import_location_browse(self,button):
        AllItems = [self.window.import_format.itemText(i) for i in range(self.window.import_format.count())]
        print(AllItems)
        index=0
        for num,i in enumerate(AllItems):
            if i == self.window.import_format.currentText():
                index=num
                break
        filters=[]
        x=AllItems.pop(index)
        if x in ['QR','Code128']:
            x='PNG'
        filters.append('{x} Files(*.{x})'.format(x=x))
        for i in AllItems:
            if i in ['Code128','QR']:
                pass
            else:
                filters.append('{x} Files(*.{x})'.format(x=i))
        filters=';;'.join(filters)
        print(filters)
        "CSV Files(*.CSV);;JSON Files(*.JSON);;PNG Files(*.PNG)"
        save_file,extension=QFileDialog.getOpenFileName(filter=filters)
        print(save_file,extension)
        def run_exporter(filename,mode):
            print(filename,mode)
            if filename != '':
                if mode == "JSON Files(*.JSON)":
                    self.window.import_location.setText(Path(filename).stem+".json")
                elif mode == "CSV Files(*.CSV)":
                    self.window.import_location.setText(Path(filename).stem+".csv")
                elif mode == "Code128 Files(*.Code128)":
                    self.window.import_location.setText(Path(filename).stem+".Code128")
                elif mode == "QR Files(*.QR)":
                    self.window.import_location.setText(Path(filename).stem+".QR")
                elif mode == "PNG Files(*.PNG)":
                    self.window.import_location.setText(Path(filename).stem+".png")
        run_exporter(save_file,extension)
    def import_readfile(self,button):
        mode=self.window.import_format.currentText()
        def run_reader(filename,mode):
            self.import_data=dict()
            print(filename,mode)
            if filename != '':
                if mode == "JSON":
                    if self.window.dontParse.isChecked():
                        with open(filename,"rb") as file:
                            self.window.import_viewer.setPlainText(str(file.read()))
                    else:
                        with open(filename,"r") as file:
                            self.import_data=json.load(file)
                        self.window.import_viewer.setPlainText(str(self.import_data))
                elif mode == "CSV":
                    if self.window.dontParse.isChecked():
                        with open(filename,"rb") as file:
                            self.window.import_viewer.setPlainText(str(file.read()))
                    else:
                        with open(filename,"r") as file:
                            reader=csv.reader(file,delimiter=',')
                            headers=[]
                            values=[]
                            for num,row in enumerate(reader):
                                if num == 0:
                                    headers=row
                                elif num == 1:
                                    values=row
                            self.import_data=dict(zip(headers,values))
                            print(self.import_data)

                            self.window.import_viewer.setPlainText(str(self.import_data))
                elif mode in ["Code128",'QR']:
                    img=Image.open(filename)
                    if self.window.dontParse.isChecked():
                        self.window.import_viewer.setPlainText(str(zbar.decode(img)[0].data))
                    else:
                        self.import_data=evaluate(zbar.decode(img)[0].data.decode('utf-8'))
                        self.window.import_viewer.setPlainText(str(self.import_data))
                else:
                    raise Exception("Invalid Reader")
        try:
            run_reader(self.window.import_location.text(),mode)
            if not self.window.dontParse.isChecked():
                self.validate_product(self.import_data)
        except Exception as e:
            print(e)
            self.window.statusBar().showMessage(str(e))
    #part of import tab
    def make_product(self):
        try:
            self.import_data=evaluate(self.window.import_viewer.toPlainText())
        except Exception as e:
            raise e
        product=dict()
        for i in HolzCraftsFrameEnum.__fields__(HolzCraftsFrameEnum):
            if i not in ['front','corner','front','rear','engraving_zip']:
                product[i]=self.import_data.get(i)
        address=self.window.server.text()+'/holzcraftsframes/new_frame/'
        token=self.window.token.text()
        response=requests.post(address,data=product,headers={'Authorization':'Token {}'.format(token)})
        if response.status_code == 200:
            self.window.statusBar().showMessage("Save Successfull!")
        else:
            self.window.statusBar().showMessage(str(response))
        print(response)
    def validate_product(self,product_dict):
        result=True
        for i in self.import_data.keys():
            try:
                HolzCraftsFrameEnum.__dict__[i]
            except Exception as e:
                raise Exception("Invalid Product")
        for i in HolzCraftsFrameEnum.__fields__(HolzCraftsFrameEnum):
            try:
                print(i,'key')
                print(product_dict[i],'data')
            except Exception as e:
                print(str(e))
                raise Exception("Invalid Product")
        if result == True:
            return
        else:
            raise Exception("Invalid Product")
    #import tab end
    def test_file_content(self):
        try:
            if self.window.formatEditor_contentFormat.currentText() != 'PNG':
                with open(self.window.formatEditor_saveLocation.text(),'r') as file:
                    self.test_content(file=file)
            else:
                self.test_content(file=self.window.formatEditor_saveLocation.text())
        except Exception as e:
            print(e)
            self.window.statusBar().showMessage(str(e))
    @pyqtSlot()
    def stop_thread(self):
        print('stop thread')
        self.worker.signals.stop.emit()(255, 255, 255)
    @pyqtSlot()
    def stop(self,worker):
        worker.running=False
    def update_results_values(self,rs):
        print(rs)
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
    def setup_external_worker(self):
        self.worker=PollingWorker()
        self.worker.signals.result.connect(self.update_results_values)
        self.worker.signals.update.connect(self.window.statusBar().showMessage)
    def aboutMe(self,x):
        print('About run()')
        msgBox = QMessageBox()
        #msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("""
        HolcraftsAdminQt6 {version} for managing Holzcrafts.
        """.format(version=self.version))
        msgBox.setWindowTitle("Home2Bar About")
        returnValue = msgBox.exec()
    def engraving_zip(self):
        import_file=QFileDialog.getOpenFileName(filter="ZIP Files (*.zip);;Tar Files (*.tar);; XZ Files(*.xz);;GZ Files(*.gz);;All Files(*)")
        print(import_file)
        if import_file[0]:
            self.window.engraving_zip.setText(import_file[0])
    def front(self):
        import_file=QFileDialog.getOpenFileName(filter="PNG Files (*.png *.PNG);;JPG Files (*.jpg *.jpeg *.JPG *.JPEG);;All Files(*)")
        print(import_file)
        if import_file[0]:
            self.window.front.setText(import_file[0])
    def corner(self):
        import_file=QFileDialog.getOpenFileName(filter="PNG Files (*.png *.PNG);;JPG Files (*.jpg *.jpeg *.JPG *.JPEG);;All Files(*)")
        print(import_file)
        if import_file[0]:
            self.window.corner.setText(import_file[0])
    def rear(self):
        import_file=QFileDialog.getOpenFileName(filter="PNG Files (*.png *.PNG);;JPG Files (*.jpg *.jpeg *.JPG *.JPEG);;All Files(*)")
        print(import_file)
        if import_file[0]:
            self.window.rear.setText(import_file[0])
    def refresh_sku(self):
        self.window.statusBar().showMessage("refreshing sku!")
        self.window.sku.setText(self.generate_sku())
    def saveOnServer(self):
        JSON=dict(
        product_type=self.window.product_type.currentText(),
        size=self.window.size.currentText(),
        can_hold_glass=self.window.can_hold_glass.currentText(),
        has_glass=self.window.has_glass.currentText(),
        can_hold_canvas=self.window.can_hold_glass.currentText(),
        has_canvas=self.window.has_canvas.currentText(),
        orientation=self.window.orientation.currentText(),
        wood_type=self.window.wood_type.currentText(),
        frame_shape=self.window.frame_shape.currentText(),
        stainable=self.window.stainable.currentText(),
        stackable=self.window.stackable.currentText(),
        finish_type=self.window.finish_type.currentText(),
        center_outer_profile=self.window.center_outer_profile.currentText(),
        sold=self.window.sold.currentText(),
        center_inner_profile=self.window.center_inner_profile.currentText(),
        rear_inner_profile=self.window.rear_inner_profile.currentText(),
        front_inner_profile=self.window.front_inner_profile.currentText(),
        front_outer_profile=self.window.front_outer_profile.currentText(),
        comments=self.window.comments.toPlainText(),
        custom_engraved=self.window.custom_engraved.currentText(),
        engraving_zip=self.window.engraving_zip.text(),
        rear=self.window.rear.text(),
        corner=self.window.corner.text(),
        front=self.window.front.text(),
        item_weight=self.window.item_weight.value(),
        item_weight_unit=self.window.item_weight_unit.currentText(),
        price=self.window.price.value(),
        other_frame_size_diameter=self.window.other_frame_size_diameter.value(),
        other_frame_size_diameter_unit=self.window.other_frame_size_diameter_unit.currentText(),
        stain=self.window.stain.text(),
        sold_to=self.window.sold_to.text(),
        sku=self.window.sku.text(),
        paid_for=self.window.paid_for.currentText(),
        amount_paid=self.window.amount_paid.value(),
        )
        print(JSON)
        files={
            'rear':JSON['rear'],
            'corner':JSON['corner'],
            'front':JSON['front'],
            'engraving_zip':JSON['engraving_zip']
        }
        counter=0
        sendFile={}
        for key in files.keys():
            if files[key]:
                print(files[key])
                try:
                    sendFile[key]=open(files[key],'rb')
                except Exception as e:
                    self.statusBar().showMessage(str(e)+":"+files[key])

        #token='1cd0130cc8870ddc77abd1b08df634c2ba46ea01'
        #address='http://127.0.0.1:8000/holzcraftsframes/new_frame/'
        address=self.window.server.text()+'/holzcraftsframes/new_frame/'
        token=self.window.token.text()
        if len(sendFile) > 0:
            response=requests.post(address,files=sendFile,data=JSON,headers={'Authorization':'Token {}'.format(token)})
        else:
            response=requests.post(address,data=JSON,headers={'Authorization':'Token {}'.format(token)})
        print(response)
        self.window.statusBar().showMessage(str(response))
        if self.window.reset_when_done.isChecked():
            self.window.comments.setPlainText('')
            self.window.engraving_zip.setText('')
            self.window.rear.setText('')
            self.window.corner.setText('')
            self.window.front.setText('')
            self.window.price.setValue(0)
            self.window.other_frame_size_diameter.setValue(0)
            self.window.item_weight.setValue(0)
            self.window.stain.setText('')
            self.window.sold_to.setText('')
            self.window.statusBar().showMessage("reset when done completed!")
        if self.window.new_sku_when_done.isChecked():
            self.refresh_sku()
            self.window.statusBar().showMessage("refreh_sku()")
        self.window.statusBar().showMessage(str(response)+str(response.json()))
    def setup_buttons(self):
        self.window.browse_engraving_zip.clicked.connect(self.engraving_zip)
        '''self.window.browse_#munge#.clicked.connect(self.#munge#)'''
        self.window.browse_front.clicked.connect(self.front)
        self.window.browse_rear.clicked.connect(self.rear)
        self.window.browse_corner.clicked.connect(self.corner)
        self.window.new_sku.clicked.connect(self.refresh_sku)
        self.window.save_new_product.clicked.connect(self.saveOnServer)
        self.window.save_settings.clicked.connect(self.save_settings)
        self.window.actionAbout.triggered.connect(self.aboutMe)
        self.window.search.clicked.connect(self.search)
        self.window.results.clicked.connect(self.item_edit)
        self.window_2.update_server.clicked.connect(self.update_item)
        self.window_2.engraving_zip_download.clicked.connect(self.engraving_zip_download)
        self.window_2.corner_download.clicked.connect(self.corner_download)
        self.window_2.rear_download.clicked.connect(self.rear_download)
        self.window_2.front_download.clicked.connect(self.front_download)
        self.window.formatEditor_testContent.clicked.connect(self.test_content_content)
        self.window.formatEditor_browse.clicked.connect(self.formatEditor_browse)
        self.window.formatEditor_save.clicked.connect(self.formatEditor_save)
        self.window.formatEditor_delete.clicked.connect(self.formatEditor_delete)
        self.window.formatEditor_testFile.clicked.connect(self.test_file_content)
        self.window.formatEditor_randomData.clicked.connect(self.random_data)
        self.window.ocr_browse.clicked.connect(self.ocr_browse_open)
        self.window.ocr_saveBrowse.clicked.connect(self.ocr_browse_save)
        self.window.ocr_save.clicked.connect(self.ocr_save)
        self.window.ocr_open.clicked.connect(self.ocr_process)
        self.window.import_browse.clicked.connect(self.import_location_browse)
        self.window.import_readfile.clicked.connect(self.import_readfile)
        self.window.import_sendToServer.clicked.connect(self.make_product)
        self.window.dontParse.toggled.connect(lambda x:self.window.import_sendToServer.setEnabled(not x))
        self.window_2.closeMe.clicked.connect(self.close_window_2)
        self.window.file2qr_start.clicked.connect(self.setup_file2qr_worker)
        self.window.file2qr_source_browse.clicked.connect(self.file2qr_source_browse)
        self.window.file2qr_destination_browse.clicked.connect(self.file2qr_destination_browse)
        self.window.qr2file_start.clicked.connect(self.qr2file_start)
        self.window.qr2file_source_browse.clicked.connect(self.qr2file_source_browse)
        self.window.qr2file_destination_browse.clicked.connect(self.qr2file_destination_browse)
        self.window_2.files2qr_download_engraving_zip.clicked.connect(self.download_engraving_zip)
        self.window_2.files2qr_download_corner.clicked.connect(self.download_corner)
        self.window_2.files2qr_download_front.clicked.connect(self.download_front)
        self.window_2.files2qr_download_rear.clicked.connect(self.download_rear)

    def close_window_2(self):
        self.window_2.edit.setChecked(False)
        self.window_2.close()
    def downloaded(self,x):
        print('downloaded run()')
        msgBox = QMessageBox()
        #msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("""
        Downloaded '{x}'
        """.format(x=x))
        msgBox.setWindowTitle("Home2Bar About")
        msgBox.exec()
    def engraving_zip_download(self):
        try:
            with open(self.window_2.engraving_zip.text(),'wb') as file:
                file.write(base64.b64decode(self.file_engraving_zip.get('file')))
            self.downloaded(self.window_2.engraving_zip.text())
        except Exception as e:
            print(e)
            self.window.statusBar().showMessage(str(e))
    def front_download(self):
        try:
            with open(self.window_2.front.text(),'wb') as file:
                file.write(base64.b64decode(self.file_front.get('file')))
            self.downloaded(self.window_2.front.text())
        except Exception as e:
            print(e)
            self.window.statusBar().showMessage(str(e))
    def rear_download(self):
        try:
            with open(self.window_2.rear.text(),'wb') as file:
                file.write(base64.b64decode(self.file_rear.get('file')))
            self.downloaded(self.window_2.rear.text())
        except Exception as e:
            print(e)
            self.window.statusBar().showMessage(str(e))
    def corner_download(self):
        try:
            with open(self.window_2.corner.text(),'wb') as file:
                file.write(base64.b64decode(self.file_corner.get('file')))
            self.downloaded(self.window_2.corner.text())
        except Exception as e:
            print(e)
            self.window.statusBar().showMessage(str(e))
    def update_engraving_zip(self):
        objectInfo=self.window.results.currentItem().text()
        object_id=int(objectInfo.split(':')[1])
        try:
            if Path(self.window_2.engraving_zip.text()).exists():
                with open(self.window_2.engraving_zip.text(),'rb') as file:
                    response=requests.post("{server}/holzcraftsframes/update_files_id/".format(server=self.window.server.text()),headers={'Authorization':'Token {}'.format(self.window.token.text())},json={'id':object_id,'name':self.window_2.engraving_zip.text(),'file':base64.b64encode(file.read()).decode('utf-8'),'which':'engraving_zip'})
                    print(response)
                    self.window.statusBar().showMessage(str(response))
        except Exception as e:
            print(e)
            self.window.statusBar().showMessage(str(e))
    def update_front(self):
        objectInfo=self.window.results.currentItem().text()
        object_id=int(objectInfo.split(':')[1])
        try:
            if Path(self.window_2.front.text()).exists():
                with open(self.window_2.front.text(),'rb') as file:
                    response=requests.post("{server}/holzcraftsframes/update_files_id/".format(server=self.window.server.text()),headers={'Authorization':'Token {}'.format(self.window.token.text())},json={'id':object_id,'name':self.window_2.front.text(),'file':base64.b64encode(file.read()).decode('utf-8'),'which':'front'})
                    print(response)
                    self.window.statusBar().showMessage(str(response))
        except Exception as e:
            print(e)
            self.window.statusBar().showMessage(str(e))
    def update_rear(self):
        objectInfo=self.window.results.currentItem().text()
        object_id=int(objectInfo.split(':')[1])
        try:
            if Path(self.window_2.rear.text()).exists():
                with open(self.window_2.rear.text(),'rb') as file:
                    response=requests.post("{server}/holzcraftsframes/update_files_id/".format(server=self.window.server.text()),headers={'Authorization':'Token {}'.format(self.window.token.text())},json={'id':object_id,'name':self.window_2.rear.text(),'file':base64.b64encode(file.read()).decode('utf-8'),'which':'rear'})
                    print(response)
                    self.window.statusBar().showMessage(str(response))
        except Exception as e:
            print(e)
            self.window.statusBar().showMessage(str(e))
    def update_corner(self):
        objectInfo=self.window.results.currentItem().text()
        object_id=int(objectInfo.split(':')[1])
        try:
            if Path(self.window_2.corner.text()).exists():
                with open(self.window_2.corner.text(),'rb') as file:
                    response=requests.post("{server}/holzcraftsframes/update_files_id/".format(server=self.window.server.text()),headers={'Authorization':'Token {}'.format(self.window.token.text())},json={'id':object_id,'name':self.window_2.corner.text(),'file':base64.b64encode(file.read()).decode('utf-8'),'which':'corner'})
                    print(response)
                    self.window.statusBar().showMessage(str(response))
        except Exception as e:
            print(e)
            self.window.statusBar().showMessage(str(e))
    def delete_item(self,button):
        response=requests.post("{server}/holzcraftsframes/delete_item_id/".format(server=self.window.server.text()),headers={'Authorization':'Token {}'.format(self.window.token.text())},json={'id':int(self.window.results.currentItem().text().split(":")[1])})
        self.window_2.close()
        self.search(None)
    def delete_engraving_zip(self):
        response=requests.post("{server}/holzcraftsframes/delete_files_id/".format(server=self.window.server.text()),headers={'Authorization':'Token {}'.format(self.window.token.text())},json={'id':int(self.window.results.currentItem().text().split(":")[1]),'which':'engraving_zip'})
        print(response)
        self.window.statusBar().showMessage(str(response))
        self.window_2.engraving_zip.setText('')
    def delete_front(self):
        response=requests.post("{server}/holzcraftsframes/delete_files_id/".format(server=self.window.server.text()),headers={'Authorization':'Token {}'.format(self.window.token.text())},json={'id':int(self.window.results.currentItem().text().split(":")[1]),'which':'front'})
        print(response)
        self.window.statusBar().showMessage(str(response))
        self.window_2.front.setText('')
    def delete_rear(self):
        response=requests.post("{server}/holzcraftsframes/delete_files_id/".format(server=self.window.server.text()),headers={'Authorization':'Token {}'.format(self.window.token.text())},json={'id':int(self.window.results.currentItem().text().split(":")[1]),'which':'rear'})
        print(response)
        self.window.statusBar().showMessage(str(response))
        self.window_2.rear.setText('')
    def delete_corner(self):
        response=requests.post("{server}/holzcraftsframes/delete_files_id/".format(server=self.window.server.text()),headers={'Authorization':'Token {}'.format(self.window.token.text())},json={'id':int(self.window.results.currentItem().text().split(":")[1]),'which':'corner'})
        print(response)
        self.window.statusBar().showMessage(str(response))
        self.window_2.corner.setText('')
    #setup editor
    def item_edit(self):
        currentItem=self.window.results.currentItem()
        id=currentItem.text().split(':')[1]
        response=requests.post('{server}/holzcraftsframes/get_id/'.format(server=self.window.server.text()),headers={'Authorization':'Token {}'.format(self.window.token.text())},json={'id':int(id)})
        #print(response.json())
        JSON=response.json()
        for key in JSON.keys():
            if key != 'id':
                widget=self.window_2.__dict__[key]
                print(key,'&^&'*4,JSON[key])
                if type(widget) is QComboBox:
                    #text=widget.currentText()
                    #name=widget.objectName()[:-2]
                    #data['{}__icontains'.format(name)]=text
                    #widget.setCurrentText(json[key])
                    widget.setCurrentIndex(widget.findText(JSON[key]))
                elif type(widget) is QLineEdit:
                    #text=widget.text()
                    #name=widget.objectName()[:-2]
                    #data['{}__icontains'.format(name)]=text
                    widget.setText(JSON[key])
                elif type(widget) is QDoubleSpinBox:
                    #text=widget.value()
                    #name=widget.objectName()[:-2]
                    #data['{}__icontains'.format(name)]=text
                    if not JSON[key]:
                        JSON[key]=-1
                    widget.setValue(float(JSON[key]))
                elif type(widget) is QPlainTextEdit:
                    #text=widget.toPlainText()
                    #name=widget.objectName()[:-2]
                    #data['{}__icontains'.format(name)]=text
                    widget.setPlainText(JSON[key])

        #this section should be put into ray
        #engraving_zip
        QMessageBox.about(self,'Downloading Files','engraving_zip will be downloaded!')
        response=requests.post("{server}/holzcraftsframes/get_files_id/".format(server=self.window.server.text()),headers={'Authorization':'Token {}'.format(self.window.token.text())},json={'id':int(id),'file':'engraving_zip'})
        content=b''
        for chunk in response.iter_content(chunk_size=512*1024):
            content+=chunk
        self.file_engraving_zip=json.loads(content.decode('utf-8'))
        self.window_2.engraving_zip.setText(self.file_engraving_zip.get('name'))

        QMessageBox.about(self,'Downloading Files','rear will be downloaded!')
        response=requests.post("{server}/holzcraftsframes/get_files_id/".format(server=self.window.server.text()),headers={'Authorization':'Token {}'.format(self.window.token.text())},json={'id':int(id),'file':'rear'})
        content=b''
        for chunk in response.iter_content(chunk_size=512*1024):
            content+=chunk
        self.file_rear=json.loads(content.decode('utf-8'))
        self.window_2.rear.setText(self.file_rear.get('name'))

        QMessageBox.about(self,'Downloading Files','front will be downloaded!')
        response=requests.post("{server}/holzcraftsframes/get_files_id/".format(server=self.window.server.text()),headers={'Authorization':'Token {}'.format(self.window.token.text())},json={'id':int(id),'file':'front'})
        content=b''
        for chunk in response.iter_content(chunk_size=512*1024):
            content+=chunk
        self.file_front=json.loads(content.decode('utf-8'))
        self.window_2.front.setText(self.file_front.get('name'))

        QMessageBox.about(self,'Downloading Files','corner will be downloaded!')
        response=requests.post("{server}/holzcraftsframes/get_files_id/".format(server=self.window.server.text()),headers={'Authorization':'Token {}'.format(self.window.token.text())},json={'id':int(id),'file':'corner'})
        content=b''
        for chunk in response.iter_content(chunk_size=512*1024):
            content+=chunk
        self.file_corner=json.loads(content.decode('utf-8'))
        self.window_2.corner.setText(self.file_corner.get('name'))

        #print(content,'JSON')
        self.setup_asQRTab()
        print("settings up images()")
        self.setup_downloaded_images()
        self.window_2.exec()
    def setup_downloaded_images(self):
        try:
            #self.file_corner_scene.updateSceneRect(QrectF(0,0,400,400))
            if self.file_corner.get('file'):
                data=BytesIO(base64.b64decode(self.file_corner.get('file')))
                data.seek(0)
                self.file_corner_rendered=Image.open(data)
                #nw,nh=self.file_corner_rendered.size
                #scale=30/100
                #nw=int(nw-(nw*scale))
                #nh=int(nh-(nh*scale))
                #self.file_corner_rendered=self.file_corner_rendered.resize((nw,nh))
                print('1')
                self.file_corner_qim=ImageQt(self.file_corner_rendered)
                print('2')
                self.file_corner_pix.setPixmap(QPixmap.fromImage(self.file_corner_qim))
                print('4')
                #self.window_2.corner_view.setScene(self.file_corner_scene)

                #self.file_corner_scene.update()

            else:
                print("print no images")
                self.file_corner_rendered=Image.new(size=(380,380),mode="RGBA")
                self.file_corner_qim=ImageQt(self.file_corner_rendered)
                self.file_corner_pix.setPixmap(QPixmap.fromImage(self.file_corner_qim))

        except Exception as e:

            print(e)
            self.statusBar().showMessage(str(e))
        try:
            #self.file_rear_scene.updateSceneRect(QrectF(0,0,400,400))
            if self.file_rear.get('file'):
                data=BytesIO(base64.b64decode(self.file_rear.get('file')))
                data.seek(0)
                self.file_rear_rendered=Image.open(data)

                print('1')
                self.file_rear_qim=ImageQt(self.file_rear_rendered)
                print('2')
                self.file_rear_pix.setPixmap(QPixmap.fromImage(self.file_rear_qim))
                print('4')
                #self.window_2.rear_view.setScene(self.file_rear_scene)

                #self.file_rear_scene.update()

            else:
                print("print no images")
                self.file_rear_rendered=Image.new(size=(380,380),mode="RGBA")
                self.file_rear_qim=ImageQt(self.file_rear_rendered)
                self.file_rear_pix.setPixmap(QPixmap.fromImage(self.file_rear_qim))

        except Exception as e:

            print(e)
            self.statusBar().showMessage(str(e))

        try:
            #self.file_front_scene.updateSceneRect(QrectF(0,0,400,400))
            if self.file_front.get('file'):
                data=BytesIO(base64.b64decode(self.file_front.get('file')))
                data.seek(0)
                self.file_front_rendered=Image.open(data)

                print('1')
                self.file_front_qim=ImageQt(self.file_front_rendered)
                print('2')
                self.file_front_pix.setPixmap(QPixmap.fromImage(self.file_front_qim))
                print('4')
                #self.window_2.front_view.setScene(self.file_front_scene)

                #self.file_front_scene.update()

            else:
                print("print no images")
                self.file_front_rendered=Image.new(size=(380,380),mode="RGBA")
                self.file_front_qim=ImageQt(self.file_front_rendered)
                self.file_front_pix.setPixmap(QPixmap.fromImage(self.file_front_qim))

        except Exception as e:

            print(e)
            self.statusBar().showMessage(str(e))
    def setup_search(self):
        #self.search_fields=['{}_c'.format(i.name) for i in HolzCraftsFrameEnum if not i.name.startswith('__') and i.name not in ['rear','front','engraving_zip','corner']]
        #for i in self.search_fields:
        #    self.window.__dict__.get(i).stateChanged.connect(self.enabler)
        for i in HolzCraftsFrameEnum.__fields__(HolzCraftsFrameEnum):
            if i != 'id':
                ii='{}_2'.format(i)
                i='{}_c'.format(i)
                print(ii)
                self.window.__dict__.get(ii).setEnabled(False)
                self.window.__dict__.get(i).stateChanged.connect(self.enabler)
    @pyqtSlot()
    def enabler(self):
        cb=self.sender()
        name=cb.objectName()
        name='{}_2'.format(name[:-2])
        print(name)
        self.window.__dict__.get(name).setEnabled(cb.isChecked())
    def search(self,btn):
        fields=['{}_2'.format(i) for i in dir(HolzCraftsFrameEnum) if not i.startswith('__') and i not in ['id','rear','front','engraving_zip','corner']]
        widgets=[]
        for i in fields:
            widgets.append(self.window.__dict__.get(i))
        data={}
        for widget in widgets:
            if widget.isEnabled():
                if type(widget) is QComboBox:
                    text=widget.currentText()
                    name=widget.objectName()[:-2]
                    data['{}__icontains'.format(name)]=text
                elif type(widget) is QLineEdit:
                    text=widget.text()
                    name=widget.objectName()[:-2]
                    data['{}__icontains'.format(name)]=text
                elif type(widget) is QDoubleSpinBox:
                    text=widget.value()
                    name=widget.objectName()[:-2]
                    data['{}__icontains'.format(name)]=text
                elif type(widget) is QPlainTextEdit:
                    text=widget.toPlainText()
                    name=widget.objectName()[:-2]
                    data['{}__icontains'.format(name)]=text
        print(data)
        uri=self.window.server.text()+'/holzcraftsframes/searchEP/'
        print(uri)
        response=requests.post(uri,headers={'Authorization':'Token {}'.format(self.window.token.text())},json=data)
        json=response.json()
        print(json)
        #for i in range(self.window.results.count()):
        #    self.window.results.takeItem(i)
        self.window.results.clear()
        for num,key in enumerate(json):
            print(key)
            self.window.results.addItem(
            '{sku}:{id}:{product_type}'.format(
            sku=json[num].get('sku'),
            product_type=json[num].get("product_type"),
            id=json[num].get('id')
            )
            )
        print(len(json))
    def save_settings(self):
        with open('settings.cfg','wb') as saved:
            settings=dict(token=self.window.token.text(),server=self.window.server.text())
            pickle.dump(settings,saved)
        self.window.statusBar().showMessage('settings saved!')
    def load_settings(self):
        try:
            with open('settings.cfg','rb') as settings:
                settled=pickle.load(settings)
                self.window.token.setText(settled.get('token'))
                self.window.server.setText(settled.get('server'))
                self.window.statusBar().showMessage('settings loaded!')
        except Exception as e:
            print(e)
            self.window.statusBar().showMessage(str(e)+":settings was not loaded")
    def run_pollthread(self):
        self.setup_external_worker()
        self.threadpool.start(self.worker)
    def setup_comboBoxes2(self):
        def product_type(self):
            for value in HolzCraftsFrameEnum.product_type.value:
                self.window.product_type_2.addItem(value[0])
        def size(self):
            for value in HolzCraftsFrameEnum.size.value:
                self.window.size_2.addItem(value[0])
        def can_hold_glass(self):
            for value in HolzCraftsFrameEnum.can_hold_glass.value:
                self.window.can_hold_glass_2.addItem(value[0])
        def can_hold_canvas(self):
            for value in HolzCraftsFrameEnum.can_hold_canvas.value:
                self.window.can_hold_canvas_2.addItem(value[0])
        def has_glass(self):
            for value in HolzCraftsFrameEnum.has_glass.value:
                self.window.has_glass_2.addItem(value[0])
        def has_canvas(self):
            for value in HolzCraftsFrameEnum.has_canvas.value:
                self.window.has_canvas_2.addItem(value[0])
        def orientation(self):
            for value in HolzCraftsFrameEnum.orientation.value:
                self.window.orientation_2.addItem(value[0])
        def wood_type(self):
            for value in HolzCraftsFrameEnum.wood_type.value:
                self.window.wood_type_2.addItem(value[0])
        '''
        def #munge#(self):
            for value in HolzCraftsFrameEnum.#munge#.value:
                self.window.#munge#.addItem(value[0])
        '''
        def front_outer_profile(self):
            for value in HolzCraftsFrameEnum.front_outer_profile.value:
                self.window.front_outer_profile_2.addItem(value[0])
        def front_inner_profile(self):
            for value in HolzCraftsFrameEnum.front_inner_profile.value:
                self.window.front_inner_profile_2.addItem(value[0])
        def rear_inner_profile(self):
            for value in HolzCraftsFrameEnum.rear_inner_profile.value:
                self.window.rear_inner_profile_2.addItem(value[0])
        def center_inner_profile(self):
            for value in HolzCraftsFrameEnum.center_inner_profile.value:
                self.window.center_inner_profile_2.addItem(value[0])
        def center_outer_profile(self):
            for value in HolzCraftsFrameEnum.center_outer_profile.value:
                self.window.center_outer_profile_2.addItem(value[0])
        def finish_type(self):
            for value in HolzCraftsFrameEnum.finish_type.value:
                self.window.finish_type_2.addItem(value[0])
        def stackable(self):
            for value in HolzCraftsFrameEnum.stackable.value:
                self.window.stackable_2.addItem(value[0])
        def custom_engraved(self):
            for value in HolzCraftsFrameEnum.custom_engraved.value:
                self.window.custom_engraved_2.addItem(value[0])
        def sold(self):
            for value in HolzCraftsFrameEnum.sold.value:
                self.window.sold_2.addItem(value[0])
        def stainable(self):
            for value in HolzCraftsFrameEnum.stainable.value:
                self.window.stainable_2.addItem(value[0])
        def frame_shape(self):
            for value in HolzCraftsFrameEnum.frame_shape.value:
                self.window.frame_shape_2.addItem(value[0])
        def other_frame_size_diameter_unit(self):
            for value in HolzCraftsFrameEnum.other_frame_size_diameter_unit.value:
                self.window.other_frame_size_diameter_unit_2.addItem(value[0])
        def item_weight_unit(self):
            for value in HolzCraftsFrameEnum.item_weight_unit.value:
                self.window.item_weight_unit_2.addItem(value[0])
        def paid_for(self):
            for value in HolzCraftsFrameEnum.paid_for.value:
                self.window.paid_for_2.addItem(value[0])

        def init(self):
            product_type(self)
            size(self)
            can_hold_glass(self)
            can_hold_canvas(self)
            has_glass(self)
            has_canvas(self)
            orientation(self)
            wood_type(self)
            front_outer_profile(self)
            front_inner_profile(self)
            rear_inner_profile(self)
            center_inner_profile(self)
            center_outer_profile(self)
            finish_type(self)
            stackable(self)
            custom_engraved(self)
            sold(self)
            stainable(self)
            frame_shape(self)
            other_frame_size_diameter_unit(self)
            item_weight_unit(self)
            paid_for(self)
        init(self)
    def setup_comboBoxes(self):
        def product_type(self):
            for value in HolzCraftsFrameEnum.product_type.value:
                self.window.product_type.addItem(value[0])
        def size(self):
            for value in HolzCraftsFrameEnum.size.value:
                self.window.size.addItem(value[0])
        def can_hold_glass(self):
            for value in HolzCraftsFrameEnum.can_hold_glass.value:
                self.window.can_hold_glass.addItem(value[0])
        def can_hold_canvas(self):
            for value in HolzCraftsFrameEnum.can_hold_canvas.value:
                self.window.can_hold_canvas.addItem(value[0])
        def has_glass(self):
            for value in HolzCraftsFrameEnum.has_glass.value:
                self.window.has_glass.addItem(value[0])
        def has_canvas(self):
            for value in HolzCraftsFrameEnum.has_canvas.value:
                self.window.has_canvas.addItem(value[0])
        def orientation(self):
            for value in HolzCraftsFrameEnum.orientation.value:
                self.window.orientation.addItem(value[0])
        def wood_type(self):
            for value in HolzCraftsFrameEnum.wood_type.value:
                self.window.wood_type.addItem(value[0])
        '''
        def #munge#(self):
            for value in HolzCraftsFrameEnum.#munge#.value:
                self.window.#munge#.addItem(value[0])
        '''
        def front_outer_profile(self):
            for value in HolzCraftsFrameEnum.front_outer_profile.value:
                self.window.front_outer_profile.addItem(value[0])
        def front_inner_profile(self):
            for value in HolzCraftsFrameEnum.front_inner_profile.value:
                self.window.front_inner_profile.addItem(value[0])
        def rear_inner_profile(self):
            for value in HolzCraftsFrameEnum.rear_inner_profile.value:
                self.window.rear_inner_profile.addItem(value[0])
        def center_inner_profile(self):
            for value in HolzCraftsFrameEnum.center_inner_profile.value:
                self.window.center_inner_profile.addItem(value[0])
        def center_outer_profile(self):
            for value in HolzCraftsFrameEnum.center_outer_profile.value:
                self.window.center_outer_profile.addItem(value[0])
        def finish_type(self):
            for value in HolzCraftsFrameEnum.finish_type.value:
                self.window.finish_type.addItem(value[0])
        def stackable(self):
            for value in HolzCraftsFrameEnum.stackable.value:
                self.window.stackable.addItem(value[0])
        def custom_engraved(self):
            for value in HolzCraftsFrameEnum.custom_engraved.value:
                self.window.custom_engraved.addItem(value[0])
        def sold(self):
            for value in HolzCraftsFrameEnum.sold.value:
                self.window.sold.addItem(value[0])
        def stainable(self):
            for value in HolzCraftsFrameEnum.stainable.value:
                self.window.stainable.addItem(value[0])
        def frame_shape(self):
            for value in HolzCraftsFrameEnum.frame_shape.value:
                self.window.frame_shape.addItem(value[0])
        def other_frame_size_diameter_unit(self):
            for value in HolzCraftsFrameEnum.other_frame_size_diameter_unit.value:
                self.window.other_frame_size_diameter_unit.addItem(value[0])
        def item_weight_unit(self):
            for value in HolzCraftsFrameEnum.item_weight_unit.value:
                self.window.item_weight_unit.addItem(value[0])
        def paid_for(self):
            for value in HolzCraftsFrameEnum.paid_for.value:
                self.window.paid_for.addItem(value[0])

        def init(self):
            product_type(self)
            size(self)
            can_hold_glass(self)
            can_hold_canvas(self)
            has_glass(self)
            has_canvas(self)
            orientation(self)
            wood_type(self)
            front_outer_profile(self)
            front_inner_profile(self)
            rear_inner_profile(self)
            center_inner_profile(self)
            center_outer_profile(self)
            finish_type(self)
            stackable(self)
            custom_engraved(self)
            sold(self)
            stainable(self)
            frame_shape(self)
            other_frame_size_diameter_unit(self)
            item_weight_unit(self)
        init(self)
        paid_for(self)
        self.setup_comboBoxes2()
        self.setup_comboBoxes3()
    ##start editor functions
    def update_item(self,button):
        btn=self.sender()
        objectInfo=self.window.results.currentItem().text()
        object_id=int(objectInfo.split(':')[1])
        response=requests.post("{server}/holzcraftsframes/get_id/".format(server=self.window.server.text()),headers={'Authorization':'Token {}'.format(self.window.token.text())},json={'id':object_id})
        original=response.json()
        new_code=copy(original)
        print(original,response,objectInfo)
        for key in original.keys():
            widget=self.window_2.__dict__.get(key)
            if type(widget) is QComboBox:
                new_code[key]=widget.currentText()
            elif type(widget) is QLineEdit:
                new_code[key]=widget.text()
            elif type(widget) is QDoubleSpinBox:
                new_code[key]=widget.value()
            elif type(widget) is QPlainTextEdit:
                new_code[key]=widget.toPlainText()
            else:
                print('{widget} is not useable'.format(widget=widget))
                print(widget)
            print(new_code)
        new_code['id']=object_id
        response=requests.post("{server}/holzcraftsframes/update_id/".format(server=self.window.server.text()),headers={'Authorization':'Token {}'.format(self.window.token.text())},json=new_code)
        self.statusBar().showMessage(str(response))
        if response.status_code == 200:
            QMessageBox().warning(None,"Success","Item Update was a success!")
    def get_engraving_zip(self):
        import_file=QFileDialog.getOpenFileName(filter="ZIP Files (*.zip);;Tar Files (*.tar);; XZ Files(*.xz);;GZ Files(*.gz);;All Files(*)")
        print(import_file)
        if import_file[0]:
            self.window_2.engraving_zip.setText(import_file[0])
    def get_rear(self):
        import_file=QFileDialog.getOpenFileName(filter="PNG Files (*.png *.PNG);;JPEG/JPG Files(*.jpg *.JPG *.jpeg *.JPEG);;All Files(*)")
        print(import_file)
        if import_file[0]:
            self.window_2.rear.setText(import_file[0])
    def get_front(self):
        import_file=QFileDialog.getOpenFileName(filter="PNG Files (*.png *.PNG);;JPEG/JPG Files(*.jpg *.JPG *.jpeg *.JPEG);;All Files(*)")
        print(import_file)
        if import_file[0]:
            self.window_2.front.setText(import_file[0])
    def get_corner(self):
        import_file=QFileDialog.getOpenFileName(filter="PNG Files (*.png *.PNG);;JPEG/JPG Files(*.jpg *.JPG *.jpeg *.JPEG);;All Files(*)")
        print(import_file)
        if import_file[0]:
            self.window_2.corner.setText(import_file[0])
    def setup_editor(self):
        self.window_2.browse_engraving_zip.clicked.connect(self.get_engraving_zip)
        self.window_2.browse_rear.clicked.connect(self.get_rear)
        self.window_2.browse_corner.clicked.connect(self.get_corner)
        self.window_2.browse_front.clicked.connect(self.get_front)
        self.window_2.update_engraving_zip.clicked.connect(self.update_engraving_zip)
        self.window_2.update_rear.clicked.connect(self.update_rear)
        self.window_2.update_corner.clicked.connect(self.update_corner)
        self.window_2.update_front.clicked.connect(self.update_front)
        self.window_2.new_sku.clicked.connect(self.refresh_sku_existing)
        self.window_2.delete_engraving_zip.clicked.connect(self.delete_engraving_zip)
        self.window_2.delete_front.clicked.connect(self.delete_front)
        self.window_2.delete_rear.clicked.connect(self.delete_rear)
        self.window_2.delete_corner.clicked.connect(self.delete_corner)
        self.window_2.delete_item.clicked.connect(self.delete_item)
        self.window_2.browse_qr_save_location.clicked.connect(self.get_qr_save_location)
        self.window_2.save_qrcode.clicked.connect(self.save_qr_code)
        self.window_2.get_label_file.clicked.connect(self.get_label_file)
        self.window_2.print.clicked.connect(self.print_)
    def print_(self):
        data='Item(sku="{sku}") printed on {date}\n'.format(sku=self.exportable.get('sku'),date=datetime.now().ctime())
        data+=(len(data)-1)*'='
        data+="\n"
        for i in self.exportable.keys():
            data+='{} = {}\n'.format(i,self.exportable.get(i))
        os.system("echo -e '{data}' | lpr".format(data=data))
    def get_label_file(self):
        save_file,extension=QFileDialog.getSaveFileName(filter="SVG Files(*.svg);;All Files(*)",directory=self.window_2.sku.text()+".svg")
        if extension == 'SVG Files(*.svg)':
            if Path(save_file).suffix != '.svg':
                save_file+=".svg"
            modder=Modify(upc=self.window_2.sku.text(),phone_number='(804) 854-4057',outfile_name=save_file)
        print(save_file)
        if self.window_2.open_inkscape.isChecked():
            val=os.system("inkscape '{file}' &".format(file=save_file))
            self.window.statusBar().showMessage("opening inkscape!")
    def save_qr_code(self,button):
        self.im.save(self.window_2.qr_save_location.text())
        self.window.statusBar().showMessage("saved {}!".format(self.window_2.qr_save_location.text()))
    def get_qr_save_location(self,button):
            import_file=QFileDialog.getSaveFileName(filter="PNG Files(*.png);;All Files(*)")
            print(import_file)
            if import_file[0]:
                self.window_2.qr_save_location.setText(import_file[0])
    def setup_asQRTab(self):
        sender=self.sender()
        id=self.window.results.currentItem().text().split(':')[1]
        self.window_2.qr_save_location.setText(self.window_2.qr_save_location.text().format(sku=id))
        response=requests.post("{server}/holzcraftsframes/get_id/".format(server=self.window.server.text()),headers={"Authorization":"Token {}".format(self.window.token.text())},json={'id':id})
        self.exportable=response.json()
        data=json.dumps(response.json())
        bios=StringIO()
        bios.write(data)
        bios.seek(0)
        self.generate_QR(bios.read())
        self.window_2.export2fs.clicked.connect(self.export2fs)
    def export2fs(self,button):
        import_file,extension=QFileDialog.getSaveFileName(filter="JSON Files(*.json);;CSV Files(*.csv);;PICKLE FILE(*.pickle);;All Files(*)")
        print(import_file,extension)
        def run_exporter(filename,mode):
            if mode == "json":
                with open(filename,'w') as out:
                    json.dump(self.exportable,out)
            elif mode == "csv":
                with open(filename,'w') as out:
                    writer=csv.writer(out,delimiter=',')
                    writer.writerow([i for i in self.exportable.keys()])
                    writer.writerow([i for i in self.exportable.values()])
            elif mode == "pickle":
                with open(filename,'wb') as out:
                    pickle.dump(self.exportable,out)
            else:
                raise Exception("unsupported mode: modes are ['json','csv','pickle']")
        if import_file != '':
            print(Path(import_file).suffix)
            if Path(import_file).suffix == '':
                if extension == 'JSON Files(*.json)':
                    import_file=import_file+".json"
                    run_exporter(import_file,"json")
                elif extension == 'CSV Files(*.csv)':
                    import_file+=".csv"
                    run_exporter(import_file,"csv")
                elif extension == 'PICKLE FILE(*.pickle)':
                    import_file+=".pickle"
                    run_exporter(import_file,"pickle")
            else:
                if extension == 'JSON Files(*.json)':
                    import_file=import_file+".json"
                    run_exporter(import_file,"json")
                elif extension == 'CSV Files(*.csv)':
                    import_file+=".csv"
                    run_exporter(import_file,"csv")
                elif extension == 'PICKLE FILE(*.pickle)':
                    import_file+=".pickle"
                    run_exporter(import_file,"pickle")
    def generate_QR(self,code):
        tmp=code
        skip_next=False
        codeio=BytesIO()

        code=pyqrcode.create(tmp)
        try:
            #code.svg(code_name+'.svg',scale=8)
            code.png(codeio,scale=4)
            view=self.window_2.findChild(QGraphicsView,'as_view')
            #z.write(tmp)
            codeio.seek(0)
            #pix = QPixmap()
            self.im=Image.open(codeio)
            self.im.convert("RGBA")
            #im=im.resize([int(view.sceneRect().height()),int(view.sceneRect().width())])
            self.data=self.im.tobytes()
            #qim=QImage(data,im.size[0],im.size[1],QImage.Format.Format_ARGB32)
            self.qim=ImageQt(self.im)
            self.pix=QPixmap().fromImage(self.qim)
            self.scene=QGraphicsScene()
            #scene.setSceneRect(SceneRect())
            self.scene.addPixmap(self.pix)
            view.setScene(self.scene)
        except Exception as e:
            print(e)
            skip_next=True
    def refresh_sku_existing(self,button):
        self.window_2.sku.setText(self.generate_sku())
    ##stop editor functions
    @pyqtSlot()
    def enable_editor(self):
        print("enabler")
        self.window_2.scrollAreaWidgetContents.setEnabled(self.sender().isChecked())
    def setup_comboBoxes3(self):
        self.window_2.edit.stateChanged.connect(self.enable_editor)
        def product_type(self):
            for value in HolzCraftsFrameEnum.product_type.value:
                self.window_2.product_type.addItem(value[0])
        def size(self):
            for value in HolzCraftsFrameEnum.size.value:
                self.window_2.size.addItem(value[0])
        def can_hold_glass(self):
            for value in HolzCraftsFrameEnum.can_hold_glass.value:
                self.window_2.can_hold_glass.addItem(value[0])
        def can_hold_canvas(self):
            for value in HolzCraftsFrameEnum.can_hold_canvas.value:
                self.window_2.can_hold_canvas.addItem(value[0])
        def has_glass(self):
            for value in HolzCraftsFrameEnum.has_glass.value:
                self.window_2.has_glass.addItem(value[0])
        def has_canvas(self):
            for value in HolzCraftsFrameEnum.has_canvas.value:
                self.window_2.has_canvas.addItem(value[0])
        def orientation(self):
            for value in HolzCraftsFrameEnum.orientation.value:
                self.window_2.orientation.addItem(value[0])
        def wood_type(self):
            for value in HolzCraftsFrameEnum.wood_type.value:
                self.window_2.wood_type.addItem(value[0])
        '''
        def #munge#(self):
            for value in HolzCraftsFrameEnum.#munge#.value:
                self.window_2.#munge#.addItem(value[0])
        '''
        def front_outer_profile(self):
            for value in HolzCraftsFrameEnum.front_outer_profile.value:
                self.window_2.front_outer_profile.addItem(value[0])
        def front_inner_profile(self):
            for value in HolzCraftsFrameEnum.front_inner_profile.value:
                self.window_2.front_inner_profile.addItem(value[0])
        def rear_inner_profile(self):
            for value in HolzCraftsFrameEnum.rear_inner_profile.value:
                self.window_2.rear_inner_profile.addItem(value[0])
        def center_inner_profile(self):
            for value in HolzCraftsFrameEnum.center_inner_profile.value:
                self.window_2.center_inner_profile.addItem(value[0])
        def center_outer_profile(self):
            for value in HolzCraftsFrameEnum.center_outer_profile.value:
                self.window_2.center_outer_profile.addItem(value[0])
        def finish_type(self):
            for value in HolzCraftsFrameEnum.finish_type.value:
                self.window_2.finish_type.addItem(value[0])
        def stackable(self):
            for value in HolzCraftsFrameEnum.stackable.value:
                self.window_2.stackable.addItem(value[0])
        def custom_engraved(self):
            for value in HolzCraftsFrameEnum.custom_engraved.value:
                self.window_2.custom_engraved.addItem(value[0])
        def sold(self):
            for value in HolzCraftsFrameEnum.sold.value:
                self.window_2.sold.addItem(value[0])
        def stainable(self):
            for value in HolzCraftsFrameEnum.stainable.value:
                self.window_2.stainable.addItem(value[0])
        def frame_shape(self):
            for value in HolzCraftsFrameEnum.frame_shape.value:
                self.window_2.frame_shape.addItem(value[0])
        def other_frame_size_diameter_unit(self):
            for value in HolzCraftsFrameEnum.other_frame_size_diameter_unit.value:
                self.window_2.other_frame_size_diameter_unit.addItem(value[0])
        def item_weight_unit(self):
            for value in HolzCraftsFrameEnum.item_weight_unit.value:
                self.window_2.item_weight_unit.addItem(value[0])
        def paid_for(self):
            for value in HolzCraftsFrameEnum.paid_for.value:
                self.window_2.paid_for.addItem(value[0])
        def init(self):
            product_type(self)
            size(self)
            can_hold_glass(self)
            can_hold_canvas(self)
            has_glass(self)
            has_canvas(self)
            orientation(self)
            wood_type(self)
            front_outer_profile(self)
            front_inner_profile(self)
            rear_inner_profile(self)
            center_inner_profile(self)
            center_outer_profile(self)
            finish_type(self)
            stackable(self)
            custom_engraved(self)
            sold(self)
            stainable(self)
            frame_shape(self)
            other_frame_size_diameter_unit(self)
            item_weight_unit(self)
            paid_for(self)
            #self.window_2.rear_view.update
        init(self)
    def setup_lineEdits(self):
        def sku(self):
            self.window.sku.setText(self.generate_sku())
        sku(self)
    def generate_sku(self):
        tmp=[]
        for i in range(0,12):
            tmp.append(str(random.randint(0,9)))
        return ''.join(tmp)
    def setIconWindow(self):
        bits=base64.b64decode(self.icon)
        pixmap=QPixmap()
        pixmap.loadFromData(bits)
        icon=QIcon(pixmap)
        self.window.setWindowIcon(icon)
    def __init__(self,parent=None):
        self.file_corner=None
        self.file_rear=None
        self.file_front=None
        self.file_engraving_zip=None
        if os.geteuid() == 0:
            self.window=uic.loadUi("main.ui")
            exit("you should not be root!")
        self.app=QApplication(sys.argv)
        super().__init__()
        if len(sys.argv) > 1:
            if sys.argv[1] == 'debug':
                self.window=uic.loadUi("main.ui")
                self.window_2=uic.loadUi("itemui.ui")
            else:
                self.window=uic.loadUi(StringIO(base64.b64decode(self.ui).decode('utf-8')))
                self.window_2=uic.loadUi(StringIO(base64.b64decode(self.itemui).decode('utf-8')))
                self.setIconWindow()
        else:
            self.window=uic.loadUi(StringIO(base64.b64decode(self.ui).decode('utf-8')))
            self.window_2=uic.loadUi(StringIO(base64.b64decode(self.itemui).decode('utf-8')))
            self.setIconWindow()

        self.setup_comboBoxes()
        self.setup_lineEdits()
        self.threadpool=QThreadPool()
        self.setup_external_worker()
        self.setup_buttons()
        self.setup_search()

        self.poller=QTimer(self)
        self.poller.timeout.connect(self.run_pollthread)
        self.poller.start(1000)
        self.setup_editor()
        self.load_settings()
        self.file_front_scene=QGraphicsScene()
        self.file_rear_scene=QGraphicsScene()
        self.file_corner_scene=QGraphicsScene()

        self.file_corner_rendered=Image.new(size=(380,380),mode="RGBA")
        self.file_rear_rendered=Image.new(size=(380,380),mode="RGBA")
        self.file_front_rendered=Image.new(size=(380,380),mode="RGBA")

        self.file_corner_qim=ImageQt(self.file_corner_rendered)
        self.file_corner_pix=QGraphicsPixmapItem()

        self.file_front_qim=ImageQt(self.file_front_rendered)
        self.file_front_pix=QGraphicsPixmapItem()
        self.file_rear_qim=ImageQt(self.file_rear_rendered)
        self.file_rear_pix=QGraphicsPixmapItem()


        self.ocr_scene=QGraphicsScene()
        self.ocr_img=Image.new(size=(580,580),mode="RGBA",color=(255,0,0))

        self.ocr_qim=ImageQt(self.ocr_img)
        self.ocr_pix=QGraphicsPixmapItem()

        self.ocr_pix.setPixmap(QPixmap.fromImage(self.ocr_qim))
        self.window.ocr_imageView.setScene(self.ocr_scene)
        self.window.ocr_imageView.fitInView(QRectF(0,0,30,30),Qt.AspectRatioMode.KeepAspectRatio)
        self.ocr_scene.addItem(self.ocr_pix)

        self.window_2.corner_view.setScene(self.file_corner_scene)
        self.window_2.corner_view.fitInView(0,0,380,380,Qt.AspectRatioMode.KeepAspectRatio)
        self.file_corner_scene.addItem(self.file_corner_pix)

        self.window_2.front_view.setScene(self.file_front_scene)
        self.window_2.front_view.fitInView(0,0,380,380,Qt.AspectRatioMode.KeepAspectRatio)
        self.file_front_scene.addItem(self.file_front_pix)

        self.window_2.rear_view.setScene(self.file_rear_scene)
        self.window_2.rear_view.fitInView(0,0,380,380,Qt.AspectRatioMode.KeepAspectRatio)
        self.file_rear_scene.addItem(self.file_rear_pix)

        self.window.show()
        self.app.exec()
    ui='''PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHVpIHZlcnNpb249IjQuMCI+CiA8Y2xhc3M+TWFpbldpbmRvdzwvY2xhc3M+CiA8d2lkZ2V0IGNsYXNzPSJRTWFpbldpbmRvdyIgbmFtZT0iTWFpbldpbmRvdyI+CiAgPHByb3BlcnR5IG5hbWU9Imdlb21ldHJ5Ij4KICAgPHJlY3Q+CiAgICA8eD4wPC94PgogICAgPHk+MDwveT4KICAgIDx3aWR0aD4xMTU4PC93aWR0aD4KICAgIDxoZWlnaHQ+ODA1PC9oZWlnaHQ+CiAgIDwvcmVjdD4KICA8L3Byb3BlcnR5PgogIDxwcm9wZXJ0eSBuYW1lPSJ3aW5kb3dUaXRsZSI+CiAgIDxzdHJpbmc+SG9semNyYWZ0c0FkbWluPC9zdHJpbmc+CiAgPC9wcm9wZXJ0eT4KICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgIDxzdHJpbmc+bWFuYWdlIGhvbHpjcmFmdHM8L3N0cmluZz4KICA8L3Byb3BlcnR5PgogIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICA8c3RyaW5nPm1hbmFnZSBob2x6Y3JhZnRzPC9zdHJpbmc+CiAgPC9wcm9wZXJ0eT4KICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgPHN0cmluZz5tYW5hZ2UgaG9semNyYWZ0czwvc3RyaW5nPgogIDwvcHJvcGVydHk+CiAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgPHN0cmluZz5tYW5hZ2UgaG9semNyYWZ0czwvc3RyaW5nPgogIDwvcHJvcGVydHk+CiAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgIDxzdHJpbmc+bWFuYWdlIGhvbHpjcmFmdHM8L3N0cmluZz4KICA8L3Byb3BlcnR5PgogIDxwcm9wZXJ0eSBuYW1lPSJhdXRvRmlsbEJhY2tncm91bmQiPgogICA8Ym9vbD50cnVlPC9ib29sPgogIDwvcHJvcGVydHk+CiAgPHByb3BlcnR5IG5hbWU9IndpbmRvd0ZpbGVQYXRoIj4KICAgPHN0cmluZz4uPC9zdHJpbmc+CiAgPC9wcm9wZXJ0eT4KICA8cHJvcGVydHkgbmFtZT0iZG9ja05lc3RpbmdFbmFibGVkIj4KICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICA8L3Byb3BlcnR5PgogIDx3aWRnZXQgY2xhc3M9IlFXaWRnZXQiIG5hbWU9ImNlbnRyYWx3aWRnZXQiPgogICA8bGF5b3V0IGNsYXNzPSJRR3JpZExheW91dCIgbmFtZT0iZ3JpZExheW91dCI+CiAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMCI+CiAgICAgPHdpZGdldCBjbGFzcz0iUVRhYldpZGdldCIgbmFtZT0idGFiV2lkZ2V0Ij4KICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgPHN0cmluZz5jb252ZXJ0IGEgLnFyLnRhci54eiBmaWxlIHRvIGl0cyBmaWxlIGNvbnRlbnQ8L3N0cmluZz4KICAgICAgPC9wcm9wZXJ0eT4KICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICA8c3RyaW5nPmNvbnZlcnQgYSAucXIudGFyLnh6IGZpbGUgdG8gaXRzIGZpbGUgY29udGVudDwvc3RyaW5nPgogICAgICA8L3Byb3BlcnR5PgogICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgIDxzdHJpbmc+Y29udmVydCBhIC5xci50YXIueHogZmlsZSB0byBpdHMgZmlsZSBjb250ZW50PC9zdHJpbmc+CiAgICAgIDwvcHJvcGVydHk+CiAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICA8c3RyaW5nPmNvbnZlcnQgYSAucXIudGFyLnh6IGZpbGUgdG8gaXRzIGZpbGUgY29udGVudDwvc3RyaW5nPgogICAgICA8L3Byb3BlcnR5PgogICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgIDxzdHJpbmc+Y29udmVydCBhIC5xci50YXIueHogZmlsZSB0byBpdHMgZmlsZSBjb250ZW50PC9zdHJpbmc+CiAgICAgIDwvcHJvcGVydHk+CiAgICAgIDxwcm9wZXJ0eSBuYW1lPSJjdXJyZW50SW5kZXgiPgogICAgICAgPG51bWJlcj4xPC9udW1iZXI+CiAgICAgIDwvcHJvcGVydHk+CiAgICAgIDx3aWRnZXQgY2xhc3M9IlFXaWRnZXQiIG5hbWU9InRhYiI+CiAgICAgICA8YXR0cmlidXRlIG5hbWU9InRpdGxlIj4KICAgICAgICA8c3RyaW5nPk5ldyBQcm9kdWN0PC9zdHJpbmc+CiAgICAgICA8L2F0dHJpYnV0ZT4KICAgICAgIDxsYXlvdXQgY2xhc3M9IlFHcmlkTGF5b3V0IiBuYW1lPSJncmlkTGF5b3V0XzIiPgogICAgICAgIDxpdGVtIHJvdz0iMyIgY29sdW1uPSIxIj4KICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNoZWNrQm94IiBuYW1lPSJyZXNldF93aGVuX2RvbmUiPgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgIDxzdHJpbmc+cmVzZXQgZm9ybSB3aGVuIGRvbmU8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICA8c3RyaW5nPnJlc2V0IGZvcm0gd2hlbiBkb25lPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgPHN0cmluZz5yZXNldCBmb3JtIHdoZW4gZG9uZTwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgPHN0cmluZz5yZXNldCBmb3JtIHdoZW4gZG9uZTwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgIDxzdHJpbmc+cmVzZXQgZm9ybSB3aGVuIGRvbmU8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgPHN0cmluZz5SZXNldCBXaGVuIERvbmU8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iY2hlY2tlZCI+CiAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgIDwvaXRlbT4KICAgICAgICA8aXRlbSByb3c9IjMiIGNvbHVtbj0iMCI+CiAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDaGVja0JveCIgbmFtZT0ibmV3X3NrdV93aGVuX2RvbmUiPgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgIDxzdHJpbmc+Z2VuZXJhdGUgbmV3IHNrdSB3aGVuIGRvbmU8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICA8c3RyaW5nPmdlbmVyYXRlIG5ldyBza3Ugd2hlbiBkb25lPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgPHN0cmluZz5nZW5lcmF0ZSBuZXcgc2t1IHdoZW4gZG9uZTwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgPHN0cmluZz5nZW5lcmF0ZSBuZXcgc2t1IHdoZW4gZG9uZTwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgIDxzdHJpbmc+Z2VuZXJhdGUgbmV3IHNrdSB3aGVuIGRvbmU8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgPHN0cmluZz5OZXcgU0tVIFdoZW4gRG9uZTwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJjaGVja2VkIj4KICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgPC9pdGVtPgogICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIwIiBjb2xzcGFuPSIyIj4KICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVNjcm9sbEFyZWEiIG5hbWU9InNjcm9sbEFyZWEiPgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndpZGdldFJlc2l6YWJsZSI+CiAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRV2lkZ2V0IiBuYW1lPSJzY3JvbGxBcmVhV2lkZ2V0Q29udGVudHMiPgogICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJnZW9tZXRyeSI+CiAgICAgICAgICAgIDxyZWN0PgogICAgICAgICAgICAgPHg+MDwveD4KICAgICAgICAgICAgIDx5PjA8L3k+CiAgICAgICAgICAgICA8d2lkdGg+MTEyMjwvd2lkdGg+CiAgICAgICAgICAgICA8aGVpZ2h0PjYxMTwvaGVpZ2h0PgogICAgICAgICAgICA8L3JlY3Q+CiAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICA8bGF5b3V0IGNsYXNzPSJRR3JpZExheW91dCIgbmFtZT0iZ3JpZExheW91dF8zIj4KICAgICAgICAgICAgPGl0ZW0gcm93PSI0IiBjb2x1bW49IjIiIGNvbHNwYW49IjciPgogICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUdyb3VwQm94IiBuYW1lPSJncm91cEJveCI+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRpdGxlIj4KICAgICAgICAgICAgICAgPHN0cmluZz5FbmdyYXZpbmcgWmlwPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8bGF5b3V0IGNsYXNzPSJRR3JpZExheW91dCIgbmFtZT0iZ3JpZExheW91dF80Ij4KICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjIiPgogICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9ImJyb3dzZV9lbmdyYXZpbmdfemlwIj4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgZW5ncmF2aW5nIHppcDwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGVuZ3JhdmluZyB6aXA8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGVuZ3JhdmluZyB6aXA8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBlbmdyYXZpbmcgemlwPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+QnJvd3NlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFMaW5lRWRpdCIgbmFtZT0iZW5ncmF2aW5nX3ppcCI+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmVuZ3JhdmluZ196aXA8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmVuZ3JhdmluZ196aXA8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmVuZ3JhdmluZ196aXA8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZW5ncmF2aW5nX3ppcDwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZW5ncmF2aW5nX3ppcDwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImRyYWdFbmFibGVkIj4KICAgICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFjZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmVuZ3JhdmluZy56aXA8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJjbGVhckJ1dHRvbkVuYWJsZWQiPgogICAgICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9ImN1c3RvbV9lbmdyYXZlZCI+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmN1c3RvbV9lbmdyYXZlZDwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+Y3VzdG9tX2VuZ3JhdmVkPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5jdXN0b21fZW5ncmF2ZWQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+Y3VzdG9tX2VuZ3JhdmVkPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5jdXN0b21fZW5ncmF2ZWQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICA8L2xheW91dD4KICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iNiIgY29sdW1uPSIyIiBjb2xzcGFuPSI3Ij4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFHcm91cEJveCIgbmFtZT0iZ3JvdXBCb3hfNCI+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRpdGxlIj4KICAgICAgICAgICAgICAgPHN0cmluZz5Db3JuZXI8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxsYXlvdXQgY2xhc3M9IlFHcmlkTGF5b3V0IiBuYW1lPSJncmlkTGF5b3V0XzUiPgogICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRTGluZUVkaXQiIG5hbWU9ImNvcm5lciI+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBjb3JuZXIgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGNvcm5lciBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgY29ybmVyIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGNvcm5lciBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgY29ybmVyIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJkcmFnRW5hYmxlZCI+CiAgICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0icGxhY2Vob2xkZXJUZXh0Ij4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5jb3JuZXIuZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImNsZWFyQnV0dG9uRW5hYmxlZCI+CiAgICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJicm93c2VfY29ybmVyIj4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGNvcm5lciBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgY29ybmVyIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBjb3JuZXIgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgY29ybmVyIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBjb3JuZXIgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPkJyb3dzZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgIDwvbGF5b3V0PgogICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjIiPgogICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJjYW5faG9sZF9nbGFzcyI+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPmNhbiBob2xkIGdsYXNzPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz5jYW4gaG9sZCBnbGFzczwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+Y2FuIGhvbGQgZ2xhc3M8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+Y2FuIGhvbGQgZ2xhc3M8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICA8c3RyaW5nPmNhbiBob2xkIGdsYXNzPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSIwIj4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0iZnJvbnRfb3V0ZXJfcHJvZmlsZSI+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPmZyb250IG91dGVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPmZyb250IG91dGVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICA8c3RyaW5nPmZyb250IG91dGVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJvbnQgb3V0ZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJvbnQgb3V0ZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMSI+CiAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9InNpemUiPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz5zaXplPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz5zaXplPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgPHN0cmluZz5zaXplPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICA8c3RyaW5nPnNpemU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICA8c3RyaW5nPnNpemU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjEiPgogICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJmcm9udF9pbm5lcl9wcm9maWxlIj4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJvbnQgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJvbnQgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJvbnQgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgPHN0cmluZz5mcm9udCBpbm5lciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgPHN0cmluZz5mcm9udCBpbm5lciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSIyIj4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0icmVhcl9pbm5lcl9wcm9maWxlIj4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+cmVhciBpbm5lciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz5yZWFyIGlubmVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICA8c3RyaW5nPnJlYXIgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgPHN0cmluZz5yZWFyIGlubmVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICA8c3RyaW5nPnJlYXIgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICA8aXRlbSByb3c9IjQiIGNvbHVtbj0iMCIgcm93c3Bhbj0iNCIgY29sc3Bhbj0iMiI+CiAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUGxhaW5UZXh0RWRpdCIgbmFtZT0iY29tbWVudHMiPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz5jb21tZW50czwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+Y29tbWVudHM8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICA8c3RyaW5nPmNvbW1lbnRzPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICA8c3RyaW5nPmNvbW1lbnRzPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgPHN0cmluZz5jb21tZW50czwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRhYkNoYW5nZXNGb2N1cyI+CiAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0icGxhY2Vob2xkZXJUZXh0Ij4KICAgICAgICAgICAgICAgPHN0cmluZz5jb21tZW50czwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICA8aXRlbSByb3c9IjciIGNvbHVtbj0iMiIgY29sc3Bhbj0iNyI+CiAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRR3JvdXBCb3giIG5hbWU9Imdyb3VwQm94XzMiPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0aXRsZSI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+RnJvbnQ8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxsYXlvdXQgY2xhc3M9IlFHcmlkTGF5b3V0IiBuYW1lPSJncmlkTGF5b3V0XzciPgogICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRTGluZUVkaXQiIG5hbWU9ImZyb250Ij4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJvbnQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmZyb250PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5mcm9udDwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5mcm9udDwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJvbnQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJkcmFnRW5hYmxlZCI+CiAgICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0icGxhY2Vob2xkZXJUZXh0Ij4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5mcm9udC5maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iY2xlYXJCdXR0b25FbmFibGVkIj4KICAgICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjEiPgogICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9ImJyb3dzZV9mcm9udCI+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBmcm9udCBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgZnJvbnQgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGZyb250IGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGZyb250IGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBmcm9udCBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+QnJvd3NlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPC9sYXlvdXQ+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICA8aXRlbSByb3c9IjUiIGNvbHVtbj0iMiIgY29sc3Bhbj0iNyI+CiAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRR3JvdXBCb3giIG5hbWU9Imdyb3VwQm94XzIiPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0aXRsZSI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+UmVhcjwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRMYXlvdXRfNiI+CiAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIwIj4KICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFMaW5lRWRpdCIgbmFtZT0icmVhciI+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPnJlYXI8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPnJlYXI8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPnJlYXI8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+cmVhcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+cmVhcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImRyYWdFbmFibGVkIj4KICAgICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFjZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPnJlYXIuZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImNsZWFyQnV0dG9uRW5hYmxlZCI+CiAgICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJicm93c2VfcmVhciI+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIHJlYXIgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIHJlYXIgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgcmVhciBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgcmVhciBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+QnJvd3NlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPC9sYXlvdXQ+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9InByb2R1Y3RfdHlwZSI+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPnByb2R1Y3QgdHlwZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+cHJvZHVjdCB0eXBlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgPHN0cmluZz5wcm9kdWN0IHR5cGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+cHJvZHVjdCB0eXBlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgPHN0cmluZz5wcm9kdWN0IHR5cGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgPGl0ZW0gcm93PSI4IiBjb2x1bW49IjAiPgogICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUURvdWJsZVNwaW5Cb3giIG5hbWU9Iml0ZW1fd2VpZ2h0Ij4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+aXRlbV93ZWlnaHQ8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPml0ZW1fd2VpZ2h0PC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgPHN0cmluZz5pdGVtX3dlaWdodDwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgPHN0cmluZz5pdGVtX3dlaWdodDwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+aXRlbV93ZWlnaHQ8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJtYXhpbXVtIj4KICAgICAgICAgICAgICAgPGRvdWJsZT4xMDAwMDAuMDAwMDAwMDAwMDAwMDAwPC9kb3VibGU+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic2luZ2xlU3RlcCI+CiAgICAgICAgICAgICAgIDxkb3VibGU+MC4wMTAwMDAwMDAwMDAwMDA8L2RvdWJsZT4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgPGl0ZW0gcm93PSI4IiBjb2x1bW49IjEiPgogICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJpdGVtX3dlaWdodF91bml0Ij4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+aXRlbV93ZWlnaHRfdW5pdDwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+aXRlbV93ZWlnaHRfdW5pdDwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+aXRlbV93ZWlnaHRfdW5pdDwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgPHN0cmluZz5pdGVtX3dlaWdodF91bml0PC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgPHN0cmluZz5pdGVtX3dlaWdodF91bml0PC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iOCIgY29sdW1uPSIyIj4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFEb3VibGVTcGluQm94IiBuYW1lPSJwcmljZSI+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPnByaWNlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz5wcmljZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+cHJpY2U8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+cHJpY2U8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICA8c3RyaW5nPnByaWNlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ibWF4aW11bSI+CiAgICAgICAgICAgICAgIDxkb3VibGU+MTAwMDAwLjAwMDAwMDAwMDAwMDAwMDwvZG91YmxlPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InNpbmdsZVN0ZXAiPgogICAgICAgICAgICAgICA8ZG91YmxlPjAuMDEwMDAwMDAwMDAwMDAwPC9kb3VibGU+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iOCIgY29sdW1uPSIzIj4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFEb3VibGVTcGluQm94IiBuYW1lPSJvdGhlcl9mcmFtZV9zaXplX2RpYW1ldGVyIj4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+b3RoZXJfZnJhbWVfc2l6ZV9kaWFtZXRlcjwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+b3RoZXJfZnJhbWVfc2l6ZV9kaWFtZXRlcjwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+b3RoZXJfZnJhbWVfc2l6ZV9kaWFtZXRlcjwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgPHN0cmluZz5vdGhlcl9mcmFtZV9zaXplX2RpYW1ldGVyPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgPHN0cmluZz5vdGhlcl9mcmFtZV9zaXplX2RpYW1ldGVyPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ibWF4aW11bSI+CiAgICAgICAgICAgICAgIDxkb3VibGU+MTAwMDAwMC4wMDAwMDAwMDAwMDAwMDA8L2RvdWJsZT4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgPGl0ZW0gcm93PSI4IiBjb2x1bW49IjQiPgogICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJvdGhlcl9mcmFtZV9zaXplX2RpYW1ldGVyX3VuaXQiPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz5vdGhlcl9mcmFtZV9zaXplX2RpYW1ldGVyX3VuaXQ8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPm90aGVyX2ZyYW1lX3NpemVfZGlhbWV0ZXJfdW5pdDwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+b3RoZXJfZnJhbWVfc2l6ZV9kaWFtZXRlcl91bml0PC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICA8c3RyaW5nPm90aGVyX2ZyYW1lX3NpemVfZGlhbWV0ZXJfdW5pdDwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+b3RoZXJfZnJhbWVfc2l6ZV9kaWFtZXRlcl91bml0PC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSIzIj4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0iY2VudGVyX2lubmVyX3Byb2ZpbGUiPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz5jZW50ZXIgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+Y2VudGVyIGlubmVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICA8c3RyaW5nPmNlbnRlciBpbm5lciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICA8c3RyaW5nPmNlbnRlciBpbm5lciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgPHN0cmluZz5jZW50ZXIgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMyI+CiAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9Imhhc19nbGFzcyI+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPmhhcyBnbGFzczwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+aGFzIGdsYXNzPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgPHN0cmluZz5oYXMgZ2xhc3M8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+aGFzIGdsYXNzPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgPHN0cmluZz5oYXMgZ2xhc3M8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjQiPgogICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJjYW5faG9sZF9jYW52YXMiPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz5jYW4gaG9sZCBjYW52YXM8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPmNhbiBob2xkIGNhbnZhczwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+Y2FuIGhvbGQgY2FudmFzPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICA8c3RyaW5nPmNhbiBob2xkIGNhbnZhczwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+Y2FuIGhvbGQgY2FudmFzPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSI1Ij4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0iaGFzX2NhbnZhcyI+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPmhhcyBjYW52YXM8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPmhhcyBjYW52YXM8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICA8c3RyaW5nPmhhcyBjYW52YXM8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+aGFzIGNhbnZhczwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+aGFzIGNhbnZhczwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iNiI+CiAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9Im9yaWVudGF0aW9uIj4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+b3JpZW50YXRpb248L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPm9yaWVudGF0aW9uPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgPHN0cmluZz5vcmllbnRhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgPHN0cmluZz5vcmllbnRhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+b3JpZW50YXRpb248L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjciPgogICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJ3b29kX3R5cGUiPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz53b29kIHR5cGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPndvb2QgdHlwZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+d29vZCB0eXBlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICA8c3RyaW5nPndvb2QgdHlwZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+d29vZCB0eXBlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSI4Ij4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0iZnJhbWVfc2hhcGUiPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz5mcmFtZV9zaGFwZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJhbWVfc2hhcGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICA8c3RyaW5nPmZyYW1lX3NoYXBlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICA8c3RyaW5nPmZyYW1lX3NoYXBlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgPHN0cmluZz5mcmFtZV9zaGFwZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICA8aXRlbSByb3c9IjExIiBjb2x1bW49IjEiIGNvbHNwYW49IjgiPgogICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUxpbmVFZGl0IiBuYW1lPSJza3UiPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz5za3U8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPnNrdTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c2t1PC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICA8c3RyaW5nPnNrdTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c2t1PC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZHJhZ0VuYWJsZWQiPgogICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InBsYWNlaG9sZGVyVGV4dCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c2t1PC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iY2xlYXJCdXR0b25FbmFibGVkIj4KICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgPGl0ZW0gcm93PSIxMSIgY29sdW1uPSIwIj4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJuZXdfc2t1Ij4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+Z2VuZXJhdGUgYSBuZXcgc2t1PC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz5nZW5lcmF0ZSBhIG5ldyBza3U8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICA8c3RyaW5nPmdlbmVyYXRlIGEgbmV3IHNrdTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgPHN0cmluZz5nZW5lcmF0ZSBhIG5ldyBza3U8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICA8c3RyaW5nPmdlbmVyYXRlIGEgbmV3IHNrdTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICA8c3RyaW5nPk5ldyBTS1U8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgPGl0ZW0gcm93PSIxMCIgY29sdW1uPSIxIiBjb2xzcGFuPSI4Ij4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFMaW5lRWRpdCIgbmFtZT0ic29sZF90byI+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPnNvbGQgdG88L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPnNvbGQgdG88L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICA8c3RyaW5nPnNvbGQgdG88L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c29sZCB0bzwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c29sZCB0bzwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImRyYWdFbmFibGVkIj4KICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFjZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICA8c3RyaW5nPnNvbGQgdG88L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJjbGVhckJ1dHRvbkVuYWJsZWQiPgogICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICA8aXRlbSByb3c9IjEwIiBjb2x1bW49IjAiPgogICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJzb2xkIj4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c29sZDwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c29sZDwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c29sZDwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgPHN0cmluZz5zb2xkPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgPHN0cmluZz5zb2xkPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSI0Ij4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0iY2VudGVyX291dGVyX3Byb2ZpbGUiPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz5jZW50ZXIgb3V0ZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+Y2VudGVyIG91dGVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICA8c3RyaW5nPmNlbnRlciBvdXRlciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICA8c3RyaW5nPmNlbnRlciBvdXRlciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgPHN0cmluZz5jZW50ZXIgb3V0ZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICA8aXRlbSByb3c9IjEiIGNvbHVtbj0iNSI+CiAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9ImZpbmlzaF90eXBlIj4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+ZmluaXNoIHR5cGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPmZpbmlzaCB0eXBlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgPHN0cmluZz5maW5pc2ggdHlwZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgPHN0cmluZz5maW5pc2ggdHlwZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+ZmluaXNoIHR5cGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjYiPgogICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJzdGFja2FibGUiPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz5zdGFja2FibGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPnN0YWNrYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c3RhY2thYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICA8c3RyaW5nPnN0YWNrYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c3RhY2thYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iOSIgY29sdW1uPSIxIiBjb2xzcGFuPSI4Ij4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFMaW5lRWRpdCIgbmFtZT0ic3RhaW4iPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz5zdGFpbjwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c3RhaW48L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICA8c3RyaW5nPnN0YWluPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICA8c3RyaW5nPnN0YWluPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgPHN0cmluZz5zdGFpbjwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImRyYWdFbmFibGVkIj4KICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFjZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICA8c3RyaW5nPnN0YWluPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iY2xlYXJCdXR0b25FbmFibGVkIj4KICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgPGl0ZW0gcm93PSI5IiBjb2x1bW49IjAiPgogICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJzdGFpbmFibGUiPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz5zdGFpbmFibGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPnN0YWluYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c3RhaW5hYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICA8c3RyaW5nPnN0YWluYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c3RhaW5hYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iOCIgY29sdW1uPSI1Ij4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0icGFpZF9mb3IiPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz53YXMgaXQgcGFpZCBmb3I8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPndhcyBpdCBwYWlkIGZvcjwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+d2FzIGl0IHBhaWQgZm9yPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICA8c3RyaW5nPndhcyBpdCBwYWlkIGZvcjwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+d2FzIGl0IHBhaWQgZm9yPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iOCIgY29sdW1uPSI2Ij4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFEb3VibGVTcGluQm94IiBuYW1lPSJhbW91bnRfcGFpZCI+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPmFtb3VudCBwYWlkIHdpdGg8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPmFtb3VudCBwYWlkIHdpdGg8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICA8c3RyaW5nPmFtb3VudCBwYWlkIHdpdGg8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+YW1vdW50IHBhaWQgd2l0aDwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+YW1vdW50IHBhaWQgd2l0aDwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgIDwvbGF5b3V0PgogICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgIDwvaXRlbT4KICAgICAgICA8aXRlbSByb3c9IjIiIGNvbHVtbj0iMCIgY29sc3Bhbj0iMiI+CiAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJzYXZlX25ld19wcm9kdWN0Ij4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICA8c3RyaW5nPlNhdmUgTmV3IFByb2R1Y3Q8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgIDwvaXRlbT4KICAgICAgIDwvbGF5b3V0PgogICAgICA8L3dpZGdldD4KICAgICAgPHdpZGdldCBjbGFzcz0iUVdpZGdldCIgbmFtZT0idGFiXzIiPgogICAgICAgPGF0dHJpYnV0ZSBuYW1lPSJ0aXRsZSI+CiAgICAgICAgPHN0cmluZz5TZWFyY2g8L3N0cmluZz4KICAgICAgIDwvYXR0cmlidXRlPgogICAgICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRMYXlvdXRfOSI+CiAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjAiPgogICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRU2Nyb2xsQXJlYSIgbmFtZT0ic2Nyb2xsQXJlYV8zIj4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aWRnZXRSZXNpemFibGUiPgogICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVdpZGdldCIgbmFtZT0ic2Nyb2xsQXJlYVdpZGdldENvbnRlbnRzXzMiPgogICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJnZW9tZXRyeSI+CiAgICAgICAgICAgIDxyZWN0PgogICAgICAgICAgICAgPHg+MDwveD4KICAgICAgICAgICAgIDx5PjA8L3k+CiAgICAgICAgICAgICA8d2lkdGg+MTEyMjwvd2lkdGg+CiAgICAgICAgICAgICA8aGVpZ2h0PjY0MTwvaGVpZ2h0PgogICAgICAgICAgICA8L3JlY3Q+CiAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICA8bGF5b3V0IGNsYXNzPSJRR3JpZExheW91dCIgbmFtZT0iZ3JpZExheW91dF8xNyI+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIwIiByb3dzcGFuPSIyIiBjb2xzcGFuPSIyIj4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFTY3JvbGxBcmVhIiBuYW1lPSJzY3JvbGxBcmVhXzUiPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aWRnZXRSZXNpemFibGUiPgogICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVdpZGdldCIgbmFtZT0ic2Nyb2xsQXJlYVdpZGdldENvbnRlbnRzXzUiPgogICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZ2VvbWV0cnkiPgogICAgICAgICAgICAgICAgPHJlY3Q+CiAgICAgICAgICAgICAgICAgPHg+MDwveD4KICAgICAgICAgICAgICAgICA8eT4wPC95PgogICAgICAgICAgICAgICAgIDx3aWR0aD4zMzQ8L3dpZHRoPgogICAgICAgICAgICAgICAgIDxoZWlnaHQ+MTI1OTwvaGVpZ2h0PgogICAgICAgICAgICAgICAgPC9yZWN0PgogICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICA8bGF5b3V0IGNsYXNzPSJRR3JpZExheW91dCIgbmFtZT0iZ3JpZExheW91dF8xMCI+CiAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjIzIiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFMaW5lRWRpdCIgbmFtZT0ic2t1XzIiPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnNrdTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c2t1PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5za3U8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c2t1PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5za3U8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImRyYWdFbmFibGVkIj4KICAgICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFjZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5za3U8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImNsZWFyQnV0dG9uRW5hYmxlZCI+CiAgICAgICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxMCIgY29sdW1uPSIwIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9ImZyb250X2lubmVyX3Byb2ZpbGVfMiI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJvbnQgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJvbnQgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJvbnQgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5mcm9udCBpbm5lciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5mcm9udCBpbm5lciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjEiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJwcm9kdWN0X3R5cGVfMiI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+cHJvZHVjdCB0eXBlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5wcm9kdWN0IHR5cGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnByb2R1Y3QgdHlwZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5wcm9kdWN0IHR5cGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnByb2R1Y3QgdHlwZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIyOCIgY29sdW1uPSIwIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9InBhaWRfZm9yXzIiPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnBhaWQgZm9yIHllcy9ubzwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+cGFpZCBmb3IgeWVzL25vPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5wYWlkIGZvciB5ZXMvbm88L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+cGFpZCBmb3IgeWVzL25vPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5wYWlkIGZvciB5ZXMvbm88L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iOCIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ2hlY2tCb3giIG5hbWU9Imhhc19nbGFzc19jIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5FbmFibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMTkiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJvdGhlcl9mcmFtZV9zaXplX2RpYW1ldGVyX3VuaXRfMiI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+b3RoZXJfZnJhbWVfc2l6ZV9kaWFtZXRlcl91bml0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5vdGhlcl9mcmFtZV9zaXplX2RpYW1ldGVyX3VuaXQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPm90aGVyX2ZyYW1lX3NpemVfZGlhbWV0ZXJfdW5pdDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5vdGhlcl9mcmFtZV9zaXplX2RpYW1ldGVyX3VuaXQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPm90aGVyX2ZyYW1lX3NpemVfZGlhbWV0ZXJfdW5pdDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxOSIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ2hlY2tCb3giIG5hbWU9Im90aGVyX2ZyYW1lX3NpemVfZGlhbWV0ZXJfdW5pdF9jIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5FbmFibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMjEiIGNvbHVtbj0iMSI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNoZWNrQm94IiBuYW1lPSJzdGFpbl9jIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5FbmFibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMTMiIGNvbHVtbj0iMSI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNoZWNrQm94IiBuYW1lPSJmcmFtZV9zaGFwZV9jIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5FbmFibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMjYiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJzb2xkXzIiPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnNvbGQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnNvbGQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnNvbGQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c29sZDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c29sZDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSI1IiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0iaGFzX2NhbnZhc18yIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5oYXMgY2FudmFzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5oYXMgY2FudmFzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5oYXMgY2FudmFzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmhhcyBjYW52YXM8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmhhcyBjYW52YXM8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMjQiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJzdGFpbmFibGVfMiI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c3RhaW5hYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5zdGFpbmFibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnN0YWluYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5zdGFpbmFibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnN0YWluYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIyMSIgY29sdW1uPSIwIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRTGluZUVkaXQiIG5hbWU9InN0YWluXzIiPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnN0YWluPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5zdGFpbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c3RhaW48L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c3RhaW48L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnN0YWluPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJkcmFnRW5hYmxlZCI+CiAgICAgICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0icGxhY2Vob2xkZXJUZXh0Ij4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c3RhaW48L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImNsZWFyQnV0dG9uRW5hYmxlZCI+CiAgICAgICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxNiIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ2hlY2tCb3giIG5hbWU9InByaWNlX2MiPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkVuYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxNSIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ2hlY2tCb3giIG5hbWU9ImZyb250X291dGVyX3Byb2ZpbGVfYyI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RW5hYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJjYW5faG9sZF9nbGFzc18yIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5jYW4gaG9sZCBnbGFzczwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+Y2FuIGhvbGQgZ2xhc3M8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmNhbiBob2xkIGdsYXNzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmNhbiBob2xkIGdsYXNzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5jYW4gaG9sZCBnbGFzczwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxNCIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ2hlY2tCb3giIG5hbWU9InN0YWNrYWJsZV9jIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5FbmFibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMTIiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJjZW50ZXJfaW5uZXJfcHJvZmlsZV8yIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5jZW50ZXIgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+Y2VudGVyIGlubmVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmNlbnRlciBpbm5lciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmNlbnRlciBpbm5lciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5jZW50ZXIgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSI0IiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0iZmluaXNoX3R5cGVfMiI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZmluaXNoIHR5cGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmZpbmlzaCB0eXBlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5maW5pc2ggdHlwZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5maW5pc2ggdHlwZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZmluaXNoIHR5cGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMTgiIGNvbHVtbj0iMSI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNoZWNrQm94IiBuYW1lPSJvdGhlcl9mcmFtZV9zaXplX2RpYW1ldGVyX2MiPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkVuYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIyNiIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ2hlY2tCb3giIG5hbWU9InNvbGRfYyI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RW5hYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjI1IiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFEb3VibGVTcGluQm94IiBuYW1lPSJpdGVtX3dlaWdodF8yIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5pdGVtX3dlaWdodDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+aXRlbV93ZWlnaHQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPml0ZW1fd2VpZ2h0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPml0ZW1fd2VpZ2h0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5pdGVtX3dlaWdodDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ibWF4aW11bSI+CiAgICAgICAgICAgICAgICAgICA8ZG91YmxlPjEwMDAwMC4wMDAwMDAwMDAwMDAwMDA8L2RvdWJsZT4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InNpbmdsZVN0ZXAiPgogICAgICAgICAgICAgICAgICAgPGRvdWJsZT4wLjAxMDAwMDAwMDAwMDAwMDwvZG91YmxlPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIyNSIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ2hlY2tCb3giIG5hbWU9Iml0ZW1fd2VpZ2h0X2MiPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkVuYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSI3IiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0id29vZF90eXBlXzIiPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPndvb2QgdHlwZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+d29vZCB0eXBlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz53b29kIHR5cGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+d29vZCB0eXBlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz53b29kIHR5cGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iOSIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ2hlY2tCb3giIG5hbWU9InJlYXJfaW5uZXJfcHJvZmlsZV9jIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5FbmFibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMTIiIGNvbHVtbj0iMSI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNoZWNrQm94IiBuYW1lPSJjZW50ZXJfaW5uZXJfcHJvZmlsZV9jIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5FbmFibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ2hlY2tCb3giIG5hbWU9ImNhbl9ob2xkX2dsYXNzX2MiPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkVuYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxMSIgY29sdW1uPSIwIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9ImNlbnRlcl9vdXRlcl9wcm9maWxlXzIiPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmNlbnRlciBvdXRlciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5jZW50ZXIgb3V0ZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+Y2VudGVyIG91dGVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+Y2VudGVyIG91dGVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmNlbnRlciBvdXRlciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjciIGNvbHVtbj0iMSI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNoZWNrQm94IiBuYW1lPSJ3b29kX3R5cGVfYyI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RW5hYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjE4IiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFEb3VibGVTcGluQm94IiBuYW1lPSJvdGhlcl9mcmFtZV9zaXplX2RpYW1ldGVyXzIiPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPm90aGVyX2ZyYW1lX3NpemVfZGlhbWV0ZXI8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPm90aGVyX2ZyYW1lX3NpemVfZGlhbWV0ZXI8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPm90aGVyX2ZyYW1lX3NpemVfZGlhbWV0ZXI8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+b3RoZXJfZnJhbWVfc2l6ZV9kaWFtZXRlcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+b3RoZXJfZnJhbWVfc2l6ZV9kaWFtZXRlcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ibWF4aW11bSI+CiAgICAgICAgICAgICAgICAgICA8ZG91YmxlPjEwMDAwMDAuMDAwMDAwMDAwMDAwMDAwPC9kb3VibGU+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjIwIiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQbGFpblRleHRFZGl0IiBuYW1lPSJjb21tZW50c18yIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5jb21tZW50czwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+Y29tbWVudHM8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmNvbW1lbnRzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmNvbW1lbnRzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5jb21tZW50czwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGFiQ2hhbmdlc0ZvY3VzIj4KICAgICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFjZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5jb21tZW50czwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxMSIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ2hlY2tCb3giIG5hbWU9ImNlbnRlcl9vdXRlcl9wcm9maWxlX2MiPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkVuYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSI2IiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0ib3JpZW50YXRpb25fMiI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+b3JpZW50YXRpb248L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPm9yaWVudGF0aW9uPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5vcmllbnRhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5vcmllbnRhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+b3JpZW50YXRpb248L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iNCIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ2hlY2tCb3giIG5hbWU9ImZpbmlzaF90eXBlX2MiPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkVuYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSI2IiBjb2x1bW49IjEiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDaGVja0JveCIgbmFtZT0ib3JpZW50YXRpb25fYyI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RW5hYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjE3IiBjb2x1bW49IjEiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDaGVja0JveCIgbmFtZT0iaXRlbV93ZWlnaHRfdW5pdF9jIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5FbmFibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMTYiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUURvdWJsZVNwaW5Cb3giIG5hbWU9InByaWNlXzIiPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnByaWNlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5wcmljZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+cHJpY2U8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+cHJpY2U8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnByaWNlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJtYXhpbXVtIj4KICAgICAgICAgICAgICAgICAgIDxkb3VibGU+MTAwMDAwLjAwMDAwMDAwMDAwMDAwMDwvZG91YmxlPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic2luZ2xlU3RlcCI+CiAgICAgICAgICAgICAgICAgICA8ZG91YmxlPjAuMDEwMDAwMDAwMDAwMDAwPC9kb3VibGU+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjgiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJoYXNfZ2xhc3NfMiI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+aGFzIGdsYXNzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5oYXMgZ2xhc3M8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmhhcyBnbGFzczwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5oYXMgZ2xhc3M8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmhhcyBnbGFzczwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxMCIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ2hlY2tCb3giIG5hbWU9ImZyb250X2lubmVyX3Byb2ZpbGVfYyI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RW5hYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjE1IiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0iZnJvbnRfb3V0ZXJfcHJvZmlsZV8yIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5mcm9udCBvdXRlciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5mcm9udCBvdXRlciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5mcm9udCBvdXRlciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmZyb250IG91dGVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmZyb250IG91dGVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMjMiIGNvbHVtbj0iMSI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNoZWNrQm94IiBuYW1lPSJza3VfYyI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RW5hYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjEiIGNvbHVtbj0iMSI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNoZWNrQm94IiBuYW1lPSJwcm9kdWN0X3R5cGVfYyI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RW5hYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjEzIiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0iZnJhbWVfc2hhcGVfMiI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJhbWVfc2hhcGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmZyYW1lX3NoYXBlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5mcmFtZV9zaGFwZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5mcmFtZV9zaGFwZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJhbWVfc2hhcGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMTQiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJzdGFja2FibGVfMiI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c3RhY2thYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5zdGFja2FibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnN0YWNrYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5zdGFja2FibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnN0YWNrYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSI1IiBjb2x1bW49IjEiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDaGVja0JveCIgbmFtZT0iaGFzX2NhbnZhc19jIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5FbmFibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMjIiIGNvbHVtbj0iMSI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNoZWNrQm94IiBuYW1lPSJzb2xkX3RvX2MiPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkVuYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIyIiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0ic2l6ZV8yIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5zaXplPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5zaXplPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5zaXplPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnNpemU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnNpemU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMjIiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUxpbmVFZGl0IiBuYW1lPSJzb2xkX3RvXzIiPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnNvbGQgdG88L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnNvbGQgdG88L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnNvbGQgdG88L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c29sZCB0bzwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c29sZCB0bzwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZHJhZ0VuYWJsZWQiPgogICAgICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InBsYWNlaG9sZGVyVGV4dCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnNvbGQgdG88L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImNsZWFyQnV0dG9uRW5hYmxlZCI+CiAgICAgICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIyNCIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ2hlY2tCb3giIG5hbWU9InN0YWluYWJsZV9jIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5FbmFibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMiIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ2hlY2tCb3giIG5hbWU9InNpemVfYyI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RW5hYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjIwIiBjb2x1bW49IjEiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDaGVja0JveCIgbmFtZT0iY29tbWVudHNfYyI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RW5hYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjE3IiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0iaXRlbV93ZWlnaHRfdW5pdF8yIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5pdGVtX3dlaWdodF91bml0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5pdGVtX3dlaWdodF91bml0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5pdGVtX3dlaWdodF91bml0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPml0ZW1fd2VpZ2h0X3VuaXQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPml0ZW1fd2VpZ2h0X3VuaXQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iOSIgY29sdW1uPSIwIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9InJlYXJfaW5uZXJfcHJvZmlsZV8yIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5yZWFyIGlubmVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnJlYXIgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+cmVhciBpbm5lciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnJlYXIgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+cmVhciBpbm5lciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjI3IiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0iY3VzdG9tX2VuZ3JhdmVkXzIiLz4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMyIgY29sdW1uPSIwIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9ImNhbl9ob2xkX2NhbnZhc18yIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5jYW4gaG9sZCBjYW52YXM8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmNhbiBob2xkIGNhbnZhczwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+Y2FuIGhvbGQgY2FudmFzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmNhbiBob2xkIGNhbnZhczwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+Y2FuIGhvbGQgY2FudmFzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjMiIGNvbHVtbj0iMSI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNoZWNrQm94IiBuYW1lPSJjYW5faG9sZF9jYW52YXNfYyI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RW5hYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjI3IiBjb2x1bW49IjEiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDaGVja0JveCIgbmFtZT0iY3VzdG9tX2VuZ3JhdmVkX2MiPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkVuYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIyOSIgY29sdW1uPSIwIj4KICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRRG91YmxlU3BpbkJveCIgbmFtZT0iYW1vdW50X3BhaWRfMiI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YW1vdW50IHBhaWQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmFtb3VudCBwYWlkPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5hbW91bnQgcGFpZDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5hbW91bnQgcGFpZDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YW1vdW50IHBhaWQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMjgiIGNvbHVtbj0iMSI+CiAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNoZWNrQm94IiBuYW1lPSJwYWlkX2Zvcl9jIj4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5FbmFibGVkPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjI5IiBjb2x1bW49IjEiPgogICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDaGVja0JveCIgbmFtZT0iYW1vdW50X3BhaWRfYyI+CiAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RW5hYmxlZDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICA8L2xheW91dD4KICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIyIj4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFMaXN0V2lkZ2V0IiBuYW1lPSJyZXN1bHRzIi8+CiAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICA8L2xheW91dD4KICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICA8L3dpZGdldD4KICAgICAgICA8L2l0ZW0+CiAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjAiPgogICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0ic2VhcmNoIj4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICA8c3RyaW5nPlNlYXJjaDwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgPC9pdGVtPgogICAgICAgPC9sYXlvdXQ+CiAgICAgIDwvd2lkZ2V0PgogICAgICA8d2lkZ2V0IGNsYXNzPSJRV2lkZ2V0IiBuYW1lPSJ0YWJfMyI+CiAgICAgICA8YXR0cmlidXRlIG5hbWU9InRpdGxlIj4KICAgICAgICA8c3RyaW5nPlNldHRpbmdzPC9zdHJpbmc+CiAgICAgICA8L2F0dHJpYnV0ZT4KICAgICAgIDxsYXlvdXQgY2xhc3M9IlFHcmlkTGF5b3V0IiBuYW1lPSJncmlkTGF5b3V0XzgiPgogICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIwIj4KICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVNjcm9sbEFyZWEiIG5hbWU9InNjcm9sbEFyZWFfMiI+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2lkZ2V0UmVzaXphYmxlIj4KICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFXaWRnZXQiIG5hbWU9InNjcm9sbEFyZWFXaWRnZXRDb250ZW50c18yIj4KICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZ2VvbWV0cnkiPgogICAgICAgICAgICA8cmVjdD4KICAgICAgICAgICAgIDx4PjA8L3g+CiAgICAgICAgICAgICA8eT4wPC95PgogICAgICAgICAgICAgPHdpZHRoPjExMjI8L3dpZHRoPgogICAgICAgICAgICAgPGhlaWdodD42NDE8L2hlaWdodD4KICAgICAgICAgICAgPC9yZWN0PgogICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgPGxheW91dCBjbGFzcz0iUVZCb3hMYXlvdXQiIG5hbWU9InZlcnRpY2FsTGF5b3V0Ij4KICAgICAgICAgICAgPGl0ZW0+CiAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRTGluZUVkaXQiIG5hbWU9InRva2VuIj4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c2VydmVyIGFjY2VzcyB0b2tlbjwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c2VydmVyIGFjY2VzcyB0b2tlbjwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c2VydmVyIGFjY2VzcyB0b2tlbjwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgPHN0cmluZz5zZXJ2ZXIgYWNjZXNzIHRva2VuPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgPHN0cmluZz5zZXJ2ZXIgYWNjZXNzIHRva2VuPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZHJhZ0VuYWJsZWQiPgogICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InBsYWNlaG9sZGVyVGV4dCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+U2VydmVyIEF1dGhlbnRpY2F0aW9uIFRva2VuPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iY2xlYXJCdXR0b25FbmFibGVkIj4KICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgPGl0ZW0+CiAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRTGluZUVkaXQiIG5hbWU9InNlcnZlciI+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPnNlcnZlciBhZGRyZXNzPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz5zZXJ2ZXIgYWRkcmVzczwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c2VydmVyIGFkZHJlc3M8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c2VydmVyIGFkZHJlc3M8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICA8c3RyaW5nPnNlcnZlciBhZGRyZXNzPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+aHR0cDovLzEyNy4wLjAuMTo4MDAwPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZHJhZ0VuYWJsZWQiPgogICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InBsYWNlaG9sZGVyVGV4dCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c2VydmVyIGFkZHJlc3M8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJjbGVhckJ1dHRvbkVuYWJsZWQiPgogICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgIDwvbGF5b3V0PgogICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgIDwvaXRlbT4KICAgICAgICA8aXRlbSByb3c9IjEiIGNvbHVtbj0iMCI+CiAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJzYXZlX3NldHRpbmdzIj4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICA8c3RyaW5nPnNhdmUgc2V0dGluZ3M8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICA8c3RyaW5nPnNhdmUgc2V0dGluZ3M8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICA8c3RyaW5nPnNhdmUgc2V0dGluZ3M8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgIDxzdHJpbmc+c2F2ZSBzZXR0aW5nczwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgIDxzdHJpbmc+c2F2ZSBzZXR0aW5nczwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICA8c3RyaW5nPlNhdmUgU2V0dGluZ3M8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgIDwvaXRlbT4KICAgICAgIDwvbGF5b3V0PgogICAgICA8L3dpZGdldD4KICAgICAgPHdpZGdldCBjbGFzcz0iUVdpZGdldCIgbmFtZT0idGFiXzQiPgogICAgICAgPGF0dHJpYnV0ZSBuYW1lPSJ0aXRsZSI+CiAgICAgICAgPHN0cmluZz5Gb3JtYXQgRWRpdG9yPC9zdHJpbmc+CiAgICAgICA8L2F0dHJpYnV0ZT4KICAgICAgIDxhdHRyaWJ1dGUgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgPHN0cmluZz5tYWtlL2VkaXQgZGF0YSBmaWxlcyBpbiBDU1YvSlNPTi9QaWNrbGUvVGV4dDwvc3RyaW5nPgogICAgICAgPC9hdHRyaWJ1dGU+CiAgICAgICA8YXR0cmlidXRlIG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgPHN0cmluZz5tYWtlL2VkaXQgZGF0YSBmaWxlcyBpbiBDU1YvSlNPTi9QaWNrbGUvVGV4dDwvc3RyaW5nPgogICAgICAgPC9hdHRyaWJ1dGU+CiAgICAgICA8bGF5b3V0IGNsYXNzPSJRR3JpZExheW91dCIgbmFtZT0iZ3JpZExheW91dF8xMyI+CiAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjAiPgogICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRR3JvdXBCb3giIG5hbWU9Imdyb3VwQm94Ij4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0aXRsZSI+CiAgICAgICAgICAgPHN0cmluZz5TdG9yYWdlPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRMYXlvdXRfMTEiPgogICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIwIj4KICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUxpbmVFZGl0IiBuYW1lPSJmb3JtYXRFZGl0b3Jfc2F2ZUxvY2F0aW9uIj4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICA8c3RyaW5nPnNhdmUgbG9jYXRpb248L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICA8c3RyaW5nPnNhdmUgbG9jYXRpb248L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICA8c3RyaW5nPnNhdmUgbG9jYXRpb248L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgIDxzdHJpbmc+c2F2ZSBsb2NhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgIDxzdHJpbmc+c2F2ZSBsb2NhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJkcmFnRW5hYmxlZCI+CiAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0icGxhY2Vob2xkZXJUZXh0Ij4KICAgICAgICAgICAgICA8c3RyaW5nPnNhdmUvbG9jYXRpb248L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iY2xlYXJCdXR0b25FbmFibGVkIj4KICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIzIj4KICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9ImZvcm1hdEVkaXRvcl9zYXZlIj4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICA8c3RyaW5nPnNhdmU8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICA8c3RyaW5nPnNhdmU8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICA8c3RyaW5nPnNhdmU8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgIDxzdHJpbmc+c2F2ZTwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgIDxzdHJpbmc+c2F2ZTwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICA8c3RyaW5nPlNhdmU8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iNCI+CiAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJmb3JtYXRFZGl0b3JfZGVsZXRlIj4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICA8c3RyaW5nPmRlbGV0ZSB0aGUgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgIDxzdHJpbmc+ZGVsZXRlIHRoZSBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgPHN0cmluZz5kZWxldGUgdGhlIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgIDxzdHJpbmc+ZGVsZXRlIHRoZSBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgPHN0cmluZz5kZWxldGUgdGhlIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgPHN0cmluZz5EZWxldGU8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMiI+CiAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJmb3JtYXRFZGl0b3JfYnJvd3NlIj4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBmb3IgYSBzYXZlIGxvY2F0aW9uPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgZm9yIGEgc2F2ZSBsb2NhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGZvciBhIHNhdmUgbG9jYXRpb248L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGZvciBhIHNhdmUgbG9jYXRpb248L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBmb3IgYSBzYXZlIGxvY2F0aW9uPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgIDxzdHJpbmc+QnJvd3NlPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjUiPgogICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0iZm9ybWF0RWRpdG9yX3Rlc3RGaWxlIj4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICA8c3RyaW5nPnRlc3QgZmlsZSBmb3IgZXJyb3JzPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgPHN0cmluZz50ZXN0IGZpbGUgZm9yIGVycm9yczwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgIDxzdHJpbmc+dGVzdCBmaWxlIGZvciBlcnJvcnM8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgIDxzdHJpbmc+dGVzdCBmaWxlIGZvciBlcnJvcnM8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICA8c3RyaW5nPnRlc3QgZmlsZSBmb3IgZXJyb3JzPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgIDxzdHJpbmc+VGVzdCBGaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjEiPgogICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9ImZvcm1hdEVkaXRvcl9jb250ZW50Rm9ybWF0Ij4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICA8c3RyaW5nPmNvbnRlbnQgZm9ybWF0IHRvIHNhdmUgdG88L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICA8c3RyaW5nPmNvbnRlbnQgZm9ybWF0IHRvIHNhdmUgdG88L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICA8c3RyaW5nPnRoaXMgd2lsbCBhdHRlbXB0IHRvIHBhcnNlIHRoZSBkYXRhIGluIHRoZSBlZGl0b3Igd2l0aCB0aGUgYXBwcm9wcmlhdGUgZGF0YSB0eXBlIGZvcm1hdCBhbmQgc2F2ZSBpdCB0byBkaXNrIGZvciB1c2Ugd2l0aCBpbXBvcnQvZXhwb3J0IG9yIE9DUjwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgPHN0cmluZz5jb250ZW50IGZvcm1hdCB0byBzYXZlIHRvPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgPHN0cmluZz50aGlzIHdpbGwgYXR0ZW1wdCB0byBwYXJzZSB0aGUgZGF0YSBpbiB0aGUgZWRpdG9yIHdpdGggdGhlIGFwcHJvcHJpYXRlIGRhdGEgdHlwZSBmb3JtYXQgYW5kIHNhdmUgaXQgdG8gZGlzayBmb3IgdXNlIHdpdGggaW1wb3J0L2V4cG9ydCBvciBPQ1I8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8aXRlbT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+Q1NWPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgIDxpdGVtPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgPHN0cmluZz5KU09OPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgIDxpdGVtPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgPHN0cmluZz5QTkc8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgPGl0ZW0+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICA8c3RyaW5nPio8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjEiPgogICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9ImZvcm1hdEVkaXRvcl9wbmdPcHRpb25zIj4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICA8c3RyaW5nPmltYWdlIG9wdGlvbnM8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICA8c3RyaW5nPmltYWdlIG9wdGlvbnM8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICA8c3RyaW5nPmltYWdlIG9wdGlvbnM8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgIDxzdHJpbmc+aW1hZ2Ugb3B0aW9uczwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgIDxzdHJpbmc+aW1hZ2Ugb3B0aW9uczwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxpdGVtPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgPHN0cmluZz5QbGFpbjwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICA8aXRlbT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+UVI8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgPGl0ZW0+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICA8c3RyaW5nPkNvZGUxMjg8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICA8L2xheW91dD4KICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgPC9pdGVtPgogICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSIwIj4KICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUdyb3VwQm94IiBuYW1lPSJncm91cEJveF81Ij4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0aXRsZSI+CiAgICAgICAgICAgPHN0cmluZz5FZGl0b3I8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8bGF5b3V0IGNsYXNzPSJRR3JpZExheW91dCIgbmFtZT0iZ3JpZExheW91dF8xMiI+CiAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjAiPgogICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0iZm9ybWF0RWRpdG9yX3Rlc3RDb250ZW50Ij4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICA8c3RyaW5nPnRlc3QgZWRpdG9yIGNvbnRlbnQgZm9yIGVycm9yczwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgIDxzdHJpbmc+dGVzdCBlZGl0b3IgY29udGVudCBmb3IgZXJyb3JzPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgPHN0cmluZz50ZXN0IGVkaXRvciBjb250ZW50IGZvciBlcnJvcnM8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgIDxzdHJpbmc+dGVzdCBlZGl0b3IgY29udGVudCBmb3IgZXJyb3JzPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgPHN0cmluZz50ZXN0IGVkaXRvciBjb250ZW50IGZvciBlcnJvcnM8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgPHN0cmluZz5UZXN0IENvbnRlbnQ8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICA8aXRlbSByb3c9IjEiIGNvbHVtbj0iMSI+CiAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJmb3JtYXRFZGl0b3JfcmFuZG9tRGF0YSI+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ibWF4aW11bVNpemUiPgogICAgICAgICAgICAgIDxzaXplPgogICAgICAgICAgICAgICA8d2lkdGg+MTIwPC93aWR0aD4KICAgICAgICAgICAgICAgPGhlaWdodD4xNjc3NzIxNTwvaGVpZ2h0PgogICAgICAgICAgICAgIDwvc2l6ZT4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgPHN0cmluZz5nZW5lcmF0ZSByYW5kb20gZGF0YTwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgIDxzdHJpbmc+Z2VuZXJhdGUgcmFuZG9tIGRhdGE8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICA8c3RyaW5nPmdlbmVyYXRlIHJhbmRvbSBkYXRhPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICA8c3RyaW5nPmdlbmVyYXRlIHJhbmRvbSBkYXRhPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgPHN0cmluZz5nZW5lcmF0ZSByYW5kb20gZGF0YTwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICA8c3RyaW5nPlJhbmRvbSBEYXRhPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjIiPgogICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRU3BpbkJveCIgbmFtZT0iZm9ybWF0RWRpdG9yX3JkU2l6ZSI+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ibWF4aW11bVNpemUiPgogICAgICAgICAgICAgIDxzaXplPgogICAgICAgICAgICAgICA8d2lkdGg+MTAwPC93aWR0aD4KICAgICAgICAgICAgICAgPGhlaWdodD4xNjc3NzIxNTwvaGVpZ2h0PgogICAgICAgICAgICAgIDwvc2l6ZT4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgPHN0cmluZz5zaXplIG9mIHJhbmRvbSBkYXRhIHRvIHVzZTwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgIDxzdHJpbmc+c2l6ZSBvZiByYW5kb20gZGF0YSB0byB1c2U8L3N0cmluZz4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICA8c3RyaW5nPnNpemUgb2YgcmFuZG9tIGRhdGEgdG8gdXNlPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICA8c3RyaW5nPnNpemUgb2YgcmFuZG9tIGRhdGEgdG8gdXNlPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgPHN0cmluZz5zaXplIG9mIHJhbmRvbSBkYXRhIHRvIHVzZTwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3cmFwcGluZyI+CiAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ibWF4aW11bSI+CiAgICAgICAgICAgICAgPG51bWJlcj40MDk2PC9udW1iZXI+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InNpbmdsZVN0ZXAiPgogICAgICAgICAgICAgIDxudW1iZXI+MTwvbnVtYmVyPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ2YWx1ZSI+CiAgICAgICAgICAgICAgPG51bWJlcj4zMjwvbnVtYmVyPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIwIiBjb2xzcGFuPSIzIj4KICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVBsYWluVGV4dEVkaXQiIG5hbWU9ImZvcm1hdEVkaXRvcl9lZGl0b3IiPgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgIDxzdHJpbmc+aW4gbWVtb3J5IGVkaXRvcjwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgIDxzdHJpbmc+aW4gbWVtb3J5IGVkaXRvcjwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgIDxzdHJpbmc+aW4gbWVtb3J5IGVkaXRvcjwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgPHN0cmluZz5pbiBtZW1vcnkgZWRpdG9yPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgPHN0cmluZz5pbiBtZW1vcnkgZWRpdG9yPC9zdHJpbmc+CiAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImRvY3VtZW50VGl0bGUiPgogICAgICAgICAgICAgIDxzdHJpbmc+Zm9ybWF0X2VkaXRvcjwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJvdmVyd3JpdGVNb2RlIj4KICAgICAgICAgICAgICA8Ym9vbD5mYWxzZTwvYm9vbD4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0icGxhY2Vob2xkZXJUZXh0Ij4KICAgICAgICAgICAgICA8c3RyaW5nPmNzdixkZWZhdWx0ZWQsY29sMTwvc3RyaW5nPgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgPC9sYXlvdXQ+CiAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgIDwvaXRlbT4KICAgICAgIDwvbGF5b3V0PgogICAgICA8L3dpZGdldD4KICAgICAgPHdpZGdldCBjbGFzcz0iUVdpZGdldCIgbmFtZT0idGFiXzUiPgogICAgICAgPGF0dHJpYnV0ZSBuYW1lPSJ0aXRsZSI+CiAgICAgICAgPHN0cmluZz5PQ1I8L3N0cmluZz4KICAgICAgIDwvYXR0cmlidXRlPgogICAgICAgPGF0dHJpYnV0ZSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICA8c3RyaW5nPmV4dHJhY3QgdGV4dCBmcm9tIGltYWdlczwvc3RyaW5nPgogICAgICAgPC9hdHRyaWJ1dGU+CiAgICAgICA8YXR0cmlidXRlIG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgPHN0cmluZz5leHRyYWN0IHRleHQgZnJvbSBpbWFnZXM8L3N0cmluZz4KICAgICAgIDwvYXR0cmlidXRlPgogICAgICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRMYXlvdXRfMTQiPgogICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIwIj4KICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVNjcm9sbEFyZWEiIG5hbWU9InNjcm9sbEFyZWFfNCI+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2lkZ2V0UmVzaXphYmxlIj4KICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFXaWRnZXQiIG5hbWU9InNjcm9sbEFyZWFXaWRnZXRDb250ZW50c180Ij4KICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZ2VvbWV0cnkiPgogICAgICAgICAgICA8cmVjdD4KICAgICAgICAgICAgIDx4PjA8L3g+CiAgICAgICAgICAgICA8eT4wPC95PgogICAgICAgICAgICAgPHdpZHRoPjExMjI8L3dpZHRoPgogICAgICAgICAgICAgPGhlaWdodD42ODM8L2hlaWdodD4KICAgICAgICAgICAgPC9yZWN0PgogICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRMYXlvdXRfMjAiPgogICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRR3JvdXBCb3giIG5hbWU9Imdyb3VwQm94XzYiPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0aXRsZSI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+RmlsZXN5c3RlbSBJbWFnZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRMYXlvdXRfMTUiPgogICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRTGluZUVkaXQiIG5hbWU9Im9jcl9sb2NhdGlvbiI+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmltYWdlIHBhdGg8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmltYWdlIHBhdGg8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmltYWdlIHBhdGg8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+aW1hZ2UgcGF0aDwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+aW1hZ2UgcGF0aDwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImRyYWdFbmFibGVkIj4KICAgICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFjZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmltYWdlIHRvIHByb2Nlc3M8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJjbGVhckJ1dHRvbkVuYWJsZWQiPgogICAgICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMSI+CiAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0ib2NyX2Jyb3dzZSI+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBmb3IgaW1hZ2VzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgZm9yIGltYWdlczwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGZvciBpbWFnZXM8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGZvciBpbWFnZXM8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBmb3IgaW1hZ2VzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+QnJvd3NlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJvY3Jfb3BlbiI+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPm9wZW4gZmlsZSBhbmQgcHJvY2VzcyBmb3IgdGV4dDwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+b3BlbiBmaWxlIGFuZCBwcm9jZXNzIGZvciB0ZXh0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5vcGVuIGZpbGUgYW5kIHByb2Nlc3MgZm9yIHRleHQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+b3BlbiBmaWxlIGFuZCBwcm9jZXNzIGZvciB0ZXh0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5vcGVuIGZpbGUgYW5kIHByb2Nlc3MgZm9yIHRleHQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5PcGVuPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPC9sYXlvdXQ+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMSIgY29sc3Bhbj0iMiI+CiAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRR3JvdXBCb3giIG5hbWU9Imdyb3VwQm94XzciPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0aXRsZSI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+RmlsZXN5c3RlbSBSZXN1bHRzPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8bGF5b3V0IGNsYXNzPSJRR3JpZExheW91dCIgbmFtZT0iZ3JpZExheW91dF8xNiI+CiAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIwIj4KICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFMaW5lRWRpdCIgbmFtZT0ib2NyX3NhdmVMb2NhdGlvbiI+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPnNhdmUgbG9jYXRpb248L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPnNhdmUgbG9jYXRpb248L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPnNhdmUgbG9jYXRpb248L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c2F2ZSBsb2NhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c2F2ZSBsb2NhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPnJlc3VsdC50eHQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJkcmFnRW5hYmxlZCI+CiAgICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0icGxhY2Vob2xkZXJUZXh0Ij4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5kYXRhL3RleHQgZmlsZSB0byBzYXZlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iY2xlYXJCdXR0b25FbmFibGVkIj4KICAgICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjEiPgogICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9Im9jcl9zYXZlQnJvd3NlIj4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIHNhdmUgbG9jYXRpb248L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBzYXZlIGxvY2F0aW9uPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2Ugc2F2ZSBsb2NhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2Ugc2F2ZSBsb2NhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIHNhdmUgbG9jYXRpb248L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5Ccm93c2U8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjEiPgogICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9Im9jcl9zYXZlIj4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c2F2ZSB0ZXh0IHJlc3VsdDwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c2F2ZSB0ZXh0IHJlc3VsdDwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c2F2ZSB0ZXh0IHJlc3VsdDwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5zYXZlIHRleHQgcmVzdWx0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5zYXZlIHRleHQgcmVzdWx0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+U2F2ZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgIDwvbGF5b3V0PgogICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjAiIGNvbHNwYW49IjIiPgogICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUdyb3VwQm94IiBuYW1lPSJncm91cEJveF84Ij4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGl0bGUiPgogICAgICAgICAgICAgICA8c3RyaW5nPlZpZXc8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxsYXlvdXQgY2xhc3M9IlFHcmlkTGF5b3V0IiBuYW1lPSJncmlkTGF5b3V0XzE4Ij4KICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUdyYXBoaWNzVmlldyIgbmFtZT0ib2NyX2ltYWdlVmlldyI+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmltYWdlIHByb2Nlc3NlZDwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+aW1hZ2UgcHJvY2Vzc2VkPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5pbWFnZSBwcm9jZXNzZWQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+aW1hZ2UgcHJvY2Vzc2VkPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5pbWFnZSBwcm9jZXNzZWQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICA8L2xheW91dD4KICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSIyIj4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFHcm91cEJveCIgbmFtZT0iZ3JvdXBCb3hfOSI+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRpdGxlIj4KICAgICAgICAgICAgICAgPHN0cmluZz5FZGl0b3I8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxsYXlvdXQgY2xhc3M9IlFHcmlkTGF5b3V0IiBuYW1lPSJncmlkTGF5b3V0XzE5Ij4KICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVBsYWluVGV4dEVkaXQiIG5hbWU9Im9jcl9lZGl0b3IiPgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5lZGl0IHJlc3VsdHM8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmVkaXQgcmVzdWx0czwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZWRpdCByZXN1bHRzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmVkaXQgcmVzdWx0czwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZWRpdCByZXN1bHRzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0icGxhY2Vob2xkZXJUZXh0Ij4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5yZXN1bHQgZnJvbSBpbWFnZSBwcm9jZXNzaW5nLi4uPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPC9sYXlvdXQ+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgIDwvbGF5b3V0PgogICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgIDwvaXRlbT4KICAgICAgIDwvbGF5b3V0PgogICAgICA8L3dpZGdldD4KICAgICAgPHdpZGdldCBjbGFzcz0iUVdpZGdldCIgbmFtZT0idGFiXzYiPgogICAgICAgPGF0dHJpYnV0ZSBuYW1lPSJ0aXRsZSI+CiAgICAgICAgPHN0cmluZz5JbXBvcnQ8L3N0cmluZz4KICAgICAgIDwvYXR0cmlidXRlPgogICAgICAgPGF0dHJpYnV0ZSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICA8c3RyaW5nPmltcG9ydC9leHBvcnQgcHJvZHVjdDwvc3RyaW5nPgogICAgICAgPC9hdHRyaWJ1dGU+CiAgICAgICA8YXR0cmlidXRlIG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgPHN0cmluZz5pbXBvcnQvZXhwb3J0IHByb2R1Y3Q8L3N0cmluZz4KICAgICAgIDwvYXR0cmlidXRlPgogICAgICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRMYXlvdXRfMjEiPgogICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIwIj4KICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVNjcm9sbEFyZWEiIG5hbWU9InNjcm9sbEFyZWFfNiI+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2lkZ2V0UmVzaXphYmxlIj4KICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFXaWRnZXQiIG5hbWU9InNjcm9sbEFyZWFXaWRnZXRDb250ZW50c182Ij4KICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZ2VvbWV0cnkiPgogICAgICAgICAgICA8cmVjdD4KICAgICAgICAgICAgIDx4PjA8L3g+CiAgICAgICAgICAgICA8eT4wPC95PgogICAgICAgICAgICAgPHdpZHRoPjExMjI8L3dpZHRoPgogICAgICAgICAgICAgPGhlaWdodD42ODM8L2hlaWdodD4KICAgICAgICAgICAgPC9yZWN0PgogICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRMYXlvdXRfMjQiPgogICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRR3JvdXBCb3giIG5hbWU9Imdyb3VwQm94XzEwIj4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGl0bGUiPgogICAgICAgICAgICAgICA8c3RyaW5nPkZpbGVzeXN0ZW0gU3RvcmFnZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRMYXlvdXRfMjIiPgogICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMSI+CiAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0iaW1wb3J0X2Jyb3dzZSI+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBmb3IgZmlsZSBpbXBvcnQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBmb3IgZmlsZSBpbXBvcnQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBmb3IgZmlsZSBpbXBvcnQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGZvciBmaWxlIGltcG9ydDwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGZvciBmaWxlIGltcG9ydDwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPkJyb3dzZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iNSI+CiAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0iaW1wb3J0X3NlbmRUb1NlcnZlciI+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPnNlbmQgcmVhZCBkYXRhIHRvIHNlcnZlcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c2VuZCByZWFkIGRhdGEgdG8gc2VydmVyPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5zZW5kIHJlYWQgZGF0YSB0byBzZXJ2ZXI8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+c2VuZCByZWFkIGRhdGEgdG8gc2VydmVyPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5zZW5kIHJlYWQgZGF0YSB0byBzZXJ2ZXI8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5TYXZlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIzIj4KICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJpbXBvcnRfcmVhZGZpbGUiPgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5yZWFkIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPnJlYWQgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+cmVhZCBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPnJlYWQgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+cmVhZCBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+UmVhZDwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMiI+CiAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9ImltcG9ydF9mb3JtYXQiPgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5pbXBvcnQgZmlsZSBmb3JtYXQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmltcG9ydCBmaWxlIGZvcm1hdDwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+aW1wb3J0IGZpbGUgZm9ybWF0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmltcG9ydCBmaWxlIGZvcm1hdDwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+aW1wb3J0IGZpbGUgZm9ybWF0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8aXRlbT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5KU09OPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgIDxpdGVtPgogICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkNTVjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgICA8aXRlbT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5RUjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgICA8aXRlbT4KICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgPHN0cmluZz5Db2RlMTI4PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUxpbmVFZGl0IiBuYW1lPSJpbXBvcnRfbG9jYXRpb24iPgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5pbXBvcnRfbG9jYXRpb248L3N0cmluZz4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmltcG9ydF9sb2NhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+aW1wb3J0X2xvY2F0aW9uPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmltcG9ydF9sb2NhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+aW1wb3J0X2xvY2F0aW9uPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+aW1wb3J0X3Byb2R1Y3QuanNvbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImRyYWdFbmFibGVkIj4KICAgICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFjZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICAgICA8c3RyaW5nPmltcG9ydF9sb2NhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImNsZWFyQnV0dG9uRW5hYmxlZCI+CiAgICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSI0Ij4KICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDaGVja0JveCIgbmFtZT0iZG9udFBhcnNlIj4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+cmVhZCBidXQgZG8gbm90IHBhcnNlIGludG8gZGljdGlvbmFyeTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+cmVhZCBidXQgZG8gbm90IHBhcnNlIGludG8gZGljdGlvbmFyeTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+cmVhZCBidXQgZG8gbm90IHBhcnNlIGludG8gZGljdGlvbmFyeTwvc3RyaW5nPgogICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5yZWFkIGJ1dCBkbyBub3QgcGFyc2UgaW50byBkaWN0aW9uYXJ5PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgPHN0cmluZz5yZWFkIGJ1dCBkbyBub3QgcGFyc2UgaW50byBkaWN0aW9uYXJ5PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RG8gTm90IFBhcnNlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPC9sYXlvdXQ+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICA8aXRlbSByb3c9IjEiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRR3JvdXBCb3giIG5hbWU9Imdyb3VwQm94XzExIj4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGl0bGUiPgogICAgICAgICAgICAgICA8c3RyaW5nPlZpZXdlcjwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRMYXlvdXRfMjMiPgogICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUGxhaW5UZXh0RWRpdCIgbmFtZT0iaW1wb3J0X3ZpZXdlciIvPgogICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPC9sYXlvdXQ+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgIDwvbGF5b3V0PgogICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgIDwvaXRlbT4KICAgICAgIDwvbGF5b3V0PgogICAgICA8L3dpZGdldD4KICAgICAgPHdpZGdldCBjbGFzcz0iUVdpZGdldCIgbmFtZT0idGFiXzciPgogICAgICAgPGF0dHJpYnV0ZSBuYW1lPSJ0aXRsZSI+CiAgICAgICAgPHN0cmluZz5GaWxlMlFSPC9zdHJpbmc+CiAgICAgICA8L2F0dHJpYnV0ZT4KICAgICAgIDxsYXlvdXQgY2xhc3M9IlFHcmlkTGF5b3V0IiBuYW1lPSJncmlkTGF5b3V0XzI1Ij4KICAgICAgICA8aXRlbSByb3c9IjEiIGNvbHVtbj0iMyI+CiAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJmaWxlMnFyX3NvdXJjZV9icm93c2UiPgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgIDxzdHJpbmc+QnJvd3NlPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICA8L3dpZGdldD4KICAgICAgICA8L2l0ZW0+CiAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjAiIGNvbHNwYW49IjMiPgogICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRTGluZUVkaXQiIG5hbWU9ImZpbGUycXJfc291cmNlIj4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICA8c3RyaW5nPmZpbGUgdG8gY29udmVydCB0byBxcjwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgIDxzdHJpbmc+ZmlsZSB0byBjb252ZXJ0IHRvIHFyPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgPHN0cmluZz5maWxlIHRvIGNvbnZlcnQgdG8gcXI8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgIDxzdHJpbmc+ZmlsZSB0byBjb252ZXJ0IHRvIHFyPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgPHN0cmluZz5maWxlIHRvIGNvbnZlcnQgdG8gcXI8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgPHN0cmluZy8+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImRyYWdFbmFibGVkIj4KICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFjZWhvbGRlclRleHQiPgogICAgICAgICAgIDxzdHJpbmc+c291cmNlIGZpbGU8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iY2xlYXJCdXR0b25FbmFibGVkIj4KICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgPC9pdGVtPgogICAgICAgIDxpdGVtIHJvdz0iNSIgY29sdW1uPSIwIiBjb2xzcGFuPSI0Ij4KICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVByb2dyZXNzQmFyIiBuYW1lPSJmaWxlMnFyX3Byb2dyZXNzIj4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ2YWx1ZSI+CiAgICAgICAgICAgPG51bWJlcj4wPC9udW1iZXI+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICA8L3dpZGdldD4KICAgICAgICA8L2l0ZW0+CiAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjAiIGNvbHNwYW49IjQiPgogICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRVGV4dEVkaXQiIG5hbWU9ImZpbGUycXJfc3RhZ2Vfdmlld2VyIj4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICA8c3RyaW5nPndhdGNoIGl0IHdvcms8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICA8c3RyaW5nPndhdGNoIGl0IHdvcms8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICA8c3RyaW5nPndhdGNoIGl0IHdvcms8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgIDxzdHJpbmc+d2F0Y2ggaXQgd29yazwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgIDxzdHJpbmc+d2F0Y2ggaXQgd29yazwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0YWJDaGFuZ2VzRm9jdXMiPgogICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9InJlYWRPbmx5Ij4KICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFjZWhvbGRlclRleHQiPgogICAgICAgICAgIDxzdHJpbmc+V0FSTklORzogVE9PIGJpZyBPRiBmaWxlcyBXSUxMIHRha2UgQSBsb25nIHRpbWUhPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICA8L3dpZGdldD4KICAgICAgICA8L2l0ZW0+CiAgICAgICAgPGl0ZW0gcm93PSIyIiBjb2x1bW49IjMiPgogICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0iZmlsZTJxcl9kZXN0aW5hdGlvbl9icm93c2UiPgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgIDxzdHJpbmc+QnJvd3NlPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICA8L3dpZGdldD4KICAgICAgICA8L2l0ZW0+CiAgICAgICAgPGl0ZW0gcm93PSIyIiBjb2x1bW49IjAiIGNvbHNwYW49IjMiPgogICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRTGluZUVkaXQiIG5hbWU9ImZpbGUycXJfZGVzdGluYXRpb24iPgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgIDxzdHJpbmc+ZGVzdGluYXRpb24gdG8gc2F2ZSBxciBmaWxlcyB0bzwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgIDxzdHJpbmc+ZGVzdGluYXRpb24gdG8gc2F2ZSBxciBmaWxlcyB0bzwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgIDxzdHJpbmc+ZGVzdGluYXRpb24gdG8gc2F2ZSBxciBmaWxlcyB0bzwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgPHN0cmluZz5kZXN0aW5hdGlvbiB0byBzYXZlIHFyIGZpbGVzIHRvPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgPHN0cmluZz5kZXN0aW5hdGlvbiB0byBzYXZlIHFyIGZpbGVzIHRvPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgIDxzdHJpbmc+Li9xcnM8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZHJhZ0VuYWJsZWQiPgogICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9InBsYWNlaG9sZGVyVGV4dCI+CiAgICAgICAgICAgPHN0cmluZz5kZXN0aW5hdGlvbiBmaWxlPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImNsZWFyQnV0dG9uRW5hYmxlZCI+CiAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgIDwvaXRlbT4KICAgICAgICA8aXRlbSByb3c9IjMiIGNvbHVtbj0iMCIgY29sc3Bhbj0iNCI+CiAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJmaWxlMnFyX3N0YXJ0Ij4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICA8c3RyaW5nPnN0YXJ0IHRoZSBwcm9jZXNzPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgPHN0cmluZz5zdGFydCB0aGUgcHJvY2Vzczwvc3RyaW5nPgogICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgIDxzdHJpbmc+c3RhcnQgdGhlIHByb2Nlc3M8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgIDxzdHJpbmc+c3RhcnQgdGhlIHByb2Nlc3M8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICA8c3RyaW5nPnN0YXJ0IHRoZSBwcm9jZXNzPC9zdHJpbmc+CiAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgIDxzdHJpbmc+U3RhcnQ8L3N0cmluZz4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgIDwvaXRlbT4KICAgICAgIDwvbGF5b3V0PgogICAgICA8L3dpZGdldD4KICAgICAgPHdpZGdldCBjbGFzcz0iUVdpZGdldCIgbmFtZT0idGFiXzgiPgogICAgICAgPGF0dHJpYnV0ZSBuYW1lPSJ0aXRsZSI+CiAgICAgICAgPHN0cmluZz5RUjJGaWxlPC9zdHJpbmc+CiAgICAgICA8L2F0dHJpYnV0ZT4KICAgICAgIDxsYXlvdXQgY2xhc3M9IlFHcmlkTGF5b3V0IiBuYW1lPSJncmlkTGF5b3V0XzI2Ij4KICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMSI+CiAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFTY3JvbGxBcmVhIiBuYW1lPSJzY3JvbGxBcmVhXzciPgogICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndpZGdldFJlc2l6YWJsZSI+CiAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRV2lkZ2V0IiBuYW1lPSJzY3JvbGxBcmVhV2lkZ2V0Q29udGVudHNfNyI+CiAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9Imdlb21ldHJ5Ij4KICAgICAgICAgICAgPHJlY3Q+CiAgICAgICAgICAgICA8eD4wPC94PgogICAgICAgICAgICAgPHk+MDwveT4KICAgICAgICAgICAgIDx3aWR0aD4xMTIyPC93aWR0aD4KICAgICAgICAgICAgIDxoZWlnaHQ+NjgzPC9oZWlnaHQ+CiAgICAgICAgICAgIDwvcmVjdD4KICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgIDxsYXlvdXQgY2xhc3M9IlFHcmlkTGF5b3V0IiBuYW1lPSJncmlkTGF5b3V0XzI3Ij4KICAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjAiIGNvbHNwYW49IjMiPgogICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVBsYWluVGV4dEVkaXQiIG5hbWU9InFyMmZpbGVfc3RhZ2Vfdmlld2VyIj4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+d2F0Y2ggaXQgZ288L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPndhdGNoIGl0IGdvPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgPHN0cmluZz53YXRjaCBpdCBnbzwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgPHN0cmluZz53YXRjaCBpdCBnbzwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+d2F0Y2ggaXQgZ288L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0YWJDaGFuZ2VzRm9jdXMiPgogICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InJlYWRPbmx5Ij4KICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFjZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICA8c3RyaW5nPnRvbyBiaWcgb2YgZmlsZXMgd2lsbCB0YWtlIGEgbG9uZyB0aW1lPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSIwIiBjb2xzcGFuPSIzIj4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQcm9ncmVzc0JhciIgbmFtZT0icXIyZmlsZV9wcm9ncmVzcyI+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InZhbHVlIj4KICAgICAgICAgICAgICAgPG51bWJlcj4wPC9udW1iZXI+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iMiIgY29sdW1uPSIwIj4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFMaW5lRWRpdCIgbmFtZT0icXIyZmlsZV9zb3VyY2UiPgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgPHN0cmluZz5zb3VyY2UgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c291cmNlIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICA8c3RyaW5nPnNvdXJjZSBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICA8c3RyaW5nPnNvdXJjZSBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgPHN0cmluZz5zb3VyY2UgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICA8c3RyaW5nPnNvdXJjZS5xci50YXIueHo8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJkcmFnRW5hYmxlZCI+CiAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0icGxhY2Vob2xkZXJUZXh0Ij4KICAgICAgICAgICAgICAgPHN0cmluZz5zb3VyY2UgZmlsZS5xci50YXIueHo8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJjbGVhckJ1dHRvbkVuYWJsZWQiPgogICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICA8aXRlbSByb3c9IjIiIGNvbHVtbj0iMSI+CiAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0icXIyZmlsZV9zb3VyY2VfYnJvd3NlIj4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c291cmNlIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPnNvdXJjZSBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgPHN0cmluZz5zb3VyY2UgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgPHN0cmluZz5zb3VyY2UgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+c291cmNlIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgPHN0cmluZz5Ccm93c2U8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgPGl0ZW0gcm93PSIzIiBjb2x1bW49IjAiPgogICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUxpbmVFZGl0IiBuYW1lPSJxcjJmaWxlX2Rlc3RpbmF0aW9uIj4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+aWYgbGVmdCBlbXB0eSwgdXNlIHNvdXJjZSBuYW1lIG1pbnVzIC5xci50YXIueHo8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPmlmIGxlZnQgZW1wdHksIHVzZSBzb3VyY2UgbmFtZSBtaW51cyAucXIudGFyLnh6PC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgPHN0cmluZz5pZiBsZWZ0IGVtcHR5LCB1c2Ugc291cmNlIG5hbWUgbWludXMgLnFyLnRhci54ejwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgPHN0cmluZz5pZiBsZWZ0IGVtcHR5LCB1c2Ugc291cmNlIG5hbWUgbWludXMgLnFyLnRhci54ejwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+aWYgbGVmdCBlbXB0eSwgdXNlIHNvdXJjZSBuYW1lIG1pbnVzIC5xci50YXIueHo8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgPHN0cmluZy8+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZHJhZ0VuYWJsZWQiPgogICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InBsYWNlaG9sZGVyVGV4dCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+ZGVzdGluYXRpb24gZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImNsZWFyQnV0dG9uRW5hYmxlZCI+CiAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgIDxpdGVtIHJvdz0iMyIgY29sdW1uPSIxIj4KICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJxcjJmaWxlX2Rlc3RpbmF0aW9uX2Jyb3dzZSI+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPmRlc3RpbmF0aW9uIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPmRlc3RpbmF0aW9uIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICA8c3RyaW5nPmRlc3RpbmF0aW9uIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+ZGVzdGluYXRpb24gZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+ZGVzdGluYXRpb24gZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICA8c3RyaW5nPkJyb3dzZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICA8aXRlbSByb3c9IjQiIGNvbHVtbj0iMCIgY29sc3Bhbj0iMiI+CiAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0icXIyZmlsZV9zdGFydCI+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICA8c3RyaW5nPmJlZ2luIHByb2Nlc3NpbmcgaW1hZ2UgcGFja2FnZTwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+YmVnaW4gcHJvY2Vzc2luZyBpbWFnZSBwYWNrYWdlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgPHN0cmluZz5iZWdpbiBwcm9jZXNzaW5nIGltYWdlIHBhY2thZ2U8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgIDxzdHJpbmc+YmVnaW4gcHJvY2Vzc2luZyBpbWFnZSBwYWNrYWdlPC9zdHJpbmc+CiAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgPHN0cmluZz5iZWdpbiBwcm9jZXNzaW5nIGltYWdlIHBhY2thZ2U8L3N0cmluZz4KICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgPHN0cmluZz5TdGFydDwvc3RyaW5nPgogICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgIDwvbGF5b3V0PgogICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgIDwvaXRlbT4KICAgICAgIDwvbGF5b3V0PgogICAgICA8L3dpZGdldD4KICAgICA8L3dpZGdldD4KICAgIDwvaXRlbT4KICAgPC9sYXlvdXQ+CiAgPC93aWRnZXQ+CiAgPHdpZGdldCBjbGFzcz0iUU1lbnVCYXIiIG5hbWU9Im1lbnViYXIiPgogICA8cHJvcGVydHkgbmFtZT0iZ2VvbWV0cnkiPgogICAgPHJlY3Q+CiAgICAgPHg+MDwveD4KICAgICA8eT4wPC95PgogICAgIDx3aWR0aD4xMTU4PC93aWR0aD4KICAgICA8aGVpZ2h0PjMyPC9oZWlnaHQ+CiAgICA8L3JlY3Q+CiAgIDwvcHJvcGVydHk+CiAgIDx3aWRnZXQgY2xhc3M9IlFNZW51IiBuYW1lPSJtZW51X0ZpbGUiPgogICAgPHByb3BlcnR5IG5hbWU9InRpdGxlIj4KICAgICA8c3RyaW5nPiZhbXA7RmlsZTwvc3RyaW5nPgogICAgPC9wcm9wZXJ0eT4KICAgIDxhZGRhY3Rpb24gbmFtZT0iYWN0aW9uX0V4aXQiLz4KICAgPC93aWRnZXQ+CiAgIDx3aWRnZXQgY2xhc3M9IlFNZW51IiBuYW1lPSJtZW51SGVscCI+CiAgICA8cHJvcGVydHkgbmFtZT0idGl0bGUiPgogICAgIDxzdHJpbmc+SGVscDwvc3RyaW5nPgogICAgPC9wcm9wZXJ0eT4KICAgIDxhZGRhY3Rpb24gbmFtZT0iYWN0aW9uQWJvdXQiLz4KICAgPC93aWRnZXQ+CiAgIDxhZGRhY3Rpb24gbmFtZT0ibWVudV9GaWxlIi8+CiAgIDxhZGRhY3Rpb24gbmFtZT0ibWVudUhlbHAiLz4KICA8L3dpZGdldD4KICA8d2lkZ2V0IGNsYXNzPSJRU3RhdHVzQmFyIiBuYW1lPSJzdGF0dXNiYXIiLz4KICA8YWN0aW9uIG5hbWU9ImFjdGlvbl9FeGl0Ij4KICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgPHN0cmluZz4mYW1wO0V4aXQ8L3N0cmluZz4KICAgPC9wcm9wZXJ0eT4KICAgPHByb3BlcnR5IG5hbWU9InNob3J0Y3V0Ij4KICAgIDxzdHJpbmc+Q3RybCtRPC9zdHJpbmc+CiAgIDwvcHJvcGVydHk+CiAgPC9hY3Rpb24+CiAgPGFjdGlvbiBuYW1lPSJhY3Rpb25BYm91dCI+CiAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgIDxzdHJpbmc+QWJvdXQ8L3N0cmluZz4KICAgPC9wcm9wZXJ0eT4KICA8L2FjdGlvbj4KIDwvd2lkZ2V0PgogPHRhYnN0b3BzPgogIDx0YWJzdG9wPnByb2R1Y3RfdHlwZTwvdGFic3RvcD4KICA8dGFic3RvcD5zaXplPC90YWJzdG9wPgogIDx0YWJzdG9wPmNhbl9ob2xkX2dsYXNzPC90YWJzdG9wPgogIDx0YWJzdG9wPmhhc19nbGFzczwvdGFic3RvcD4KICA8dGFic3RvcD5jYW5faG9sZF9jYW52YXM8L3RhYnN0b3A+CiAgPHRhYnN0b3A+aGFzX2NhbnZhczwvdGFic3RvcD4KICA8dGFic3RvcD5vcmllbnRhdGlvbjwvdGFic3RvcD4KICA8dGFic3RvcD53b29kX3R5cGU8L3RhYnN0b3A+CiAgPHRhYnN0b3A+ZnJhbWVfc2hhcGU8L3RhYnN0b3A+CiAgPHRhYnN0b3A+ZnJvbnRfb3V0ZXJfcHJvZmlsZTwvdGFic3RvcD4KICA8dGFic3RvcD5mcm9udF9pbm5lcl9wcm9maWxlPC90YWJzdG9wPgogIDx0YWJzdG9wPnJlYXJfaW5uZXJfcHJvZmlsZTwvdGFic3RvcD4KICA8dGFic3RvcD5jZW50ZXJfaW5uZXJfcHJvZmlsZTwvdGFic3RvcD4KICA8dGFic3RvcD5jZW50ZXJfb3V0ZXJfcHJvZmlsZTwvdGFic3RvcD4KICA8dGFic3RvcD5maW5pc2hfdHlwZTwvdGFic3RvcD4KICA8dGFic3RvcD5zdGFja2FibGU8L3RhYnN0b3A+CiAgPHRhYnN0b3A+Y29tbWVudHM8L3RhYnN0b3A+CiAgPHRhYnN0b3A+Y3VzdG9tX2VuZ3JhdmVkPC90YWJzdG9wPgogIDx0YWJzdG9wPmVuZ3JhdmluZ196aXA8L3RhYnN0b3A+CiAgPHRhYnN0b3A+YnJvd3NlX2VuZ3JhdmluZ196aXA8L3RhYnN0b3A+CiAgPHRhYnN0b3A+cmVhcjwvdGFic3RvcD4KICA8dGFic3RvcD5icm93c2VfcmVhcjwvdGFic3RvcD4KICA8dGFic3RvcD5jb3JuZXI8L3RhYnN0b3A+CiAgPHRhYnN0b3A+YnJvd3NlX2Nvcm5lcjwvdGFic3RvcD4KICA8dGFic3RvcD5mcm9udDwvdGFic3RvcD4KICA8dGFic3RvcD5icm93c2VfZnJvbnQ8L3RhYnN0b3A+CiAgPHRhYnN0b3A+aXRlbV93ZWlnaHQ8L3RhYnN0b3A+CiAgPHRhYnN0b3A+aXRlbV93ZWlnaHRfdW5pdDwvdGFic3RvcD4KICA8dGFic3RvcD5wcmljZTwvdGFic3RvcD4KICA8dGFic3RvcD5vdGhlcl9mcmFtZV9zaXplX2RpYW1ldGVyPC90YWJzdG9wPgogIDx0YWJzdG9wPm90aGVyX2ZyYW1lX3NpemVfZGlhbWV0ZXJfdW5pdDwvdGFic3RvcD4KICA8dGFic3RvcD5zdGFpbmFibGU8L3RhYnN0b3A+CiAgPHRhYnN0b3A+c3RhaW48L3RhYnN0b3A+CiAgPHRhYnN0b3A+c29sZDwvdGFic3RvcD4KICA8dGFic3RvcD5zb2xkX3RvPC90YWJzdG9wPgogIDx0YWJzdG9wPm5ld19za3U8L3RhYnN0b3A+CiAgPHRhYnN0b3A+c2t1PC90YWJzdG9wPgogIDx0YWJzdG9wPm5ld19za3Vfd2hlbl9kb25lPC90YWJzdG9wPgogIDx0YWJzdG9wPnJlc2V0X3doZW5fZG9uZTwvdGFic3RvcD4KICA8dGFic3RvcD5zYXZlX25ld19wcm9kdWN0PC90YWJzdG9wPgogIDx0YWJzdG9wPnNhdmVfc2V0dGluZ3M8L3RhYnN0b3A+CiAgPHRhYnN0b3A+dGFiV2lkZ2V0PC90YWJzdG9wPgogIDx0YWJzdG9wPnNlcnZlcjwvdGFic3RvcD4KICA8dGFic3RvcD5zY3JvbGxBcmVhPC90YWJzdG9wPgogIDx0YWJzdG9wPnRva2VuPC90YWJzdG9wPgogIDx0YWJzdG9wPnNjcm9sbEFyZWFfMjwvdGFic3RvcD4KIDwvdGFic3RvcHM+CiA8cmVzb3VyY2VzLz4KIDxjb25uZWN0aW9ucz4KICA8Y29ubmVjdGlvbj4KICAgPHNlbmRlcj5hY3Rpb25fRXhpdDwvc2VuZGVyPgogICA8c2lnbmFsPnRyaWdnZXJlZCgpPC9zaWduYWw+CiAgIDxyZWNlaXZlcj5NYWluV2luZG93PC9yZWNlaXZlcj4KICAgPHNsb3Q+Y2xvc2UoKTwvc2xvdD4KICAgPGhpbnRzPgogICAgPGhpbnQgdHlwZT0ic291cmNlbGFiZWwiPgogICAgIDx4Pi0xPC94PgogICAgIDx5Pi0xPC95PgogICAgPC9oaW50PgogICAgPGhpbnQgdHlwZT0iZGVzdGluYXRpb25sYWJlbCI+CiAgICAgPHg+NTM2PC94PgogICAgIDx5PjM3OTwveT4KICAgIDwvaGludD4KICAgPC9oaW50cz4KICA8L2Nvbm5lY3Rpb24+CiA8L2Nvbm5lY3Rpb25zPgo8L3VpPgo='''
    icon='''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'''
    itemui='''PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHVpIHZlcnNpb249IjQuMCI+CiA8Y2xhc3M+RGlhbG9nPC9jbGFzcz4KIDx3aWRnZXQgY2xhc3M9IlFEaWFsb2ciIG5hbWU9IkRpYWxvZyI+CiAgPHByb3BlcnR5IG5hbWU9ImVuYWJsZWQiPgogICA8Ym9vbD50cnVlPC9ib29sPgogIDwvcHJvcGVydHk+CiAgPHByb3BlcnR5IG5hbWU9Imdlb21ldHJ5Ij4KICAgPHJlY3Q+CiAgICA8eD4wPC94PgogICAgPHk+MDwveT4KICAgIDx3aWR0aD4xMDMwPC93aWR0aD4KICAgIDxoZWlnaHQ+NzU4PC9oZWlnaHQ+CiAgIDwvcmVjdD4KICA8L3Byb3BlcnR5PgogIDxwcm9wZXJ0eSBuYW1lPSJ3aW5kb3dUaXRsZSI+CiAgIDxzdHJpbmc+SXRlbUVkaXRWaWV3PC9zdHJpbmc+CiAgPC9wcm9wZXJ0eT4KICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgIDxzdHJpbmc+SXRlbSBEYXRhPC9zdHJpbmc+CiAgPC9wcm9wZXJ0eT4KICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgPHN0cmluZz5JdGVtIERhdGE8L3N0cmluZz4KICA8L3Byb3BlcnR5PgogIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICA8c3RyaW5nPkl0ZW0gRGF0YTwvc3RyaW5nPgogIDwvcHJvcGVydHk+CiAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgPHN0cmluZz5JdGVtIERhdGE8L3N0cmluZz4KICA8L3Byb3BlcnR5PgogIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICA8c3RyaW5nPkl0ZW0gRGF0YTwvc3RyaW5nPgogIDwvcHJvcGVydHk+CiAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRMYXlvdXQiPgogICA8aXRlbSByb3c9IjIiIGNvbHVtbj0iNiI+CiAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0iY2xvc2VNZSI+CiAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICA8c3RyaW5nPmNsb3NlIGRpYWxvZzwvc3RyaW5nPgogICAgIDwvcHJvcGVydHk+CiAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgIDxzdHJpbmc+Y2xvc2UgZGlhbG9nPC9zdHJpbmc+CiAgICAgPC9wcm9wZXJ0eT4KICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgPHN0cmluZz5jbG9zZSBkaWFsb2c8L3N0cmluZz4KICAgICA8L3Byb3BlcnR5PgogICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgIDxzdHJpbmc+Y2xvc2UgZGlhbG9nPC9zdHJpbmc+CiAgICAgPC9wcm9wZXJ0eT4KICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgPHN0cmluZz5jbG9zZSBkaWFsb2c8L3N0cmluZz4KICAgICA8L3Byb3BlcnR5PgogICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgPHN0cmluZz5DbG9zZTwvc3RyaW5nPgogICAgIDwvcHJvcGVydHk+CiAgICA8L3dpZGdldD4KICAgPC9pdGVtPgogICA8aXRlbSByb3c9IjIiIGNvbHVtbj0iMCI+CiAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0iYnJvd3NlX3FyX3NhdmVfbG9jYXRpb24iPgogICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgPHN0cmluZz5icm93c2Ugc2F2ZSBsb2NhdGlvbjwvc3RyaW5nPgogICAgIDwvcHJvcGVydHk+CiAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgIDxzdHJpbmc+YnJvd3NlIHNhdmUgbG9jYXRpb248L3N0cmluZz4KICAgICA8L3Byb3BlcnR5PgogICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICA8c3RyaW5nPmJyb3dzZSBzYXZlIGxvY2F0aW9uPC9zdHJpbmc+CiAgICAgPC9wcm9wZXJ0eT4KICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICA8c3RyaW5nPmJyb3dzZSBzYXZlIGxvY2F0aW9uPC9zdHJpbmc+CiAgICAgPC9wcm9wZXJ0eT4KICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgPHN0cmluZz5icm93c2Ugc2F2ZSBsb2NhdGlvbjwvc3RyaW5nPgogICAgIDwvcHJvcGVydHk+CiAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICA8c3RyaW5nPkJyb3dzZTwvc3RyaW5nPgogICAgIDwvcHJvcGVydHk+CiAgICA8L3dpZGdldD4KICAgPC9pdGVtPgogICA8aXRlbSByb3c9IjIiIGNvbHVtbj0iMyI+CiAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0iZ2V0X2xhYmVsX2ZpbGUiPgogICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgPHN0cmluZz5nZXQgbGFiZWwgZmlsZSBmb3IgaW5zY2FwZTwvc3RyaW5nPgogICAgIDwvcHJvcGVydHk+CiAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgIDxzdHJpbmc+Z2V0IGxhYmVsIGZpbGUgZm9yIGluc2NhcGU8L3N0cmluZz4KICAgICA8L3Byb3BlcnR5PgogICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICA8c3RyaW5nPmdldCBsYWJlbCBmaWxlIGZvciBpbnNjYXBlPC9zdHJpbmc+CiAgICAgPC9wcm9wZXJ0eT4KICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICA8c3RyaW5nPmdldCBsYWJlbCBmaWxlIGZvciBpbnNjYXBlPC9zdHJpbmc+CiAgICAgPC9wcm9wZXJ0eT4KICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgPHN0cmluZz5nZXQgbGFiZWwgZmlsZSBmb3IgaW5zY2FwZTwvc3RyaW5nPgogICAgIDwvcHJvcGVydHk+CiAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICA8c3RyaW5nPkdldCBMYWJlbCBGaWxlPC9zdHJpbmc+CiAgICAgPC9wcm9wZXJ0eT4KICAgIDwvd2lkZ2V0PgogICA8L2l0ZW0+CiAgIDxpdGVtIHJvdz0iMiIgY29sdW1uPSIyIj4KICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJleHBvcnQyZnMiPgogICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgPHN0cmluZz5FeHBvcnQ8L3N0cmluZz4KICAgICA8L3Byb3BlcnR5PgogICAgPC93aWRnZXQ+CiAgIDwvaXRlbT4KICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjAiIGNvbHNwYW49IjciPgogICAgPHdpZGdldCBjbGFzcz0iUUxpbmVFZGl0IiBuYW1lPSJxcl9zYXZlX2xvY2F0aW9uIj4KICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgIDxzdHJpbmc+d2hlcmUgdG8gc2F2ZSB0aGUgZ2VuZXJhdGVkIFFSQ29kZTwvc3RyaW5nPgogICAgIDwvcHJvcGVydHk+CiAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgIDxzdHJpbmc+d2hlcmUgdG8gc2F2ZSB0aGUgZ2VuZXJhdGVkIFFSQ29kZTwvc3RyaW5nPgogICAgIDwvcHJvcGVydHk+CiAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgIDxzdHJpbmc+d2hlcmUgdG8gc2F2ZSB0aGUgZ2VuZXJhdGVkIFFSQ29kZTwvc3RyaW5nPgogICAgIDwvcHJvcGVydHk+CiAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgPHN0cmluZz53aGVyZSB0byBzYXZlIHRoZSBnZW5lcmF0ZWQgUVJDb2RlPC9zdHJpbmc+CiAgICAgPC9wcm9wZXJ0eT4KICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgPHN0cmluZz53aGVyZSB0byBzYXZlIHRoZSBnZW5lcmF0ZWQgUVJDb2RlPC9zdHJpbmc+CiAgICAgPC9wcm9wZXJ0eT4KICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgIDxzdHJpbmc+aXRlbV9xcmNvZGVfe3NrdX0ucG5nPC9zdHJpbmc+CiAgICAgPC9wcm9wZXJ0eT4KICAgICA8cHJvcGVydHkgbmFtZT0iZHJhZ0VuYWJsZWQiPgogICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgIDwvcHJvcGVydHk+CiAgICAgPHByb3BlcnR5IG5hbWU9InBsYWNlaG9sZGVyVGV4dCI+CiAgICAgIDxzdHJpbmc+V2hlcmUgdG8gc2F2ZSBRUkNvZGU8L3N0cmluZz4KICAgICA8L3Byb3BlcnR5PgogICAgIDxwcm9wZXJ0eSBuYW1lPSJjbGVhckJ1dHRvbkVuYWJsZWQiPgogICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgIDwvcHJvcGVydHk+CiAgICA8L3dpZGdldD4KICAgPC9pdGVtPgogICA8aXRlbSByb3c9IjIiIGNvbHVtbj0iNSI+CiAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0icHJpbnQiPgogICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgPHN0cmluZz5QcmludCBFeHBvcnRhYmxlIERhdGE8L3N0cmluZz4KICAgICA8L3Byb3BlcnR5PgogICAgPC93aWRnZXQ+CiAgIDwvaXRlbT4KICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjAiIGNvbHNwYW49IjciPgogICAgPHdpZGdldCBjbGFzcz0iUVRhYldpZGdldCIgbmFtZT0idGFiV2lkZ2V0Ij4KICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgIDxzdHJpbmc+ZmlsZXMgYXNzb2NpYXRlZCB3aXRoIHByb2R1Y3QgY2FuIGJlIERvd25sb2FkZWQgYXMgYSBRUkNvZGU8L3N0cmluZz4KICAgICA8L3Byb3BlcnR5PgogICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICA8c3RyaW5nPmZpbGVzIGFzc29jaWF0ZWQgd2l0aCBwcm9kdWN0IGNhbiBiZSBEb3dubG9hZGVkIGFzIGEgUVJDb2RlPC9zdHJpbmc+CiAgICAgPC9wcm9wZXJ0eT4KICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgPHN0cmluZz5maWxlcyBhc3NvY2lhdGVkIHdpdGggcHJvZHVjdCBjYW4gYmUgRG93bmxvYWRlZCBhcyBhIFFSQ29kZTwvc3RyaW5nPgogICAgIDwvcHJvcGVydHk+CiAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgPHN0cmluZz5maWxlcyBhc3NvY2lhdGVkIHdpdGggcHJvZHVjdCBjYW4gYmUgRG93bmxvYWRlZCBhcyBhIFFSQ29kZTwvc3RyaW5nPgogICAgIDwvcHJvcGVydHk+CiAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgIDxzdHJpbmc+ZmlsZXMgYXNzb2NpYXRlZCB3aXRoIHByb2R1Y3QgY2FuIGJlIERvd25sb2FkZWQgYXMgYSBRUkNvZGU8L3N0cmluZz4KICAgICA8L3Byb3BlcnR5PgogICAgIDxwcm9wZXJ0eSBuYW1lPSJjdXJyZW50SW5kZXgiPgogICAgICA8bnVtYmVyPjA8L251bWJlcj4KICAgICA8L3Byb3BlcnR5PgogICAgIDx3aWRnZXQgY2xhc3M9IlFXaWRnZXQiIG5hbWU9InRhYiI+CiAgICAgIDxhdHRyaWJ1dGUgbmFtZT0idGl0bGUiPgogICAgICAgPHN0cmluZz5JdGVtPC9zdHJpbmc+CiAgICAgIDwvYXR0cmlidXRlPgogICAgICA8bGF5b3V0IGNsYXNzPSJRR3JpZExheW91dCIgbmFtZT0iZ3JpZExheW91dF84Ij4KICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIwIj4KICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRV2lkZ2V0IiBuYW1lPSJhcmVhIiBuYXRpdmU9InRydWUiPgogICAgICAgICA8bGF5b3V0IGNsYXNzPSJRR3JpZExheW91dCIgbmFtZT0iZ3JpZExheW91dF8yIj4KICAgICAgICAgIDxpdGVtIHJvdz0iMiIgY29sdW1uPSIwIiBjb2xzcGFuPSIyIj4KICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRU2Nyb2xsQXJlYSIgbmFtZT0ic2Nyb2xsQXJlYSI+CiAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aWRnZXRSZXNpemFibGUiPgogICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVdpZGdldCIgbmFtZT0ic2Nyb2xsQXJlYVdpZGdldENvbnRlbnRzIj4KICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJlbmFibGVkIj4KICAgICAgICAgICAgICA8Ym9vbD5mYWxzZTwvYm9vbD4KICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZ2VvbWV0cnkiPgogICAgICAgICAgICAgIDxyZWN0PgogICAgICAgICAgICAgICA8eD4wPC94PgogICAgICAgICAgICAgICA8eT4wPC95PgogICAgICAgICAgICAgICA8d2lkdGg+OTYxPC93aWR0aD4KICAgICAgICAgICAgICAgPGhlaWdodD4xMjUyPC9oZWlnaHQ+CiAgICAgICAgICAgICAgPC9yZWN0PgogICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgIDxsYXlvdXQgY2xhc3M9IlFHcmlkTGF5b3V0IiBuYW1lPSJncmlkTGF5b3V0XzMiPgogICAgICAgICAgICAgIDxpdGVtIHJvdz0iNCIgY29sdW1uPSIyIiBjb2xzcGFuPSI3Ij4KICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUdyb3VwQm94IiBuYW1lPSJncm91cEJveCI+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGl0bGUiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+RW5ncmF2aW5nIFppcDwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxsYXlvdXQgY2xhc3M9IlFHcmlkTGF5b3V0IiBuYW1lPSJncmlkTGF5b3V0XzQiPgogICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIwIj4KICAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJjdXN0b21fZW5ncmF2ZWQiPgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+Y3VzdG9tX2VuZ3JhdmVkPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5jdXN0b21fZW5ncmF2ZWQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmN1c3RvbV9lbmdyYXZlZDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5jdXN0b21fZW5ncmF2ZWQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmN1c3RvbV9lbmdyYXZlZDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUxpbmVFZGl0IiBuYW1lPSJlbmdyYXZpbmdfemlwIj4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmVuZ3JhdmluZ196aXA8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmVuZ3JhdmluZ196aXA8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmVuZ3JhdmluZ196aXA8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZW5ncmF2aW5nX3ppcDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZW5ncmF2aW5nX3ppcDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJkcmFnRW5hYmxlZCI+CiAgICAgICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0icGxhY2Vob2xkZXJUZXh0Ij4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmVuZ3JhdmluZy56aXA8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iY2xlYXJCdXR0b25FbmFibGVkIj4KICAgICAgICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSI0Ij4KICAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9InVwZGF0ZV9lbmdyYXZpbmdfemlwIj4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnVwZGF0ZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSI1Ij4KICAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9ImRlbGV0ZV9lbmdyYXZpbmdfemlwIj4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmRlbGV0ZSBlbmdyYXZpbmcgemlwPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5kZWxldGUgZW5ncmF2aW5nIHppcDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZGVsZXRlIGVuZ3JhdmluZyB6aXA8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZGVsZXRlIGVuZ3JhdmluZyB6aXA8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmRlbGV0ZSBlbmdyYXZpbmcgemlwPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RGVsZXRlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjMiPgogICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0iZW5ncmF2aW5nX3ppcF9kb3dubG9hZCI+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5Eb3dubG9hZDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIyIj4KICAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9ImJyb3dzZV9lbmdyYXZpbmdfemlwIj4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGVuZ3JhdmluZyB6aXA8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBlbmdyYXZpbmcgemlwPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBlbmdyYXZpbmcgemlwPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgZW5ncmF2aW5nIHppcDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkJyb3dzZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPC9sYXlvdXQ+CiAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iNiI+CiAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0ib3JpZW50YXRpb24iPgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+b3JpZW50YXRpb248L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPm9yaWVudGF0aW9uPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5vcmllbnRhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5vcmllbnRhdGlvbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+b3JpZW50YXRpb248L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICA8aXRlbSByb3c9IjEiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0iZnJvbnRfb3V0ZXJfcHJvZmlsZSI+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5mcm9udCBvdXRlciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5mcm9udCBvdXRlciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5mcm9udCBvdXRlciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmZyb250IG91dGVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmZyb250IG91dGVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMyI+CiAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0iaGFzX2dsYXNzIj4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmhhcyBnbGFzczwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+aGFzIGdsYXNzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5oYXMgZ2xhc3M8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+aGFzIGdsYXNzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5oYXMgZ2xhc3M8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICA8aXRlbSByb3c9IjEiIGNvbHVtbj0iNSI+CiAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0iZmluaXNoX3R5cGUiPgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+ZmluaXNoIHR5cGU8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmZpbmlzaCB0eXBlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5maW5pc2ggdHlwZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5maW5pc2ggdHlwZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+ZmluaXNoIHR5cGU8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICA8aXRlbSByb3c9IjkiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0ic3RhaW5hYmxlIj4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPnN0YWluYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+c3RhaW5hYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5zdGFpbmFibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+c3RhaW5hYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5zdGFpbmFibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iNCI+CiAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0iY2FuX2hvbGRfY2FudmFzIj4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmNhbiBob2xkIGNhbnZhczwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+Y2FuIGhvbGQgY2FudmFzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5jYW4gaG9sZCBjYW52YXM8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+Y2FuIGhvbGQgY2FudmFzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5jYW4gaG9sZCBjYW52YXM8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICA8aXRlbSByb3c9IjEwIiBjb2x1bW49IjEiIGNvbHNwYW49IjgiPgogICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRTGluZUVkaXQiIG5hbWU9InNvbGRfdG8iPgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+c29sZCB0bzwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+c29sZCB0bzwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+c29sZCB0bzwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5zb2xkIHRvPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5zb2xkIHRvPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImRyYWdFbmFibGVkIj4KICAgICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFjZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+c29sZCB0bzwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJjbGVhckJ1dHRvbkVuYWJsZWQiPgogICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjEiPgogICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9InNpemUiPgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+c2l6ZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+c2l6ZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+c2l6ZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5zaXplPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5zaXplPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjQiPgogICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9ImNlbnRlcl9vdXRlcl9wcm9maWxlIj4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmNlbnRlciBvdXRlciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5jZW50ZXIgb3V0ZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+Y2VudGVyIG91dGVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+Y2VudGVyIG91dGVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmNlbnRlciBvdXRlciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxMSIgY29sdW1uPSIxIiBjb2xzcGFuPSI4Ij4KICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUxpbmVFZGl0IiBuYW1lPSJza3UiPgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+c2t1PC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5za3U8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPnNrdTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5za3U8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPnNrdTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJkcmFnRW5hYmxlZCI+CiAgICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0icGxhY2Vob2xkZXJUZXh0Ij4KICAgICAgICAgICAgICAgICA8c3RyaW5nPnNrdTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJjbGVhckJ1dHRvbkVuYWJsZWQiPgogICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjYiPgogICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9InN0YWNrYWJsZSI+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5zdGFja2FibGU8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPnN0YWNrYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+c3RhY2thYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPnN0YWNrYWJsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+c3RhY2thYmxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPGl0ZW0gcm93PSI4IiBjb2x1bW49IjYiPgogICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRRG91YmxlU3BpbkJveCIgbmFtZT0iYW1vdW50X3BhaWQiPgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+YW1vdW50IHBhaWQgd2l0aDwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+YW1vdW50IHBhaWQgd2l0aDwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+YW1vdW50IHBhaWQgd2l0aDwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5hbW91bnQgcGFpZCB3aXRoPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5hbW91bnQgcGFpZCB3aXRoPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjEiPgogICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9ImZyb250X2lubmVyX3Byb2ZpbGUiPgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJvbnQgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJvbnQgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJvbnQgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5mcm9udCBpbm5lciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5mcm9udCBpbm5lciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjMiPgogICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9ImNlbnRlcl9pbm5lcl9wcm9maWxlIj4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmNlbnRlciBpbm5lciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5jZW50ZXIgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+Y2VudGVyIGlubmVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+Y2VudGVyIGlubmVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmNlbnRlciBpbm5lciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxMSIgY29sdW1uPSIwIj4KICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9Im5ld19za3UiPgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+Z2VuZXJhdGUgYSBuZXcgc2t1PC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5nZW5lcmF0ZSBhIG5ldyBza3U8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmdlbmVyYXRlIGEgbmV3IHNrdTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5nZW5lcmF0ZSBhIG5ldyBza3U8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmdlbmVyYXRlIGEgbmV3IHNrdTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICA8c3RyaW5nPk5ldyBTS1U8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICA8aXRlbSByb3c9IjgiIGNvbHVtbj0iNSI+CiAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0icGFpZF9mb3IiPgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+d2FzIGl0IHBhaWQgZm9yPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz53YXMgaXQgcGFpZCBmb3I8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPndhcyBpdCBwYWlkIGZvcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz53YXMgaXQgcGFpZCBmb3I8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPndhcyBpdCBwYWlkIGZvcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSI1Ij4KICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJoYXNfY2FudmFzIj4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmhhcyBjYW52YXM8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmhhcyBjYW52YXM8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmhhcyBjYW52YXM8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+aGFzIGNhbnZhczwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+aGFzIGNhbnZhczwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSIwIj4KICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJwcm9kdWN0X3R5cGUiPgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+cHJvZHVjdCB0eXBlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5wcm9kdWN0IHR5cGU8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPnByb2R1Y3QgdHlwZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5wcm9kdWN0IHR5cGU8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPnByb2R1Y3QgdHlwZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgIDxpdGVtIHJvdz0iMCIgY29sdW1uPSI4Ij4KICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJmcmFtZV9zaGFwZSI+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5mcmFtZV9zaGFwZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJhbWVfc2hhcGU8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmZyYW1lX3NoYXBlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmZyYW1lX3NoYXBlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5mcmFtZV9zaGFwZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgIDxpdGVtIHJvdz0iOCIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJpdGVtX3dlaWdodF91bml0Ij4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPml0ZW1fd2VpZ2h0X3VuaXQ8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPml0ZW1fd2VpZ2h0X3VuaXQ8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPml0ZW1fd2VpZ2h0X3VuaXQ8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+aXRlbV93ZWlnaHRfdW5pdDwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+aXRlbV93ZWlnaHRfdW5pdDwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgIDxpdGVtIHJvdz0iOCIgY29sdW1uPSIwIj4KICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUURvdWJsZVNwaW5Cb3giIG5hbWU9Iml0ZW1fd2VpZ2h0Ij4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPml0ZW1fd2VpZ2h0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5pdGVtX3dlaWdodDwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+aXRlbV93ZWlnaHQ8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+aXRlbV93ZWlnaHQ8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPml0ZW1fd2VpZ2h0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9Im1heGltdW0iPgogICAgICAgICAgICAgICAgIDxkb3VibGU+MTAwMDAwLjAwMDAwMDAwMDAwMDAwMDwvZG91YmxlPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzaW5nbGVTdGVwIj4KICAgICAgICAgICAgICAgICA8ZG91YmxlPjAuMDEwMDAwMDAwMDAwMDAwPC9kb3VibGU+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPGl0ZW0gcm93PSI3IiBjb2x1bW49IjIiIGNvbHNwYW49IjciPgogICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRR3JvdXBCb3giIG5hbWU9Imdyb3VwQm94XzMiPgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRpdGxlIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPkZyb250PC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRMYXlvdXRfNyI+CiAgICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjEiPgogICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0iYnJvd3NlX2Zyb250Ij4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBmcm9udCBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgZnJvbnQgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGZyb250IGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGZyb250IGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBmcm9udCBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+QnJvd3NlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRTGluZUVkaXQiIG5hbWU9ImZyb250Ij4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmZyb250PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5mcm9udDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJvbnQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJvbnQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmZyb250PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImRyYWdFbmFibGVkIj4KICAgICAgICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFjZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZnJvbnQuZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJjbGVhckJ1dHRvbkVuYWJsZWQiPgogICAgICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjMiPgogICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0idXBkYXRlX2Zyb250Ij4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPnVwZGF0ZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSI0Ij4KICAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9ImRlbGV0ZV9mcm9udCI+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5kZWxldGUgZnJvbnQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmRlbGV0ZSBmcm9udDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZGVsZXRlIGZyb250PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmRlbGV0ZSBmcm9udDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZGVsZXRlIGZyb250PC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RGVsZXRlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjIiPgogICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0iZnJvbnRfZG93bmxvYWQiPgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RG93bmxvYWQ8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMCIgY29sc3Bhbj0iNSI+CiAgICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFHcmFwaGljc1ZpZXciIG5hbWU9ImZyb250X3ZpZXciPgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9Im1pbmltdW1TaXplIj4KICAgICAgICAgICAgICAgICAgICA8c2l6ZT4KICAgICAgICAgICAgICAgICAgICAgPHdpZHRoPjA8L3dpZHRoPgogICAgICAgICAgICAgICAgICAgICA8aGVpZ2h0PjIwMDwvaGVpZ2h0PgogICAgICAgICAgICAgICAgICAgIDwvc2l6ZT4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDwvbGF5b3V0PgogICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPGl0ZW0gcm93PSI4IiBjb2x1bW49IjMiPgogICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRRG91YmxlU3BpbkJveCIgbmFtZT0ib3RoZXJfZnJhbWVfc2l6ZV9kaWFtZXRlciI+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5vdGhlcl9mcmFtZV9zaXplX2RpYW1ldGVyPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5vdGhlcl9mcmFtZV9zaXplX2RpYW1ldGVyPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5vdGhlcl9mcmFtZV9zaXplX2RpYW1ldGVyPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPm90aGVyX2ZyYW1lX3NpemVfZGlhbWV0ZXI8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPm90aGVyX2ZyYW1lX3NpemVfZGlhbWV0ZXI8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ibWF4aW11bSI+CiAgICAgICAgICAgICAgICAgPGRvdWJsZT4xMDAwMDAwLjAwMDAwMDAwMDAwMDAwMDwvZG91YmxlPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgIDxpdGVtIHJvdz0iOCIgY29sdW1uPSI0Ij4KICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUUNvbWJvQm94IiBuYW1lPSJvdGhlcl9mcmFtZV9zaXplX2RpYW1ldGVyX3VuaXQiPgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+b3RoZXJfZnJhbWVfc2l6ZV9kaWFtZXRlcl91bml0PC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5vdGhlcl9mcmFtZV9zaXplX2RpYW1ldGVyX3VuaXQ8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPm90aGVyX2ZyYW1lX3NpemVfZGlhbWV0ZXJfdW5pdDwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5vdGhlcl9mcmFtZV9zaXplX2RpYW1ldGVyX3VuaXQ8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPm90aGVyX2ZyYW1lX3NpemVfZGlhbWV0ZXJfdW5pdDwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgIDxpdGVtIHJvdz0iOCIgY29sdW1uPSIyIj4KICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUURvdWJsZVNwaW5Cb3giIG5hbWU9InByaWNlIj4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPnByaWNlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5wcmljZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+cHJpY2U8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+cHJpY2U8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPnByaWNlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9Im1heGltdW0iPgogICAgICAgICAgICAgICAgIDxkb3VibGU+MTAwMDAwLjAwMDAwMDAwMDAwMDAwMDwvZG91YmxlPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzaW5nbGVTdGVwIj4KICAgICAgICAgICAgICAgICA8ZG91YmxlPjAuMDEwMDAwMDAwMDAwMDAwPC9kb3VibGU+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPGl0ZW0gcm93PSI0IiBjb2x1bW49IjAiIHJvd3NwYW49IjQiIGNvbHNwYW49IjIiPgogICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUGxhaW5UZXh0RWRpdCIgbmFtZT0iY29tbWVudHMiPgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+Y29tbWVudHM8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmNvbW1lbnRzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5jb21tZW50czwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5jb21tZW50czwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+Y29tbWVudHM8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGFiQ2hhbmdlc0ZvY3VzIj4KICAgICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFjZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+Y29tbWVudHM8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICA8aXRlbSByb3c9IjEwIiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9InNvbGQiPgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+c29sZDwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+c29sZDwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+c29sZDwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5zb2xkPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5zb2xkPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPGl0ZW0gcm93PSI1IiBjb2x1bW49IjIiIGNvbHNwYW49IjciPgogICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRR3JvdXBCb3giIG5hbWU9Imdyb3VwQm94XzIiPgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRpdGxlIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPlJlYXI8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8bGF5b3V0IGNsYXNzPSJRR3JpZExheW91dCIgbmFtZT0iZ3JpZExheW91dF82Ij4KICAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjEiIGNvbHVtbj0iMyI+CiAgICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJ1cGRhdGVfcmVhciI+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz51cGRhdGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjEiIGNvbHVtbj0iNCI+CiAgICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJkZWxldGVfcmVhciI+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5kZWxldGUgcmVhcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZGVsZXRlIHJlYXI8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmRlbGV0ZSByZWFyPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmRlbGV0ZSByZWFyPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5kZWxldGUgcmVhcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkRlbGV0ZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9ImJyb3dzZV9yZWFyIj4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIHJlYXIgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIHJlYXIgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgcmVhciBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgcmVhciBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+QnJvd3NlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjAiPgogICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRTGluZUVkaXQiIG5hbWU9InJlYXIiPgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+cmVhcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+cmVhcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+cmVhcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5yZWFyPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5yZWFyPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImRyYWdFbmFibGVkIj4KICAgICAgICAgICAgICAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJwbGFjZWhvbGRlclRleHQiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+cmVhci5maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImNsZWFyQnV0dG9uRW5hYmxlZCI+CiAgICAgICAgICAgICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjEiIGNvbHVtbj0iMiI+CiAgICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJyZWFyX2Rvd25sb2FkIj4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkRvd25sb2FkPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjAiIGNvbHNwYW49IjUiPgogICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRR3JhcGhpY3NWaWV3IiBuYW1lPSJyZWFyX3ZpZXciPgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9Im1pbmltdW1TaXplIj4KICAgICAgICAgICAgICAgICAgICA8c2l6ZT4KICAgICAgICAgICAgICAgICAgICAgPHdpZHRoPjA8L3dpZHRoPgogICAgICAgICAgICAgICAgICAgICA8aGVpZ2h0PjIwMDwvaGVpZ2h0PgogICAgICAgICAgICAgICAgICAgIDwvc2l6ZT4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgIDwvbGF5b3V0PgogICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPGl0ZW0gcm93PSI2IiBjb2x1bW49IjIiIGNvbHNwYW49IjciPgogICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRR3JvdXBCb3giIG5hbWU9Imdyb3VwQm94XzQiPgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRpdGxlIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPkNvcm5lcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxsYXlvdXQgY2xhc3M9IlFHcmlkTGF5b3V0IiBuYW1lPSJncmlkTGF5b3V0XzUiPgogICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSI0Ij4KICAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9ImRlbGV0ZV9jb3JuZXIiPgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZGVsZXRlIGNvcm5lcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZGVsZXRlIGNvcm5lcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+ZGVsZXRlIGNvcm5lcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5kZWxldGUgY29ybmVyPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5kZWxldGUgY29ybmVyPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+RGVsZXRlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjMiPgogICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUHVzaEJ1dHRvbiIgbmFtZT0idXBkYXRlX2Nvcm5lciI+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz51cGRhdGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICAgICA8aXRlbSByb3c9IjEiIGNvbHVtbj0iMCI+CiAgICAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFMaW5lRWRpdCIgbmFtZT0iY29ybmVyIj4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBjb3JuZXIgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGNvcm5lciBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgY29ybmVyIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGNvcm5lciBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgY29ybmVyIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZHJhZ0VuYWJsZWQiPgogICAgICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InBsYWNlaG9sZGVyVGV4dCI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5jb3JuZXIuZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJjbGVhckJ1dHRvbkVuYWJsZWQiPgogICAgICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjAiIGNvbHNwYW49IjUiPgogICAgICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRR3JhcGhpY3NWaWV3IiBuYW1lPSJjb3JuZXJfdmlldyI+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ibWluaW11bVNpemUiPgogICAgICAgICAgICAgICAgICAgIDxzaXplPgogICAgICAgICAgICAgICAgICAgICA8d2lkdGg+MDwvd2lkdGg+CiAgICAgICAgICAgICAgICAgICAgIDxoZWlnaHQ+MjAwPC9oZWlnaHQ+CiAgICAgICAgICAgICAgICAgICAgPC9zaXplPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSIxIj4KICAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9ImJyb3dzZV9jb3JuZXIiPgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgICAgIDxzdHJpbmc+YnJvd3NlIGNvcm5lciBmaWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgY29ybmVyIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBjb3JuZXIgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5icm93c2UgY29ybmVyIGZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPmJyb3dzZSBjb3JuZXIgZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICAgICA8c3RyaW5nPkJyb3dzZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSIyIj4KICAgICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9ImNvcm5lcl9kb3dubG9hZCI+CiAgICAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgICAgPHN0cmluZz5Eb3dubG9hZDwvc3RyaW5nPgogICAgICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgICAgPC9sYXlvdXQ+CiAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMiI+CiAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFDb21ib0JveCIgbmFtZT0iY2FuX2hvbGRfZ2xhc3MiPgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+Y2FuIGhvbGQgZ2xhc3M8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmNhbiBob2xkIGdsYXNzPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5jYW4gaG9sZCBnbGFzczwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5jYW4gaG9sZCBnbGFzczwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+Y2FuIGhvbGQgZ2xhc3M8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgICAgIDwvaXRlbT4KICAgICAgICAgICAgICA8aXRlbSByb3c9IjkiIGNvbHVtbj0iMSIgY29sc3Bhbj0iOCI+CiAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFMaW5lRWRpdCIgbmFtZT0ic3RhaW4iPgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+c3RhaW48L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPnN0YWluPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5zdGFpbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5zdGFpbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+c3RhaW48L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iZHJhZ0VuYWJsZWQiPgogICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9InBsYWNlaG9sZGVyVGV4dCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5zdGFpbjwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJjbGVhckJ1dHRvbkVuYWJsZWQiPgogICAgICAgICAgICAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxIiBjb2x1bW49IjIiPgogICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9InJlYXJfaW5uZXJfcHJvZmlsZSI+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5yZWFyIGlubmVyIHByb2ZpbGU8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPnJlYXIgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+cmVhciBpbm5lciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPnJlYXIgaW5uZXIgcHJvZmlsZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+cmVhciBpbm5lciBwcm9maWxlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjciPgogICAgICAgICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ29tYm9Cb3giIG5hbWU9Indvb2RfdHlwZSI+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz53b29kIHR5cGU8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPndvb2QgdHlwZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+d29vZCB0eXBlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPndvb2QgdHlwZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+d29vZCB0eXBlPC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICA8L3dpZGdldD4KICAgICAgICAgICAgICA8L2l0ZW0+CiAgICAgICAgICAgICAgPGl0ZW0gcm93PSIxMiIgY29sdW1uPSI3IiBjb2xzcGFuPSIyIj4KICAgICAgICAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9ImRlbGV0ZV9pdGVtIj4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPmRlbGV0ZSBpdGVtIGluIGludmVudG9yeTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+ZGVsZXRlIGl0ZW0gaW4gaW52ZW50b3J5PC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5kZWxldGUgaXRlbSBpbiBpbnZlbnRvcnk8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+ZGVsZXRlIGl0ZW0gaW4gaW52ZW50b3J5PC9zdHJpbmc+CiAgICAgICAgICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5kZWxldGUgaXRlbSBpbiBpbnZlbnRvcnk8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICAgICAgICAgPHN0cmluZz5EZWxldGUgSXRlbTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgIDxpdGVtIHJvdz0iMTIiIGNvbHVtbj0iMCIgY29sc3Bhbj0iMiI+CiAgICAgICAgICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJ1cGRhdGVfc2VydmVyIj4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPnVwZGF0ZSBvbiBzZXJ2ZXI8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPnVwZGF0ZSBvbiBzZXJ2ZXI8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgICAgICAgICA8c3RyaW5nPnVwZGF0ZSBvbiBzZXJ2ZXI8L3N0cmluZz4KICAgICAgICAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+dXBkYXRlIG9uIHNlcnZlcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgICAgICAgIDxzdHJpbmc+dXBkYXRlIG9uIHNlcnZlcjwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgICAgICAgICA8c3RyaW5nPlVwZGF0ZTwvc3RyaW5nPgogICAgICAgICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgICAgICAgPC93aWRnZXQ+CiAgICAgICAgICAgICAgPC9pdGVtPgogICAgICAgICAgICAgPC9sYXlvdXQ+CiAgICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgIDwvd2lkZ2V0PgogICAgICAgICAgPC9pdGVtPgogICAgICAgICA8L2xheW91dD4KICAgICAgICA8L3dpZGdldD4KICAgICAgIDwvaXRlbT4KICAgICAgIDxpdGVtIHJvdz0iMSIgY29sdW1uPSIwIj4KICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRQ2hlY2tCb3giIG5hbWU9ImVkaXQiPgogICAgICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgICAgICA8c3RyaW5nPkVkaXQ8L3N0cmluZz4KICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICA8L3dpZGdldD4KICAgICAgIDwvaXRlbT4KICAgICAgPC9sYXlvdXQ+CiAgICAgPC93aWRnZXQ+CiAgICAgPHdpZGdldCBjbGFzcz0iUVdpZGdldCIgbmFtZT0idGFiXzIiPgogICAgICA8YXR0cmlidXRlIG5hbWU9InRpdGxlIj4KICAgICAgIDxzdHJpbmc+QXNRUjwvc3RyaW5nPgogICAgICA8L2F0dHJpYnV0ZT4KICAgICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRMYXlvdXRfOSI+CiAgICAgICA8aXRlbSByb3c9IjAiIGNvbHVtbj0iMCI+CiAgICAgICAgPHdpZGdldCBjbGFzcz0iUUdyYXBoaWNzVmlldyIgbmFtZT0iYXNfdmlldyIvPgogICAgICAgPC9pdGVtPgogICAgICA8L2xheW91dD4KICAgICA8L3dpZGdldD4KICAgICA8d2lkZ2V0IGNsYXNzPSJRV2lkZ2V0IiBuYW1lPSJ0YWJfMyI+CiAgICAgIDxhdHRyaWJ1dGUgbmFtZT0idGl0bGUiPgogICAgICAgPHN0cmluZz5GaWxlczJRUjwvc3RyaW5nPgogICAgICA8L2F0dHJpYnV0ZT4KICAgICAgPGxheW91dCBjbGFzcz0iUVZCb3hMYXlvdXQiIG5hbWU9InZlcnRpY2FsTGF5b3V0Ij4KICAgICAgIDxpdGVtPgogICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQbGFpblRleHRFZGl0IiBuYW1lPSJmaWxlczJxcl9zdGFnZV92aWV3ZXIiPgogICAgICAgICA8cHJvcGVydHkgbmFtZT0icmVhZE9ubHkiPgogICAgICAgICAgPGJvb2w+dHJ1ZTwvYm9vbD4KICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgPHByb3BlcnR5IG5hbWU9InBsYWNlaG9sZGVyVGV4dCI+CiAgICAgICAgICA8c3RyaW5nPndhdGNoIGl0IGdvPC9zdHJpbmc+CiAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgPC93aWRnZXQ+CiAgICAgICA8L2l0ZW0+CiAgICAgICA8aXRlbT4KICAgICAgICA8d2lkZ2V0IGNsYXNzPSJRUHJvZ3Jlc3NCYXIiIG5hbWU9ImZpbGVzMnFyX3Byb2dyZXNzIj4KICAgICAgICAgPHByb3BlcnR5IG5hbWU9InZhbHVlIj4KICAgICAgICAgIDxudW1iZXI+MDwvbnVtYmVyPgogICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgIDwvd2lkZ2V0PgogICAgICAgPC9pdGVtPgogICAgICAgPGl0ZW0+CiAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9ImZpbGVzMnFyX2Rvd25sb2FkX2VuZ3JhdmluZ196aXAiPgogICAgICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgICAgICA8c3RyaW5nPmRvd25sb2FkIHppcHBlZCBxcnMgZm9yIGVuZ3JhdmluZyB6aXBmaWxlPC9zdHJpbmc+CiAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICAgICAgPHN0cmluZz5kb3dubG9hZCB6aXBwZWQgcXJzIGZvciBlbmdyYXZpbmcgemlwZmlsZTwvc3RyaW5nPgogICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgIDxzdHJpbmc+ZG93bmxvYWQgemlwcGVkIHFycyBmb3IgZW5ncmF2aW5nIHppcGZpbGU8L3N0cmluZz4KICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgICAgIDxzdHJpbmc+ZG93bmxvYWQgemlwcGVkIHFycyBmb3IgZW5ncmF2aW5nIHppcGZpbGU8L3N0cmluZz4KICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgICAgICA8c3RyaW5nPmRvd25sb2FkIHppcHBlZCBxcnMgZm9yIGVuZ3JhdmluZyB6aXBmaWxlPC9zdHJpbmc+CiAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgIDxzdHJpbmc+RG93bmxvYWQgRW5ncmF2aW5nIFppcDwvc3RyaW5nPgogICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgIDwvd2lkZ2V0PgogICAgICAgPC9pdGVtPgogICAgICAgPGl0ZW0+CiAgICAgICAgPHdpZGdldCBjbGFzcz0iUVB1c2hCdXR0b24iIG5hbWU9ImZpbGVzMnFyX2Rvd25sb2FkX2Nvcm5lciI+CiAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgIDxzdHJpbmc+ZG93bmxvYWQgemlwcGVkIHFycyBmb3IgY29ybmVyIGZpbGU8L3N0cmluZz4KICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICA8c3RyaW5nPmRvd25sb2FkIHppcHBlZCBxcnMgZm9yIGNvcm5lciBmaWxlPC9zdHJpbmc+CiAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgICAgPHN0cmluZz5kb3dubG9hZCB6aXBwZWQgcXJzIGZvciBjb3JuZXIgZmlsZTwvc3RyaW5nPgogICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgPHN0cmluZz5kb3dubG9hZCB6aXBwZWQgcXJzIGZvciBjb3JuZXIgZmlsZTwvc3RyaW5nPgogICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgIDxzdHJpbmc+ZG93bmxvYWQgemlwcGVkIHFycyBmb3IgY29ybmVyIGZpbGU8L3N0cmluZz4KICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgICAgPHN0cmluZz5Eb3dubG9hZCBDb3JuZXI8L3N0cmluZz4KICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICA8L3dpZGdldD4KICAgICAgIDwvaXRlbT4KICAgICAgIDxpdGVtPgogICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJmaWxlczJxcl9kb3dubG9hZF9mcm9udCI+CiAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgICAgIDxzdHJpbmc+ZG93bmxvYWQgemlwcGVkIHFycyBmb3IgZnJvbnQgZmlsZTwvc3RyaW5nPgogICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgICAgIDxzdHJpbmc+ZG93bmxvYWQgemlwcGVkIHFycyBmb3IgZnJvbnQgZmlsZTwvc3RyaW5nPgogICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgIDxzdHJpbmc+ZG93bmxvYWQgemlwcGVkIHFycyBmb3IgZnJvbnQgZmlsZTwvc3RyaW5nPgogICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgICAgPHN0cmluZz5kb3dubG9hZCB6aXBwZWQgcXJzIGZvciBmcm9udCBmaWxlPC9zdHJpbmc+CiAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgICAgPHN0cmluZz5kb3dubG9hZCB6aXBwZWQgcXJzIGZvciBmcm9udCBmaWxlPC9zdHJpbmc+CiAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgIDxzdHJpbmc+RG93bmxvYWQgRnJvbnQ8L3N0cmluZz4KICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICA8L3dpZGdldD4KICAgICAgIDwvaXRlbT4KICAgICAgIDxpdGVtPgogICAgICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJmaWxlczJxcl9kb3dubG9hZF9yZWFyIj4KICAgICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgICAgPHN0cmluZz5kb3dubG9hZCB6aXBwZWQgcXJzIGZvciByZWFyIGZpbGU8L3N0cmluZz4KICAgICAgICAgPC9wcm9wZXJ0eT4KICAgICAgICAgPHByb3BlcnR5IG5hbWU9InN0YXR1c1RpcCI+CiAgICAgICAgICA8c3RyaW5nPmRvd25sb2FkIHppcHBlZCBxcnMgZm9yIHJlYXIgZmlsZTwvc3RyaW5nPgogICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgICAgIDxzdHJpbmc+ZG93bmxvYWQgemlwcGVkIHFycyBmb3IgcmVhciBmaWxlPC9zdHJpbmc+CiAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICAgICA8c3RyaW5nPmRvd25sb2FkIHppcHBlZCBxcnMgZm9yIHJlYXIgZmlsZTwvc3RyaW5nPgogICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZURlc2NyaXB0aW9uIj4KICAgICAgICAgIDxzdHJpbmc+ZG93bmxvYWQgemlwcGVkIHFycyBmb3IgcmVhciBmaWxlPC9zdHJpbmc+CiAgICAgICAgIDwvcHJvcGVydHk+CiAgICAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgICAgIDxzdHJpbmc+RG93bmxvYWQgUmVhcjwvc3RyaW5nPgogICAgICAgICA8L3Byb3BlcnR5PgogICAgICAgIDwvd2lkZ2V0PgogICAgICAgPC9pdGVtPgogICAgICA8L2xheW91dD4KICAgICA8L3dpZGdldD4KICAgIDwvd2lkZ2V0PgogICA8L2l0ZW0+CiAgIDxpdGVtIHJvdz0iMiIgY29sdW1uPSIxIj4KICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJzYXZlX3FyY29kZSI+CiAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICA8c3RyaW5nPnNhdmUgcXJjb2RlPC9zdHJpbmc+CiAgICAgPC9wcm9wZXJ0eT4KICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgPHN0cmluZz5zYXZlIHFyY29kZTwvc3RyaW5nPgogICAgIDwvcHJvcGVydHk+CiAgICAgPHByb3BlcnR5IG5hbWU9IndoYXRzVGhpcyI+CiAgICAgIDxzdHJpbmc+c2F2ZSBxcmNvZGU8L3N0cmluZz4KICAgICA8L3Byb3BlcnR5PgogICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgIDxzdHJpbmc+c2F2ZSBxcmNvZGU8L3N0cmluZz4KICAgICA8L3Byb3BlcnR5PgogICAgIDxwcm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICA8c3RyaW5nPnNhdmUgcXJjb2RlPC9zdHJpbmc+CiAgICAgPC9wcm9wZXJ0eT4KICAgICA8cHJvcGVydHkgbmFtZT0idGV4dCI+CiAgICAgIDxzdHJpbmc+U2F2ZSBRUkNvZGU8L3N0cmluZz4KICAgICA8L3Byb3BlcnR5PgogICAgPC93aWRnZXQ+CiAgIDwvaXRlbT4KICAgPGl0ZW0gcm93PSIyIiBjb2x1bW49IjQiPgogICAgPHdpZGdldCBjbGFzcz0iUUNoZWNrQm94IiBuYW1lPSJvcGVuX2lua3NjYXBlIj4KICAgICA8cHJvcGVydHkgbmFtZT0idG9vbFRpcCI+CiAgICAgIDxzdHJpbmc+b3BlbiBpbmtzY2FwZSB3aGVuIGRvbmU8L3N0cmluZz4KICAgICA8L3Byb3BlcnR5PgogICAgIDxwcm9wZXJ0eSBuYW1lPSJzdGF0dXNUaXAiPgogICAgICA8c3RyaW5nPm9wZW4gaW5rc2NhcGUgd2hlbiBkb25lPC9zdHJpbmc+CiAgICAgPC9wcm9wZXJ0eT4KICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgPHN0cmluZz5vcGVuIGlua3NjYXBlIHdoZW4gZG9uZTwvc3RyaW5nPgogICAgIDwvcHJvcGVydHk+CiAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVOYW1lIj4KICAgICAgPHN0cmluZz5vcGVuIGlua3NjYXBlIHdoZW4gZG9uZTwvc3RyaW5nPgogICAgIDwvcHJvcGVydHk+CiAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlwdGlvbiI+CiAgICAgIDxzdHJpbmc+b3BlbiBpbmtzY2FwZSB3aGVuIGRvbmU8L3N0cmluZz4KICAgICA8L3Byb3BlcnR5PgogICAgIDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgPHN0cmluZz5PcGVuIElua3NhcGUKV2hlbiBEb25lPC9zdHJpbmc+CiAgICAgPC9wcm9wZXJ0eT4KICAgICA8cHJvcGVydHkgbmFtZT0iY2hlY2tlZCI+CiAgICAgIDxib29sPnRydWU8L2Jvb2w+CiAgICAgPC9wcm9wZXJ0eT4KICAgIDwvd2lkZ2V0PgogICA8L2l0ZW0+CiAgPC9sYXlvdXQ+CiA8L3dpZGdldD4KIDxyZXNvdXJjZXMvPgogPGNvbm5lY3Rpb25zLz4KPC91aT4K'''
Window()
