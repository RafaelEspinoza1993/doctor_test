viruela = {
    "high" : {
        "ct": "5-15",
        "amp":1.2,
        "cq": 1.9
    },
    "medium" : {
        "ct": "12-22",
        "amp":1.2,
        "cq": 1.9
    },
    "low" : {
        "ct": "22-31",
        "amp":1.2,
        "cq": 1.9
    },
    "no_range" : {
        "ct": "n/a",
        "amp":"n/a",
        "cq": "n/a"
    },
}
sarampeon = {
    "high" : {
        "ct": "n/a",
        "amp":1.2,
        "cq": 1.9
    },
    "medium" : {
        "ct": "n/a",
        "amp":1.2,
        "cq": 1.9
    },
    "low" : {
        "ct": "n/a",
        "amp":1.2,
        "cq": 1.9
    },
    "no_range" : {
        "ct": "8-30",
        "amp":1.2,
        "cq": 1.9
    },
}
covid = {
    "high" : {
        "ct": "6-10",
        "amp":1.2,
        "cq": 1.9
    },
    "medium" : {
        "ct": "10-21",
        "amp":1.2,
        "cq": 1.9
    },
    "low" : {
        "ct": "21-29",
        "amp":1.2,
        "cq": 1.9
    },
    "no_range" : {
        "ct": "n/a",
        "amp":"n/a",
        "cq": "n/a"
    },
}
ebola = {
    "high" : {
        "ct": "8-11",
        "amp":1.2,
        "cq": 1.9
    },
    "medium" : {
        "ct": "11-17",
        "amp":1.2,
        "cq": 1.9
    },
    "low" : {
        "ct":"n/a",
        "amp":"n/a",
        "cq":"n/a",
    },
    "no_range" : {
        "ct": "n/a",
        "amp":"n/a",
        "cq": "n/a"
    },
}

def TransformSTRtoFLOAT(data):
    return {
        'ct' : 0 if data['ct'] == 'Undetermined' else float(data['ct']),
        'amp' : 0 if data['amp'] == 'Undetermined' else float(data['amp']),
        'cq' : 0 if data['cq'] == 'Undetermined' else float(data['cq'])
    }

def validacionViruela(data, text):
    viruelaHighCTsplit = viruela['high']['ct'].split('-')
    viruelaMediumCTsplit = viruela['medium']['ct'].split('-')
    viruelaLowCTsplit = viruela['low']['ct'].split('-')
    result = {
        'well': '',
        'target id': '',
        'target name': '',
        'ct': '',
        'amp': '',
        'cq': '',
        'result': '',
        'comment': ''
    }


    statusEnfermedad = {
        'viruela': {
            'status':0,
            'ct':0,
            'amp':0,
            'cq':0
        },
        'sarampeon': {
            'status':0,
            'ct':0,
            'amp':0,
            'cq':0
        },
        'covid': {
            'status':0,
            'ct':0,
            'amp':0,
            'cq':0
        },
        'ebola': {
            'status':0,
            'ct':0,
            'amp':0,
            'cq':0
        }
    }
    if data['ct'] > float(viruelaHighCTsplit[0]) or data['ct'] > float(viruelaHighCTsplit[1]) or data['amp'] > viruela['high']['amp'] or data['cq'] > viruela['high']['cq']:
        result['well'] = text['well']
        result['target id'] = text['target id']
        result['target name'] = text['target name']
        result['ct'] = data['ct']
        result['amp'] = data['amp']
        result['cq'] = data['cq']
        result['comment'] = 'high'
    elif data['ct'] > float(viruelaMediumCTsplit[0]) or data['ct'] > float(viruelaMediumCTsplit[1]) or data['amp'] > viruela['medium']['amp'] or data['cq'] > viruela['medium']['cq']:
        result['well'] = text['well']
        result['target id'] = text['target id']
        result['target name'] = text['target name']
        result['ct'] = data['ct']
        result['amp'] = data['amp']
        result['cq'] = data['cq']
        result['comment'] = 'medium'
    elif data['ct'] > float(viruelaLowCTsplit[0]) or data['ct'] > float(viruelaLowCTsplit[1]) or data['amp'] > viruela['low']['amp'] or data['cq'] > viruela['low']['cq']:
        result['well'] = text['well']
        result['target id'] = text['target id']
        result['target name'] = text['target name']
        result['ct'] = data['ct']
        result['amp'] = data['amp']
        result['cq'] = data['cq']
        result['comment'] = 'low'
    else:
        result['well'] = text['well']
        result['target id'] = text['target id']
        result['target name'] = text['target name']
        result['ct'] = data['ct']
        result['amp'] = data['amp']
        result['cq'] = data['cq']
        result['comment'] = 'no range'
    return {
        'result': result,
        'status': statusEnfermedad
    }

