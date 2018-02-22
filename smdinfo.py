#!/usr/bin/env python

"""
SMDInfo
Small program with TkInter GUI for viewing SMD files properties.
SMD - StudioMDL Data, stores 3D models in ASCII for Valve Source Engine.
"""


import Tkinter
import ttk
import tkMessageBox
import tkFileDialog
import os.path
import sys


__version__ = '0.1'


# - Information ----------------------------------------------------------------
INFO_LICENSE = \
'SMDInfo ' + __version__ + '\n\n'                        + \
'Created by vlanski (https://github.com/vlanski)\n'      + \
'Icons by FatCow (http://www.fatcow.com/free-icons)\n\n' + \
'SMDInfo is released under MIT License'
# ------------------------------------------------------------------------------


# - Base64 GIF Icons -----------------------------------------------------------
ICONS_BASE64 = {
'main': 'R0lGODlhEAAQAOZ0ACyPADCSAKtxACSTAABqAKdtAKlsAC2SACqQALNsAFnFAF/IAL' + \
        '1nAFO5AFW8AE+lACqSAJvTU2ewC1ixAEmwAHTPACqUAFK6AFC6AFW1AFG1AFzPACyT' + \
        'AFvDAGrTAFjEADihAFjGACJ1ADCQAO6cAPiuEmLAAIfBQlq1AJ7cTf+qFIPdAGfSAA' + \
        'ubAJjiN0izAJHLS5zZUpDLR0WhAJ3bSonFPkauAJrVUqDjQ2u7AACSACR6AD6hADiV' + \
        'AEu6AEqxAFPAACWLACyRAHjPAKluADKVACiRAKlwAK9pAGjVAIjEQXrAFSV5AIrMND' + \
        'ygALBoAFa/AFvFAG3LAFGjAGW7AIPbAGazAGe7AJfXRZ/jQSd6AEWvAEy5AEmnAFG7' + \
        'AEuyAOegAFGtAE+zAJ/dSVrIAE61AJjSUIDcAF7JAFrEAFu4AIzESp7fPkyzAGDHAE' + \
        'muAFfAAJTOSpjTT4fEPwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'ACH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZW' + \
        'hpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczpt' + \
        'ZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxMzIgNzkuMTU5Mjg0LC' + \
        'AyMDE2LzA0LzE5LTEzOjEzOjQwICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9' + \
        'Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cm' + \
        'RmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5h' + \
        'ZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY2' + \
        '9tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94' + \
        'YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZS' + \
        'BQaG90b3Nob3AgQ0MgMjAxNS41IChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0i' + \
        'eG1wLmlpZDpBOUFGNDFEQjE1QTgxMUU4QUJDQ0ZBRkZGNjFFNDlEQSIgeG1wTU06RG' + \
        '9jdW1lbnRJRD0ieG1wLmRpZDpBOUFGNDFEQzE1QTgxMUU4QUJDQ0ZBRkZGNjFFNDlE' + \
        'QSI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOk' + \
        'E5QUY0MUQ5MTVBODExRThBQkNDRkFGRkY2MUU0OURBIiBzdFJlZjpkb2N1bWVudElE' + \
        'PSJ4bXAuZGlkOkE5QUY0MURBMTVBODExRThBQkNDRkFGRkY2MUU0OURBIi8+IDwvcm' + \
        'RmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQg' + \
        'ZW5kPSJyIj8+Af/+/fz7+vn49/b19PPy8fDv7u3s6+rp6Ofm5eTj4uHg397d3Nva2d' + \
        'jX1tXU09LR0M/OzczLysnIx8bFxMPCwcC/vr28u7q5uLe2tbSzsrGwr66trKuqqain' + \
        'pqWko6KhoJ+enZybmpmYl5aVlJOSkZCPjo2Mi4qJiIeGhYSDgoGAf359fHt6eXh3dn' + \
        'V0c3JxcG9ubWxramloZ2ZlZGNiYWBfXl1cW1pZWFdWVVRTUlFQT05NTEtKSUhHRkVE' + \
        'Q0JBQD8+PTw7Ojk4NzY1NDMyMTAvLi0sKyopKCcmJSQjIiEgHx4dHBsaGRgXFhUUEx' + \
        'IREA8ODQwLCgkIBwYFBAMCAQAAIfkEAQAAdAAsAAAAABAAEAAAB6uAdIKDgkIACISJ' + \
        'g1NxMWMPioIHRRAnV1wVWQCKARIRKU1bDQpnM4o9cxkdLl8YIRtBiSIBYS9AHm9UMD' + \
        'c0kII7nmZLMnJYNSg+UjiIdAdKGh9rOSZDbDZeUSubdAETZWlWPxcKVWoOC0kjglpO' + \
        'DQtdYg5uLBRwaDyETBwDFm1QZCCMDIAQiQEdAi10EKBjMBKdBE9UkECSwOEgAyXAGL' + \
        'AoSACRAgWOCOBIMhAAOw==',
'open': 'R0lGODlhEAAQAOZTAP/93dCUPc+TQM+TO86SPcuKL//wuc+SOs+SO86SPtGVQP/208' + \
        '+SPP/32M+SP//52c+SPtCTQP/31frUaPnQXf/73NCVPv3bcNGWQMuKMfzXav/yqv/0' + \
        'vv/wsP/0q82PO//+3f/62/3qtP3cdf/72M2ONfrUa8uLMNCUPvjPX/zbc8yNN//wtM' + \
        '6SP//3zv/1qP/83P/21P/yrdCTO//4yc2PNf/zuf/0sP/42vrUav/yp82ONsuKMP/7' + \
        'qd2qUP/6qP/0pP/31MuMNf//4//0tf/41t2oSM+SPfnRYv/wt/vXbNCUQP/ylf/jev' + \
        '/qi//phf/qiP/mf/7edP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'ACH5BAEAAFMALAAAAAAQABAAAAe2gEsBBwcBS1OIiYoBMA0NISUHCAOUAzMWhwhFFC' + \
        'kiOBUAoaEgQxhTCC4TJjkaRhk8BbEnNQpTKDQXKiM+Dw8SQTELCyQBUwo7QisfBgZI' + \
        'zs8GDFMBSdXVStjZSklHUwwcUuHi41Is3Uc2Terr7E0d50RR8vP0UTLdBDdP+/z9Tx' + \
        'sEphDwAKWgwYNQdASE8MKJw4cQnQCBMGVJDyYYM2pk8uPQkiUJEjgQICACSQctEnxU' + \
        'xLIlokAAOw==',
'quit': 'R0lGODlhEAAQAPePALCDSlVVV1FSU0pKTFhZW1xdX2BhYkRGSDg9Q05OT2NkZltbWm' + \
        'lqbF9hYmJkZz1CSlpcX6x+SK+CSrGET9O1lbKFTldZW+/awGJnbklPVWhqbUZKUE9R' + \
        'U1thaPLbwcaUWLuKT82bX+vTuEVLUuvVuZt0R7yOWPXauap9R/e5IsKQVDY7QqyATF' + \
        'pgZTE4Q62BTlddZNKcXtWgYMmXXVZYW6R+Tk9SUztBSEFFTKh8RsWVXMKfc2Vqb6uC' + \
        'UMGQWbeKUsmYXaZ3RVZZXL+ccLqMVcqWWqFxQNmkaCwzPE1NT0hJTDY8Q0xNT0FGTe' + \
        'rRs7iJUUpPV7SHUbSGUJ5wPr6PW9e8ns2aW1paW1RVV7CDS8yaXK6DTcCQV/Hfyal9' + \
        'RKt/SVJYYKJsOs+viEJFR9/EpsGRXKV5QqB5SKyASXZoV76NUVtdX7mVaLKMXU1TWz' + \
        'c8Q66CSltbW7WGTsmWWMimfvW3IGhqbKl6RbqJTKF1P9WiZU1SWcSUWsWUV6V2Q9Ge' + \
        'YllbXV5jatihX1FWXebMr0NFSKJ0QkhITFpbXMyVVJ9uPNqwf1NUV1ZbYryNVP///w' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAI8ALAAA' + \
        'AAAQABAAAAjSAB8JHEhwYJc8AwHAAcAQgAQvQ0g48WBm4BcXbxBoXIHkxKJEF3IMjH' + \
        'Cj0IGTY5YI0jJHBJqBKHAoGUDz0AMZQD4QyjLwzoYkCYIyaRJDhw8ycgYGyWBDgFMO' + \
        'I6yUqVPlyUA/e7AE2MoIShEqKSg4GmhokAUCaGm46WOihBguA400WlOgLgQwKoi8oM' + \
        'Nn4JQWDQwIbgBDzY8oO2YMVBTIgYLHDjqAkDKBTYiBYXhoYMDZDgY8Fba0+TMQEKI4' + \
        'C1JfEZKmBoseegrKHnjmyOzbAgMCADs=',
'copy': 'R0lGODlhEAAQANU9ANns8w50rgVwrCKAtSB/teby+Cl+reXy+MTc7KzV5a7W5rDX5u' + \
        'fz+M3m8LHX58fj7c3n8Njs822rz7HY59Do8bjc6tzu9OHw9s/n8MPc7Bp7s/T7/NPq' + \
        '8bzd6xJ2sCGAtbrd6rDX5x5/tLze673d6xB2sNrs8+n0+c/o8bPZ6Mjj7TKKuyp+rb' + \
        'vc6xJ3sNHo8SWCtuTx9xF2sOf1+N7w9h9/tMfk7xx9sySBtq/W5h9/tR5+tP//////' + \
        '/wAAAAAAACH5BAEAAD0ALAAAAAAQABAAAAabQBZOt9vVBreecqnE8Z5QRJKp1PEmkx' + \
        'BPwMtMmTteh9TiSbi3DwGpDD9UjwtUFk2GURQKpgHhBUZbPFJhAAAmhRF+NmZcA2EH' + \
        'BQwMBQd+HDFQImEJOZ05CX40L3w8O1YKOQsLOQp+MxYAiTtOULUlGyeUpQY4BDpEGi' + \
        '4eKxUOn6VUPQM8IBUpxq06yTC1tTjJvL6/OgQ4BsngS0EAOw==',
'del':  'R0lGODlhEAAQAOZWAAB7ugB7tgB5tQB1uABztAB1tT83M6vq/2fC49jb2wB6tvr///' + \
        '7//wB3tUM4M/j//wB6tgB7u3Z4eQB9uAB4tllWWGXC5AB0t42CewB2ud/Y1QB6tff/' + \
        '/5SVl4SEhIOCgen//7WqouX6/6nl/6Pe9QB4t+T5//H8//z//5XV8AB7tvT19mvG5z' + \
        '81MD42MAB9u7S/yD41MP///+f6/3/D5JXa90E2MEQ5M/Hv7t7X06bf9mHB5aff9oKC' + \
        'gl7C6IqKioaGhmXG7AB8twB9twB6tej6/7a/x0A3M6bk/oKBfwB9uOH6/wB+unHE5u' + \
        'v9/wB1tebXzdLs+IiIiHd2d4TN7Z7O5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'ACH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZW' + \
        'hpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczpt' + \
        'ZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxMzIgNzkuMTU5Mjg0LC' + \
        'AyMDE2LzA0LzE5LTEzOjEzOjQwICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9' + \
        'Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cm' + \
        'RmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5h' + \
        'ZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY2' + \
        '9tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94' + \
        'YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZS' + \
        'BQaG90b3Nob3AgQ0MgMjAxNS41IChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0i' + \
        'eG1wLmlpZDpGRTc3RTRBMzE3NDYxMUU4QjcwMEY2NTU3NkJDRjU3MSIgeG1wTU06RG' + \
        '9jdW1lbnRJRD0ieG1wLmRpZDpGRTc3RTRBNDE3NDYxMUU4QjcwMEY2NTU3NkJDRjU3' + \
        'MSI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOk' + \
        'ZFNzdFNEExMTc0NjExRThCNzAwRjY1NTc2QkNGNTcxIiBzdFJlZjpkb2N1bWVudElE' + \
        'PSJ4bXAuZGlkOkZFNzdFNEEyMTc0NjExRThCNzAwRjY1NTc2QkNGNTcxIi8+IDwvcm' + \
        'RmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQg' + \
        'ZW5kPSJyIj8+Af/+/fz7+vn49/b19PPy8fDv7u3s6+rp6Ofm5eTj4uHg397d3Nva2d' + \
        'jX1tXU09LR0M/OzczLysnIx8bFxMPCwcC/vr28u7q5uLe2tbSzsrGwr66trKuqqain' + \
        'pqWko6KhoJ+enZybmpmYl5aVlJOSkZCPjo2Mi4qJiIeGhYSDgoGAf359fHt6eXh3dn' + \
        'V0c3JxcG9ubWxramloZ2ZlZGNiYWBfXl1cW1pZWFdWVVRTUlFQT05NTEtKSUhHRkVE' + \
        'Q0JBQD8+PTw7Ojk4NzY1NDMyMTAvLi0sKyopKCcmJSQjIiEgHx4dHBsaGRgXFhUUEx' + \
        'IREA8ODQwLCgkIBwYFBAMCAQAAIfkEAQAAVgAsAAAAABAAEAAAB3uAVoKDhCoCKoSJ' + \
        'gyUoJxwNioQACz47TQxCkVYADzEtVVQpiIoQIi4dUzY1PEOKFE5BRxIVNyOjhAJFFh' + \
        'k5Bg4HTIpKMwhPRhcgSC+RACxPUAQmJBCaIQMwBFE0RJofMhoDSzrcmj0JOBgRSpqC' + \
        'HitJ7IRSQPGEP/X4ioEAOw==',
'info': 'R0lGODlhEAAQAOZCAEN2pvL5/X6jxebx+ISnxj5ypDtwolyJs4mpyV2JtD1xo46syo' + \
        'eoyD5yo4uqyer0+oyryoGkxH+kxISmxzxwou/3/P7//0l6qfz//9/t9oGlxV+Ks2CM' + \
        'tebz+4aoxkJ0pe/4/eDv+EF0pXSavmONtT1yo2aQuGuUunmewUV3p2KMtmmSuUR3p2' + \
        'eRuWONt2iRuEp6qUJ1pWCLtDZsoI6tyzpvol+Ls2GMtWKNtER2pkJ1pkd4qOf0++Ty' + \
        '+o+ty2OOtpGuy////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'ACH5BAEAAEIALAAAAAAQABAAAAeOgEKCg4JAhIeHQEGGiIc0QR5BPo2DC0EbMzJBC5' + \
        'QQQTcnFgo/QRCIDkEqJQYGAAAuQQ6ECBg4HyNBQSIXLCQYCIVBEQ07Oi0WBTAXBRGL' + \
        'ggwBHAAxJiA1KTkcAQyEBBUbLz0hHSs2FQSIEw8HFAoUBw8TlBoDCQ0JAxqUghIZKB' + \
        'kS9g0SwEOAQEKMDgoMBAA7',
'root': 'R0lGODlhEAAQAOZVAFCnLVCmLU+lK4fZWrflllGnLlSoMLjklonUXqnnglGoLqHmek' + \
        'WRJVGmLn/UUkqiJ2/DRZXQckmiJsDvocr0qoDDXEigJcn1qVKpL73nnEWUJbjplpTe' + \
        'aHbLSXPGTE6mK1KmLpznb6Lle87/qIvMaEykKEujKEGHJIbWW7vnmcPuoUueKrXrkJ' + \
        '3ucFitM73onG3ERFOoMFitMb7rnMr2qoHGX5bSdMTyoofaV4rcXs/2rqPudqHwdKfh' + \
        'gUqYKVKoLrr2k2i8QU+kK5LZaJLjZF2vOoTXWKDsdI7WY8n/pE2iKkqeKHO8UE+mKz' + \
        'p6H7j/iJDgY0+mLIDUUlCnLHS8Uv///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'ACH5BAEAAFUALAAAAAAQABAAAAeFgFWCg1UATQCEiYMABykHiIqEUQkcCQGRhA07PC' + \
        '2XmII+DxYSGp9VDBUEGS8EEUyKUyU2M0MICEg9KieEPzoUGxAwUg4dMjgFiQAfSyYk' + \
        'AwMsSkQGmFQ3OVBGK9SRRRchLigiTphCEwsYVUFANZgCSQqDRzQCkSBPnlUeI/mJMY' + \
        'nITH0KBAA7',
'root_err': 'R0lGODlhEAAQAOZVAMsIHcoIHv9qicwMIv80WP1+nf9hfssJH8kGHft+n/c6Xf' + \
            '9hf9wySswMIf+QrccAFP+lvv5khsUAFf98mv+fuOxVcv+IoscCF/srUPtGacwJ' + \
            'IOpKZfs2V/0yVLkHHOI9Wf+huMoKIP+Vr9IXLuVAWLEEGP+ov8EHGuonQv87Xf' + \
            'hAY/9lgssGG/+RqcgDGP9lgcsGHMgGHf8yWOkfP8oHHMwHHf+ftv9ffP+AnrUD' + \
            'FpUDFMoIHP9EZv9IavsrTuodO8YGG+5XcvIiRc0KH/+kucEEGdwvSaUGF+EcN/' + \
            '9Ha8oKH8wJHv+FpMkCGNILJdEOJv9Xd/2FpP6BoP+Ipv+Ko////wAAAAAAAAAA' + \
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAFUALAAAAAAQABAAAAeFgF' + \
            'WCg1UAMACEiYMACVIJiIqENAJJAjuRhEorLzcBmIMeFxIPOZ9VJR8FUUwFFUaK' + \
            'NU1BUxkKCioRDkeEGhAUODM/GD5CTjIHiQAsRS4bBAQTQD0DmAwiKTwdJ9SRIz' + \
            'ZQTxwLOpgxLQZDVUhUJJgIREuDBiAIkSEWnoIoJvmKDYnITH0KBAA7',
'root_empty': 'R0lGODlhEAAQANU6AL29vWxsbGhoaLCwsKOjo2RkZISEhJiYmMPDw5OTk2tr' + \
              'a7S0tKGhoWZmZrKyss/Pz4mJiZ2dnXR0dJycnG9vb4qKioaGhqurq3BwcLGx' + \
              'scrKyqCgoMLCwmJiYlxcXNLS0ltbW7+/v9PT02dnZ8DAwGVlZWNjY8fHx6+v' + \
              'r9DQ0FVVVYeHh35+fsHBwUxMTJKSko+Pj2BgYJqamsjIyNHR0ZeXl8TExGlp' + \
              'aWpqapmZmf///wAAAAAAAAAAAAAAAAAAACH5BAEAADoALAAAAAAQABAAAAZ3' + \
              'QJ1wqMMJcMTkEAcgAZBK4m1BWNyiRJzDgbpihbFCp+D56kAwQIsDYFiUtwYB' + \
              'scnlJpmTiqj4PEIGBgkJFRQHUEsCJiUydgByAVgrGhEMNQWRURIPFxgHAy5Y' + \
              'IzMDkSw2L1gCNApDAykCUTgIXjoQIrVJmUtmZkEAOw==',
'bones': 'R0lGODlhEAAQAMQSADA4PzdASDpDS0RPVykxNkFLUiYsMhgcICMoLjQ8Qy40OyAkK' + \
         'RUYGxsgJT5HTwoMD0RPWS83PgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
         'AAAAAAAAAAAAAAACH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGl' + \
         'kPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4' + \
         'PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxM' + \
         'zIgNzkuMTU5Mjg0LCAyMDE2LzA0LzE5LTEzOjEzOjQwICAgICAgICAiPiA8cmRmOl' + \
         'JERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN' + \
         '5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4' + \
         'bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJod' + \
         'HRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cD' + \
         'ovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1wOkN' + \
         'yZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxNS41IChXaW5kb3dzKSIg' + \
         'eG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo3ODg4OTk5QjE1QTgxMUU4QkY3NkMyR' + \
         'kMyM0MyNDZBQyIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo3ODg4OTk5QzE1QT' + \
         'gxMUU4QkY3NkMyRkMyM0MyNDZBQyI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjp' + \
         'pbnN0YW5jZUlEPSJ4bXAuaWlkOjc4ODg5OTk5MTVBODExRThCRjc2QzJGQzIzQzI0' + \
         'NkFDIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjc4ODg5OTlBMTVBODExRThCR' + \
         'jc2QzJGQzIzQzI0NkFDIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+ID' + \
         'wveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+Af/+/fz7+vn49/b19PPy8fD' + \
         'v7u3s6+rp6Ofm5eTj4uHg397d3Nva2djX1tXU09LR0M/OzczLysnIx8bFxMPCwcC/' + \
         'vr28u7q5uLe2tbSzsrGwr66trKuqqainpqWko6KhoJ+enZybmpmYl5aVlJOSkZCPj' + \
         'o2Mi4qJiIeGhYSDgoGAf359fHt6eXh3dnV0c3JxcG9ubWxramloZ2ZlZGNiYWBfXl' + \
         '1cW1pZWFdWVVRTUlFQT05NTEtKSUhHRkVEQ0JBQD8+PTw7Ojk4NzY1NDMyMTAvLi0' + \
         'sKyopKCcmJSQjIiEgHx4dHBsaGRgXFhUUExIREA8ODQwLCgkIBwYFBAMCAQAAIfkE' + \
         'AQAAEgAsAAAAABAAEAAABUGgJI7SAA1kOharmjoj7I4CLdWzFOxikIuJUVAVARiPR' + \
         'pditPwRRs+fYTT9jRAPhFW0kHS3DUl4e5CUtwxJepsLAQA7',
'mats': 'R0lGODlhEAAQAOZOAD636zO27Du36zi360C469bw/za27Lfq/9jx/5nc/8nr/8/u/4' + \
        'XT/4HR/53e/6Dg/7bp/8vs/6ni//b7//j8/4vV/3nP/3HL/9Pv/8zt/4/X/93z/9Xv' + \
        '/5Pa/8Do/5La/9Lu/8Dn/9Tv/9Du/zm27IjU/8rr/2vJ/3PN/37Q/73r//f8/8Hr//' + \
        'z9/8Du/4PT/+P1/8Tp/6rj/7vl//H6/8ru/+r3/8nt//X6/9Xw/8Dr/9Hv/83u/77r' + \
        '/8jt/8Xs/7/q/8Hu/5vc/9zy/87v/9/z/+H0//3+/8vt/+34/4vX/+f2/8Tr/9rx/w' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'ACH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZW' + \
        'hpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczpt' + \
        'ZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxMzIgNzkuMTU5Mjg0LC' + \
        'AyMDE2LzA0LzE5LTEzOjEzOjQwICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9' + \
        'Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cm' + \
        'RmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5h' + \
        'ZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY2' + \
        '9tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94' + \
        'YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZS' + \
        'BQaG90b3Nob3AgQ0MgMjAxNS41IChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0i' + \
        'eG1wLmlpZDo4RDNFMDhENjE1QkMxMUU4QTkwMUQ3NkUzRTRBMEQ1NCIgeG1wTU06RG' + \
        '9jdW1lbnRJRD0ieG1wLmRpZDo4RDNFMDhENzE1QkMxMUU4QTkwMUQ3NkUzRTRBMEQ1' + \
        'NCI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOj' + \
        'hEM0UwOEQ0MTVCQzExRThBOTAxRDc2RTNFNEEwRDU0IiBzdFJlZjpkb2N1bWVudElE' + \
        'PSJ4bXAuZGlkOjhEM0UwOEQ1MTVCQzExRThBOTAxRDc2RTNFNEEwRDU0Ii8+IDwvcm' + \
        'RmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQg' + \
        'ZW5kPSJyIj8+Af/+/fz7+vn49/b19PPy8fDv7u3s6+rp6Ofm5eTj4uHg397d3Nva2d' + \
        'jX1tXU09LR0M/OzczLysnIx8bFxMPCwcC/vr28u7q5uLe2tbSzsrGwr66trKuqqain' + \
        'pqWko6KhoJ+enZybmpmYl5aVlJOSkZCPjo2Mi4qJiIeGhYSDgoGAf359fHt6eXh3dn' + \
        'V0c3JxcG9ubWxramloZ2ZlZGNiYWBfXl1cW1pZWFdWVVRTUlFQT05NTEtKSUhHRkVE' + \
        'Q0JBQD8+PTw7Ojk4NzY1NDMyMTAvLi0sKyopKCcmJSQjIiEgHx4dHBsaGRgXFhUUEx' + \
        'IREA8ODQwLCgkIBwYFBAMCAQAAIfkEAQAATgAsAAAAABAAEAAAB8qABAMBhIWGAQME' + \
        'TgMtOBMUFBOPkRMrRwNOBkkzIRcXHh6eHiEnNAaZSzEKFhYKq60KKDanBjApDRERDb' + \
        'i6DSZGpyRDLwwZGQzFxwwRTSSLIkgLFRUL0tQLJQWYA0Q8IxoaICDgICNKO5gCNR0d' + \
        'GBgfH+4fHSI36T5CCRwcCfr8CQV+CHAigEWOAg4cFECoECGTgQKAIEDw4MHEihd1QO' + \
        'whQ8KGDRI8gpRQRMVAAkEOHIAAQSVLly4UESAAoKbNmwBmOtnJs6fPnYEAADs=',
'flexes': 'R0lGODlhEAAQANUtALH/3QCKWQC3d////4uit97p8Y+luO/0+cDV35CluQC4d/7/' + \
          '/wCLWdLf6ezy97PCz4qhtgCJVgCKV8TW4gC5dABySACydv3+/5aoueTv9OXv846j' + \
          't52yw5KjtfH19wC6euDr8qn/2qi6ypent/L29wC4d6CzwwCHUbP/3YyjtwCdZ9Pg' + \
          '6bv/3gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
          'AAAAAAAAAAAAAAAAACH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78i' + \
          'IGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxu' + \
          'czp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42' + \
          'LWMxMzIgNzkuMTU5Mjg0LCAyMDE2LzA0LzE5LTEzOjEzOjQwICAgICAgICAiPiA8' + \
          'cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjIt' + \
          'cmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4' + \
          'bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnht' + \
          'cE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJl' + \
          'Zj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVm' + \
          'IyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxNS41IChX' + \
          'aW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo2M0I1QUI4MzE1QkQx' + \
          'MUU4QUY3Mjk2MkFENjlFMkE0NCIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo2' + \
          'M0I1QUI4NDE1QkQxMUU4QUY3Mjk2MkFENjlFMkE0NCI+IDx4bXBNTTpEZXJpdmVk' + \
          'RnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjYzQjVBQjgxMTVCRDExRThB' + \
          'RjcyOTYyQUQ2OUUyQTQ0IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjYzQjVB' + \
          'QjgyMTVCRDExRThBRjcyOTYyQUQ2OUUyQTQ0Ii8+IDwvcmRmOkRlc2NyaXB0aW9u' + \
          'PiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+Af/+' + \
          '/fz7+vn49/b19PPy8fDv7u3s6+rp6Ofm5eTj4uHg397d3Nva2djX1tXU09LR0M/O' + \
          'zczLysnIx8bFxMPCwcC/vr28u7q5uLe2tbSzsrGwr66trKuqqainpqWko6KhoJ+e' + \
          'nZybmpmYl5aVlJOSkZCPjo2Mi4qJiIeGhYSDgoGAf359fHt6eXh3dnV0c3JxcG9u' + \
          'bWxramloZ2ZlZGNiYWBfXl1cW1pZWFdWVVRTUlFQT05NTEtKSUhHRkVEQ0JBQD8+' + \
          'PTw7Ojk4NzY1NDMyMTAvLi0sKyopKCcmJSQjIiEgHx4dHBsaGRgXFhUUExIREA8O' + \
          'DQwLCgkIBwYFBAMCAQAAIfkEAQAALQAsAAAAABAAEAAABkvAlnBILBqPyKRymSRA' + \
          'CMzHYCpqVRiSgDYQOWFIl8HCs1GxUIB0OtTRHByHTMryKQnughJltCqACg0GSiYI' + \
          'EwgcTAkGCUyNjo+QTEEAOw==',
'bone': 'R0lGODlhEAAQAMQUAACEugCo5gC17ACs6ACDulfF7gCFugCTyFnH8DTB7wC17QC67Q' + \
        'CSyQCo5VzJ8QCTyQCDuQCDuUHF8wC06wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAACH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPS' + \
        'JXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJh' + \
        'ZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxMzIgNz' + \
        'kuMTU5Mjg0LCAyMDE2LzA0LzE5LTEzOjEzOjQwICAgICAgICAiPiA8cmRmOlJERiB4' + \
        'bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC' + \
        '1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0' + \
        'dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbn' + \
        'MuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFk' + \
        'b2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1wOkNyZWF0b3JUb2' + \
        '9sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxNS41IChXaW5kb3dzKSIgeG1wTU06SW5z' + \
        'dGFuY2VJRD0ieG1wLmlpZDo4NEVGNjA1OTE1QUExMUU4OTI5NEY2NzgwMjU4RkFDMS' + \
        'IgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo4NEVGNjA1QTE1QUExMUU4OTI5NEY2' + \
        'NzgwMjU4RkFDMSI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPS' + \
        'J4bXAuaWlkOjg0RUY2MDU3MTVBQTExRTg5Mjk0RjY3ODAyNThGQUMxIiBzdFJlZjpk' + \
        'b2N1bWVudElEPSJ4bXAuZGlkOjg0RUY2MDU4MTVBQTExRTg5Mjk0RjY3ODAyNThGQU' + \
        'MxIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8' + \
        'P3hwYWNrZXQgZW5kPSJyIj8+Af/+/fz7+vn49/b19PPy8fDv7u3s6+rp6Ofm5eTj4u' + \
        'Hg397d3Nva2djX1tXU09LR0M/OzczLysnIx8bFxMPCwcC/vr28u7q5uLe2tbSzsrGw' + \
        'r66trKuqqainpqWko6KhoJ+enZybmpmYl5aVlJOSkZCPjo2Mi4qJiIeGhYSDgoGAf3' + \
        '59fHt6eXh3dnV0c3JxcG9ubWxramloZ2ZlZGNiYWBfXl1cW1pZWFdWVVRTUlFQT05N' + \
        'TEtKSUhHRkVEQ0JBQD8+PTw7Ojk4NzY1NDMyMTAvLi0sKyopKCcmJSQjIiEgHx4dHB' + \
        'saGRgXFhUUExIREA8ODQwLCgkIBwYFBAMCAQAAIfkEAQAAFAAsAAAAABAAEAAABTIg' + \
        'JY5kaZ5oqq4lEAHsUzgFowLI0AwIjBKLgHBBSBkUgolAYVAdEpLEgeXysa7YrBYbAg' + \
        'A7',
'mat': 'R0lGODlhEAAQAMQXAOpKL+pJLv+JbupKMOtHLetJLv+nkP96WP9tSv+JbP+nkPhaP/9' + \
       '9Xv99Xf98Xf+NculJLv90U/pdQvpdQf9tSupGLP+tlQAAAAAAAAAAAAAAAAAAAAAAAA' + \
       'AAAAAAAAAAACH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXN' + \
       'U0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9i' + \
       'ZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxMzIgNzkuMTU' + \
       '5Mjg0LCAyMDE2LzA0LzE5LTEzOjEzOjQwICAgICAgICAiPiA8cmRmOlJERiB4bWxucz' + \
       'pyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiP' + \
       'iA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9u' + \
       'cy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmU' + \
       'uY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS' + \
       '94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZ' + \
       'SBQaG90b3Nob3AgQ0MgMjAxNS41IChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0i' + \
       'eG1wLmlpZDpGNEMxQzYxNDE1QUExMUU4QUIwN0I4ODQ1MUJCQ0RBOCIgeG1wTU06RG9' + \
       'jdW1lbnRJRD0ieG1wLmRpZDpGNEMxQzYxNTE1QUExMUU4QUIwN0I4ODQ1MUJCQ0RBOC' + \
       'I+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkY0Q' + \
       'zFDNjEyMTVBQTExRThBQjA3Qjg4NDUxQkJDREE4IiBzdFJlZjpkb2N1bWVudElEPSJ4' + \
       'bXAuZGlkOkY0QzFDNjEzMTVBQTExRThBQjA3Qjg4NDUxQkJDREE4Ii8+IDwvcmRmOkR' + \
       'lc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPS' + \
       'JyIj8+Af/+/fz7+vn49/b19PPy8fDv7u3s6+rp6Ofm5eTj4uHg397d3Nva2djX1tXU0' + \
       '9LR0M/OzczLysnIx8bFxMPCwcC/vr28u7q5uLe2tbSzsrGwr66trKuqqainpqWko6Kh' + \
       'oJ+enZybmpmYl5aVlJOSkZCPjo2Mi4qJiIeGhYSDgoGAf359fHt6eXh3dnV0c3JxcG9' + \
       'ubWxramloZ2ZlZGNiYWBfXl1cW1pZWFdWVVRTUlFQT05NTEtKSUhHRkVEQ0JBQD8+PT' + \
       'w7Ojk4NzY1NDMyMTAvLi0sKyopKCcmJSQjIiEgHx4dHBsaGRgXFhUUExIREA8ODQwLC' + \
       'gkIBwYFBAMCAQAAIfkEAQAAFwAsAAAAABAAEAAABTPgJY5kaZ5oqq4lURGspFjKpBbK' + \
       'ER1KkQYJijARSA0aDAejMVAtBA/BggWAAFjYrHa7DQEAOw==',
'flex': 'R0lGODlhEAAQAMQVAACLAACLAKPbXQCKAGPIAGzPAACLAG/HADOgAGXJAFTBAKjbbS' + \
        'GcAHzQAACKAACKAFS/AGTHAHHSAK/fdGXEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAACH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPS' + \
        'JXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJh' + \
        'ZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxMzIgNz' + \
        'kuMTU5Mjg0LCAyMDE2LzA0LzE5LTEzOjEzOjQwICAgICAgICAiPiA8cmRmOlJERiB4' + \
        'bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC' + \
        '1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0' + \
        'dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbn' + \
        'MuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFk' + \
        'b2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1wOkNyZWF0b3JUb2' + \
        '9sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxNS41IChXaW5kb3dzKSIgeG1wTU06SW5z' + \
        'dGFuY2VJRD0ieG1wLmlpZDpFRjExRjJFMjE1QUExMUU4OTdGMEQ3QkEzMjRENEE5RS' + \
        'IgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpFRjExRjJFMzE1QUExMUU4OTdGMEQ3' + \
        'QkEzMjRENEE5RSI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPS' + \
        'J4bXAuaWlkOkVGMTFGMkUwMTVBQTExRTg5N0YwRDdCQTMyNEQ0QTlFIiBzdFJlZjpk' + \
        'b2N1bWVudElEPSJ4bXAuZGlkOkVGMTFGMkUxMTVBQTExRTg5N0YwRDdCQTMyNEQ0QT' + \
        'lFIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8' + \
        'P3hwYWNrZXQgZW5kPSJyIj8+Af/+/fz7+vn49/b19PPy8fDv7u3s6+rp6Ofm5eTj4u' + \
        'Hg397d3Nva2djX1tXU09LR0M/OzczLysnIx8bFxMPCwcC/vr28u7q5uLe2tbSzsrGw' + \
        'r66trKuqqainpqWko6KhoJ+enZybmpmYl5aVlJOSkZCPjo2Mi4qJiIeGhYSDgoGAf3' + \
        '59fHt6eXh3dnV0c3JxcG9ubWxramloZ2ZlZGNiYWBfXl1cW1pZWFdWVVRTUlFQT05N' + \
        'TEtKSUhHRkVEQ0JBQD8+PTw7Ojk4NzY1NDMyMTAvLi0sKyopKCcmJSQjIiEgHx4dHB' + \
        'saGRgXFhUUExIREA8ODQwLCgkIBwYFBAMCAQAAIfkEAQAAFQAsAAAAABAAEAAABTNg' + \
        'JY5kaZ5oqq6l8RgsskwLohrCQR0CjD4NBUTReKQMhEQkQfChGAVJgcFyOVnYrHaLDQ' + \
        'EAOw==',
'none': 'R0lGODlhEAAQAMQRAGhoaHt7e5OTk6mpqZiYmLq6uqWlpaOjo7i4uLGxsbu7u3p6eq' + \
        'KiomZmZmdnZ7a2tpKSkgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + \
        'AAAAAAAAAAAAACH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPS' + \
        'JXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJh' + \
        'ZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxMzIgNz' + \
        'kuMTU5Mjg0LCAyMDE2LzA0LzE5LTEzOjEzOjQwICAgICAgICAiPiA8cmRmOlJERiB4' + \
        'bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC' + \
        '1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0' + \
        'dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbn' + \
        'MuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFk' + \
        'b2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1wOkNyZWF0b3JUb2' + \
        '9sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxNS41IChXaW5kb3dzKSIgeG1wTU06SW5z' + \
        'dGFuY2VJRD0ieG1wLmlpZDo2OEZFN0RFQTE1QUIxMUU4QUEzODg0MzYwRkQxMEREOS' + \
        'IgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo2OEZFN0RFQjE1QUIxMUU4QUEzODg0' + \
        'MzYwRkQxMEREOSI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPS' + \
        'J4bXAuaWlkOjY4RkU3REU4MTVBQjExRThBQTM4ODQzNjBGRDEwREQ5IiBzdFJlZjpk' + \
        'b2N1bWVudElEPSJ4bXAuZGlkOjY4RkU3REU5MTVBQjExRThBQTM4ODQzNjBGRDEwRE' + \
        'Q5Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8' + \
        'P3hwYWNrZXQgZW5kPSJyIj8+Af/+/fz7+vn49/b19PPy8fDv7u3s6+rp6Ofm5eTj4u' + \
        'Hg397d3Nva2djX1tXU09LR0M/OzczLysnIx8bFxMPCwcC/vr28u7q5uLe2tbSzsrGw' + \
        'r66trKuqqainpqWko6KhoJ+enZybmpmYl5aVlJOSkZCPjo2Mi4qJiIeGhYSDgoGAf3' + \
        '59fHt6eXh3dnV0c3JxcG9ubWxramloZ2ZlZGNiYWBfXl1cW1pZWFdWVVRTUlFQT05N' + \
        'TEtKSUhHRkVEQ0JBQD8+PTw7Ojk4NzY1NDMyMTAvLi0sKyopKCcmJSQjIiEgHx4dHB' + \
        'saGRgXFhUUExIREA8ODQwLCgkIBwYFBAMCAQAAIfkEAQAAEQAsAAAAABAAEAAABTNg' + \
        'JI5kaZ5oqq4l0ABsgCjIogIFAREFjAIDgXDgOwEMB8bBUDwFEo9EgAVwNFnYrHbLCg' + \
        'EAOw=='
}
# ------------------------------------------------------------------------------


# - SMD Reader Class -----------------------------------------------------------
class SMDReader():
    def __init__(self, file_name):
        # - Initial Values -----------------------------------------------------
        self.bones = []
        self.materials = []
        self.flexes = []
        self.has_flexes = False
        current_section = -1
        # ----------------------------------------------------------------------

        # - File Processing ----------------------------------------------------
        with open(file_name, 'r') as smd_file:
            for smd_str in smd_file:
                smd_str = smd_str.strip().replace('\t', ' ')
                smd_str_wo_com = smd_str

                # - Parse Comments ---------------------------------------------
                comment_ind = smd_str.find('//')
                if comment_ind == -1:
                    comment_ind = smd_str.find('#')
                if comment_ind == -1:
                    comment_ind = smd_str.find(';')

                if comment_ind != -1:
                    smd_str = smd_str[0:comment_ind]
                # --------------------------------------------------------------

                if current_section == -1:
                    # - Find Bones ---------------------------------------------
                    if smd_str.lower() == 'nodes':
                        current_section = 0
                    # ----------------------------------------------------------

                    # - Find Materials -----------------------------------------
                    if smd_str.lower() == 'triangles':
                        current_section = 1
                        tri_ind = 0

                    # - Find Flexes --------------------------------------------
                    if smd_str.lower() == 'vertexanimation':
                        self.has_flexes = True
                        current_section = 2
                        is_base_vertex = True
                    # ----------------------------------------------------------

                # - Parsing Bones Section --------------------------------------
                elif current_section == 0:
                    if smd_str.lower() == 'end':
                        current_section = -1
                    else:
                        start_bone_name = smd_str.find(' ')
                        end_bone_name = smd_str.rfind(' ')

                        bone_id = int(smd_str[0:start_bone_name])
                        bone_name = smd_str[start_bone_name+1:
                                            end_bone_name].strip().strip('"')

                        parent_id = int(smd_str[end_bone_name+1:])

                        self.bones.append((bone_id, parent_id, bone_name))
                # --------------------------------------------------------------

                # - Parsing Materials Serction ---------------------------------
                elif current_section == 1:
                    if smd_str.lower() == 'end':
                        current_section = -1
                    else:
                        if tri_ind == 0:
                            current_material = smd_str.strip()
                            is_found = False
                            for iter_material in self.materials:
                                if current_material == iter_material:
                                    is_found = True
                                    break

                            if not is_found:
                                self.materials.append(current_material)

                        tri_ind = (tri_ind + 1) % 4
                # --------------------------------------------------------------

                # - Parsing Flexes Section -------------------------------------
                elif current_section == 2:
                    if smd_str.lower() == 'end':
                        current_section = -1
                    else:
                        if smd_str.startswith('time'):
                            if is_base_vertex:
                                is_base_vertex = False
                            else:
                                start_vname = smd_str_wo_com.find('#')

                                if start_vname != -1:
                                    vertex_name = smd_str_wo_com[start_vname
                                                                 +1:].lstrip()
                                    is_vertex_dual = False
                                    plus_pos = vertex_name.find('+')

                                    if plus_pos != -1:
                                        vertex_l = vertex_name[plus_pos+1:]
                                        vertex_r = vertex_name[0:plus_pos]

                                        vertex_name = self._similar(vertex_l,
                                                                    vertex_r)
                                        is_vertex_dual = True

                                    self.flexes.append((vertex_name,
                                                        is_vertex_dual))
                                else:
                                    self.flexes.append(('unnamed flex #'
                                                       + smd_str[5:], False))
                # --------------------------------------------------------------
        # ----------------------------------------------------------------------


    # - Similar Parts ----------------------------------------------------------
    def _similar(self, s1, s2):
        """ Returns similar part of two strings """
        count = min(len(s1), len(s2))

        s = ''
        for i in xrange(0, count):
            if s1[i] == s2[i]:
                s += s1[i]

        return s
    # --------------------------------------------------------------------------