def validacionSarampeon(data, text):
    sarampeonNoRangeCTsplit = sarampeon['no_range']['ct'].split('-')
    result = {
        'well': '',
        'target id': '',
        'target name': '',
        'ct': '',
        'amp': '',
        'cq': '',
        'result': '',
        'comment': ''
    }


    statusEnfermedad = {
        'viruela': {
            'status':0,
            'ct':0,
            'amp':0,
            'cq':0
        },
        'sarampeon': {
            'status':0,
            'ct':0,
            'amp':0,
            'cq':0
        },
        'covid': {
            'status':0,
            'ct':0,
            'amp':0,
            'cq':0
        },
        'ebola': {
            'status':0,
            'ct':0,
            'amp':0,
            'cq':0
        }
    }
    if data['amp'] > sarampeon['high']['amp'] or data['cq'] > sarampeon['high']['cq']:
        result['well'] = text['well']
        result['target id'] = text['target id']
        result['target name'] = text['target name']
        result['ct'] = data['ct']
        result['amp'] = data['amp']
        result['cq'] = data['cq']
        result['comment'] = 'high'
    elif data['amp'] > sarampeon['medium']['amp'] or data['cq'] > sarampeon['medium']['cq']:
        result['well'] = text['well']
        result['target id'] = text['target id']
        result['target name'] = text['target name']
        result['ct'] = data['ct']
        result['amp'] = data['amp']
        result['cq'] = data['cq']
        result['comment'] = 'medium'
    elif data['amp'] > sarampeon['low']['amp'] or data['cq'] > sarampeon['low']['cq']:
        result['well'] = text['well']
        result['target id'] = text['target id']
        result['target name'] = text['target name']
        result['ct'] = data['ct']
        result['amp'] = data['amp']
        result['cq'] = data['cq']
        result['comment'] = 'low'
    elif data['ct'] > float(sarampeonNoRangeCTsplit[0]) or data['ct'] > float(sarampeonNoRangeCTsplit[1]) or data['amp'] > sarampeon['no_range']['amp'] or data['cq'] > sarampeon['no_range']['cq']:
        result['well'] = text['well']
        result['target id'] = text['target id']
        result['target name'] = text['target name']
        result['ct'] = data['ct']
        result['amp'] = data['amp']
        result['cq'] = data['cq']
        result['comment'] = 'no range'
    return {
        'result': result,
        'status': statusEnfermedad
    }