# ------------------------------------------------------------------------------


# - Menu Commands --------------------------------------------------------------
def cmd_open_smd_file(*args):
    ''' File -> Open '''
    open_dialog = tkFileDialog.Open(main_form,
                                    title='Open SMD File',
                                    filetypes=(('SMD Files','*.smd;*.vta'),
                                               ('All Files','*.*')))

    file_name = open_dialog.show()
    load_smd(file_name)


def cmd_quit(*args):
    ''' File -> Quit '''
    main_form.quit()


def cmd_copy(*args):
    ''' Edit -> Copy '''
    main_form.clipboard_clear()
    main_form.clipboard_append(smd_tree.item(smd_tree.selection())['text'])


def cmd_delete(*args):
    ''' Edit -> Delete '''
    curr_element = smd_tree.selection()
    while smd_tree.parent(curr_element) != '':
        curr_element = smd_tree.parent(curr_element)

    if tkMessageBox.askyesno('Delete', 'Do you want to delete "'
                                       + smd_tree.item(curr_element)['text']
                                       + '"'):


        # - Finding Element For Selection --------------------------------------
        if smd_tree.prev(curr_element) != '':
            sel_element = smd_tree.prev(curr_element)
        elif smd_tree.next(curr_element) != '':
            sel_element = smd_tree.next(curr_element)
        else:
            sel_element = ''
        # ----------------------------------------------------------------------

        smd_tree.selection_set(sel_element)
        smd_tree.delete(curr_element)

        # - If Tree Is Empty ---------------------------------------------------
        if len(smd_tree.get_children()) == 0:
            init_tree()
        # ----------------------------------------------------------------------