def validacionCovid(data, text):
    covidHighCTsplit = covid['high']['ct'].split('-')
    covidMediumCTsplit = covid['medium']['ct'].split('-')
    covidLowCTsplit = covid['low']['ct'].split('-')
    result = {
        'well': '',
        'target id': '',
        'target name': '',
        'ct': '',
        'amp': '',
        'cq': '',
        'result': '',
        'comment': ''
    }


    statusEnfermedad = {
        'viruela': {
            'status':0,
            'ct':0,
            'amp':0,
            'cq':0
        },
        'sarampeon': {
            'status':0,
            'ct':0,
            'amp':0,
            'cq':0
        },
        'covid': {
            'status':0,
            'ct':0,
            'amp':0,
            'cq':0
        },
        'ebola': {
            'status':0,
            'ct':0,
            'amp':0,
            'cq':0
        }
    }
    if data['ct'] > float(covidHighCTsplit[0]) or data['ct'] > float(covidHighCTsplit[1]) or data['amp'] > covid['high']['amp'] or data['cq'] > covid['high']['cq']:
        result['well'] = text['well']
        result['target id'] = text['target id']
        result['target name'] = text['target name']
        result['ct'] = data['ct']
        result['amp'] = data['amp']
        result['cq'] = data['cq']
        result['comment'] = 'high'
    elif data['ct'] > float(covidMediumCTsplit[0]) or data['ct'] > float(covidMediumCTsplit[1]) or data['amp'] > covid['medium']['amp'] or data['cq'] > covid['medium']['cq']:
        result['well'] = text['well']
        result['target id'] = text['target id']
        result['target name'] = text['target name']
        result['ct'] = data['ct']
        result['amp'] = data['amp']
        result['cq'] = data['cq']
        result['comment'] = 'medium'
    elif data['ct'] > float(covidLowCTsplit[0]) or data['ct'] > float(covidLowCTsplit[1]) or data['amp'] > covid['low']['amp'] or data['cq'] > covid['low']['cq']:
        result['well'] = text['well']
        result['target id'] = text['target id']
        result['target name'] = text['target name']
        result['ct'] = data['ct']
        result['amp'] = data['amp']
        result['cq'] = data['cq']
        result['comment'] = 'low'
    else:
        result['well'] = text['well']
        result['target id'] = text['target id']
        result['target name'] = text['target name']
        result['ct'] = data['ct']
        result['amp'] = data['amp']
        result['cq'] = data['cq']
        result['comment'] = 'no range'
    return {
        'result': result,
        'status': statusEnfermedad
    }

def validacionEbola(data, text):
    ebolaHighCTsplit = ebola['high']['ct'].split('-')
    ebolaMediumCTsplit = ebola['medium']['ct'].split('-')
    result = {
        'well': '',
        'target id': '',
        'target name': '',
        'ct': '',
        'amp': '',
        'cq': '',
        'result': '',
        'comment': ''
    }


    statusEnfermedad = {
        'viruela': {
            'status':0,
            'ct':0,
            'amp':0,
            'cq':0
        },
        'sarampeon': {
            'status':0,
            'ct':0,
            'amp':0,
            'cq':0
        },
        'covid': {
            'status':0,
            'ct':0,
            'amp':0,
            'cq':0
        },
        'ebola': {
            'status':0,
            'ct':0,
            'amp':0,
            'cq':0
        }
    }
    if data['ct'] > float(ebolaHighCTsplit[0]) or data['ct'] > float(ebolaHighCTsplit[1]) or data['amp'] > covid['high']['amp'] or data['cq'] > covid['high']['cq']:
        result['well'] = text['well']
        result['target id'] = text['target id']
        result['target name'] = text['target name']
        result['ct'] = data['ct']
        result['amp'] = data['amp']
        result['cq'] = data['cq']
        result['comment'] = 'high'
    elif data['ct'] > float(ebolaMediumCTsplit[0]) or data['ct'] > float(ebolaMediumCTsplit[1]) or data['amp'] > covid['medium']['amp'] or data['cq'] > covid['medium']['cq']:
        result['well'] = text['well']
        result['target id'] = text['target id']
        result['target name'] = text['target name']
        result['ct'] = data['ct']
        result['amp'] = data['amp']
        result['cq'] = data['cq']
        result['comment'] = 'medium'
    else:
        result['well'] = text['well']
        result['target id'] = text['target id']
        result['target name'] = text['target name']
        result['ct'] = data['ct']
        result['amp'] = data['amp']
        result['cq'] = data['cq']
        result['comment'] = 'no range'
    return {
        'result': result,
        'status': statusEnfermedad
    }

def validacion(data, id):
    test = TransformSTRtoFLOAT(data)
    if 'org1':
        result= validacionViruela(test, data)
    if 'org2':
        result = validacionSarampeon(test, data)
    if 'org3':
        result = validacionCovid(test, data)
    if 'org4':
        result = validacionEbola(test, data)

    return result