def cmd_about(*args):
    ''' Help -> About '''
    tkMessageBox.showinfo('Delete', INFO_LICENSE)
# ------------------------------------------------------------------------------


# - StatusBar text -------------------------------------------------------------
def smd_tree_select(event):
    ''' Tree Select Event '''
    curr_element = smd_tree.selection()
    path = ''

    while curr_element != '':
        curr_item = smd_tree.item(curr_element)
        if len(curr_item['values']) > 0:
            curr_text = curr_item['values'][0]
        else:
            curr_text = curr_item['text']

        if path == '':
            path = curr_text
        else:
            path = curr_text + '/' + path

        curr_element = smd_tree.parent(curr_element)

    status_bar['text'] = path
# ------------------------------------------------------------------------------


# - Popup Menu -----------------------------------------------------------------
def smd_tree_popup_menu(event):
    smd_selection = smd_tree.identify_row(event.y)

    if smd_selection != '':
        smd_tree.selection_set(smd_selection)

    try:
        smd_tree_menu.tk_popup(event.x_root, event.y_root)
    finally:
        smd_tree_menu.grab_release() # Tk 8.0a1 only
# ------------------------------------------------------------------------------


# - GUI procedures -------------------------------------------------------------
def init_controls():
    # - Globals ----------------------------------------------------------------
    global main_form
    global smd_tree
    global status_bar
    global icons
    # --------------------------------------------------------------------------

    # - Main Form --------------------------------------------------------------
    main_form = Tkinter.Tk()
    main_form.title('SMDInfo')
    main_form.minsize(400, 280)
    main_form.geometry('400x300+' +
                       str((main_form.winfo_screenwidth()  - 400) // 2) + '+' +
                       str((main_form.winfo_screenheight() - 300) // 2))
    # --------------------------------------------------------------------------

    # - Hotkeys ----------------------------------------------------------------
    main_form.bind_all('<Control-Key-o>', cmd_open_smd_file)
    main_form.bind_all('<Control-Key-c>', cmd_copy)
    main_form.bind_all('<Delete>',        cmd_delete)
    main_form.bind_all('<F1>',            cmd_about)
    main_form.bind_all('<Alt-F4>',        cmd_quit)
    # --------------------------------------------------------------------------

    # - Icons ------------------------------------------------------------------
    icons = {}
    for icon_name, icon_base64 in ICONS_BASE64.iteritems():
        icons[icon_name] = Tkinter.PhotoImage(data=icon_base64)

    # Main form icon
    main_form.tk.call('wm', 'iconphoto', main_form._w, icons['main'])
    # --------------------------------------------------------------------------

    # - Statusbar Label --------------------------------------------------------
    status_bar_frame = ttk.Frame(main_form)
    status_bar_frame.pack(side=Tkinter.BOTTOM, fill=Tkinter.X, padx=1, pady=1)

    size_grip = ttk.Sizegrip(status_bar_frame)
    size_grip.pack(side=Tkinter.RIGHT)

    status_bar = Tkinter.Label(status_bar_frame, '', anchor=Tkinter.W)
    status_bar.pack(fill=Tkinter.X)
    # --------------------------------------------------------------------------

    # - ScrollBar for Treeview -------------------------------------------------
    smd_scrollbar = ttk.Scrollbar(main_form)
    smd_scrollbar.pack(side=Tkinter.RIGHT, fill='y')
    # --------------------------------------------------------------------------

    # - Treeview ---------------------------------------------------------------
    smd_tree = ttk.Treeview(main_form, height=0xFFFF,
                            yscrollcommand=smd_scrollbar.set)

    smd_tree.pack(fill='x')
    smd_tree.heading('#0', anchor=Tkinter.W, text='SMD Files')
    smd_scrollbar.config(command=smd_tree.yview)

    smd_tree.bind('<<TreeviewSelect>>', smd_tree_select)
    smd_tree.bind('<Button-3>', smd_tree_popup_menu)
    # --------------------------------------------------------------------------


def init_menu():
    # - Main Menu --------------------------------------------------------------
    main_menu = Tkinter.Menu(main_form)
    main_form.config(menu=main_menu)
    # --------------------------------------------------------------------------

    # - Popup Menu -------------------------------------------------------------
    global smd_tree_menu
    smd_tree_menu =  Tkinter.Menu(main_form, tearoff=0)
    # --------------------------------------------------------------------------

    # - Sub Menus --------------------------------------------------------------
    file_menu = Tkinter.Menu(main_menu, tearoff=0)
    edit_menu = Tkinter.Menu(main_menu, tearoff=0)
    help_menu = Tkinter.Menu(main_menu, tearoff=0)
    # --------------------------------------------------------------------------

    # - File Submenu -----------------------------------------------------------
    file_menu.add_command(label='Open SMD File...',
                          accelerator='Ctrl+O',
                          command=cmd_open_smd_file,
                          image=icons['open'],
                          compound=Tkinter.LEFT)
    file_menu.add_separator()
    file_menu.add_command(label='Quit',
                          accelerator='Alt+F4',
                          command=cmd_quit,
                          image=icons['quit'],
                          compound=Tkinter.LEFT)
    # --------------------------------------------------------------------------

    # - Edit Submenu -----------------------------------------------------------
    edit_menu.add_command(label='Copy',
                          accelerator='Ctrl+C',
                          command=cmd_copy,
                          image=icons['copy'],
                          compound=Tkinter.LEFT)
    edit_menu.add_separator()
    edit_menu.add_command(label='Delete...',
                          accelerator='Delete',
                          command=cmd_delete,
                          image=icons['del'],
                          compound=Tkinter.LEFT)
    # --------------------------------------------------------------------------

    # - Help Submenu -----------------------------------------------------------
    help_menu.add_command(label='About...',
                          accelerator='F1',
                          command=cmd_about,
                          image=icons['info'],
                          compound=Tkinter.LEFT)
    # --------------------------------------------------------------------------

    # - Main Menu Cascades -----------------------------------------------------
    main_menu.add_cascade(label='File', menu=file_menu)
    main_menu.add_cascade(label='Edit', menu=edit_menu)
    main_menu.add_cascade(label='Help', menu=help_menu)
    # --------------------------------------------------------------------------

    # - Popup Menu (Same As Edit Menu) -----------------------------------------
    smd_tree_menu.add_command(label='Copy',
                          accelerator='Ctrl+C',
                          command=cmd_copy,
                          image=icons['copy'],
                          compound=Tkinter.LEFT)
    smd_tree_menu.add_separator()
    smd_tree_menu.add_command(label='Delete...',
                          accelerator='Delete',
                          command=cmd_delete,
                          image=icons['del'],
                          compound=Tkinter.LEFT)
    # --------------------------------------------------------------------------


def init_tree():
    # - Is SMD Opened ----------------------------------------------------------
    global is_opened
    is_opened = False
    # --------------------------------------------------------------------------

    # - Init Tree --------------------------------------------------------------
    smd_tree_root = smd_tree.insert('',
                                    'end',
                                    text='<Empty SMD File>',
                                    open=True,
                                    image=icons['root_empty'],
                                    values=('<Empty SMD>',))
    smd_tree_bones = smd_tree.insert(smd_tree_root,
                                     'end',
                                     text='Bones (Count: 0)',
                                     image=icons['bones'],
                                     values=('Bones',))
    smd_tree_materials = smd_tree.insert(smd_tree_root,
                                         'end',
                                         text='Materials (Count: 0)',
                                         image=icons['mats'],
                                         values=('Materials',))
    smd_tree_flexes = smd_tree.insert(smd_tree_root,
                                      'end',
                                      text='Flexes (Count: 0)',
                                      image=icons['flexes'],
                                      values=('Flexes',))

    smd_tree.insert(smd_tree_bones, 'end', text='<none>', image=icons['none'])
    smd_tree.insert(smd_tree_materials, 'end', text='<none>',
                    image=icons['none'])
    smd_tree.insert(smd_tree_flexes, 'end', text='<none>', image=icons['none'])

    smd_tree.selection_set(smd_tree_root)
    smd_tree.see(smd_tree_flexes)
    # --------------------------------------------------------------------------


def load_smd(file_name):
    if os.path.isfile(file_name):
        # - Load SMD File ------------------------------------------------------
        smd_data = SMDReader(file_name)
        base_name = os.path.basename(file_name)
        # ----------------------------------------------------------------------

        global is_opened
        if not is_opened:
            smd_tree.delete(*smd_tree.get_children())
            is_opened = True

        smd_bones_count = len(smd_data.bones)
        smd_materials_count = len(smd_data.materials)
        smd_flexes_count = len(smd_data.flexes)

        # - Consider SMD Type --------------------------------------------------
        if smd_bones_count != 0:
            if smd_materials_count != 0:
                if not smd_data.has_flexes:
                    smd_name = base_name + ' (Reference)'
                    smd_icon = 'root'
                else:
                    smd_name = base_name + ' (Invalid)'
                    smd_icon = 'root_err'
            else:
                if not smd_data.has_flexes:
                    smd_name = base_name + ' (Animation)'
                else:
                    smd_name = base_name + ' (Vertex)'
                smd_icon = 'root'
            smd_bones_count += 1
        else:
            smd_name = base_name + ' (Not SMD)'
            smd_icon = 'root_err'
        # ----------------------------------------------------------------------

        # - Root Tree Elements -------------------------------------------------
        smd_tree_root = smd_tree.insert('',
                                        'end',
                                        text=smd_name,
                                        open=True,
                                        image=icons[smd_icon],
                                        values=(base_name,))

        smd_tree_bones = smd_tree.insert(smd_tree_root,
                                         'end',
                                         text='Bones (Count: ' +
                                         str(smd_bones_count) + ')',
                                         image=icons['bones'],
                                         values=('Bones',))
        smd_tree_materials = smd_tree.insert(smd_tree_root,
                                             'end',
                                             text='Materials (Count: ' +
                                             str(smd_materials_count) + ')',
                                             image=icons['mats'],
                                             values=('Materials',))
        smd_tree_flexes = smd_tree.insert(smd_tree_root,
                                          'end',
                                          text='Flexes (Count: ' +
                                          str(smd_flexes_count) + ')',
                                          image=icons['flexes'],
                                          values=('Flexes',))
        # ----------------------------------------------------------------------

        # - Add Bones ----------------------------------------------------------
        if len(smd_data.bones) > 0:
            smd_tree_bones_root = smd_tree.insert(smd_tree_bones,
                                                  'end',
                                                  text='root',
                                                  image=icons['bone'])

            bones_tree = [(bone_id, None) for bone_id, _, _ in smd_data.bones]

            for bone_id, parent_id, bone_name in smd_data.bones:
                if parent_id == -1:
                    bones_tree[bone_id] = smd_tree.insert(smd_tree_bones_root,
                                                          'end',
                                                          text=bone_name,
                                                          image=icons['bone'])
                else:
                    bones_tree[bone_id] = smd_tree.insert(bones_tree[parent_id],
                                                          'end',
                                                          text=bone_name,
                                                          image=icons['bone'])
        else:
            smd_tree.insert(smd_tree_bones,
                            'end',
                            text='<none>',
                            image=icons['none'])
        # ----------------------------------------------------------------------

        # - Add Materials ------------------------------------------------------
        if len(smd_data.materials) > 0:
            for material in sorted(smd_data.materials, key=str.lower):
                material = os.path.splitext(material)
                smd_tree.insert(smd_tree_materials,
                                'end',
                                text=material[0],
                                image=icons['mat'])
        else:
            smd_tree.insert(smd_tree_materials,
                            'end',
                            text='<none>',
                            image=icons['none'])
        # ----------------------------------------------------------------------

        # - Add Flexes ---------------------------------------------------------
        if len(smd_data.flexes) > 0:
            for flex_name, flex_dual in sorted(smd_data.flexes,
                                               key=lambda x: x[0].lower()):
                lr_suffix = ' (L + R)' if flex_dual else ''
                smd_tree.insert(smd_tree_flexes,
                                'end',
                                text=flex_name + lr_suffix,
                                image=icons['flex'],
                                values=(flex_name,))
        else:
            smd_tree.insert(smd_tree_flexes,
                            'end',
                            text='<none>',
                            image=icons['none'])
        # ----------------------------------------------------------------------

        # - Make Current File Visible ------------------------------------------
        smd_tree.selection_set(smd_tree_root)
        smd_tree.see(smd_tree_flexes)
        # ----------------------------------------------------------------------
# ------------------------------------------------------------------------------


# - Main -----------------------------------------------------------------------
def main():
    # - Init GUI ---------------------------------------------------------------
    init_controls()
    init_menu()
    init_tree()
    # --------------------------------------------------------------------------

    # - Load Files From Command Line -------------------------------------------
    is_first = True
    for arg in sys.argv:
        if not is_first:
            load_smd(arg)
        is_first = False
    # --------------------------------------------------------------------------

    # - Main loop for GUI ------------------------------------------------------
    main_form.mainloop()
    # --------------------------------------------------------------------------


if __name__ == '__main__':
    main()
# ------------------------------------------------------------------------------