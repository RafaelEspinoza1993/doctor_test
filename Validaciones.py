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

def TransformSTRtoFLOAT(data):
    return {
        'ct' : 'n/a' if data['ct'] == 'Undetermined' else float(data['ct']),
        'amp' : 'n/a' if data['amp'] == 'Undetermined' else float(data['amp']),
        'cq' : 'n/a' if data['cq'] == 'Undetermined' else float(data['cq'])
    }

def validacionViruela(data):
    viruelaHighCTsplit = viruela['high']['ct'].split('-')
    viruelaMediumCTsplit = viruela['medium']['ct'].split('-')
    viruelaLowCTsplit = viruela['low']['ct'].split('-')

    if data['amp'] > viruela['high']['amp']:
        result['amp'] = data['amp']
        result['comment'] = 'high'
    elif data['amp'] > viruela['medium']['amp']:
        result['amp'] = data['amp']
        result['comment'] = 'medium'
    elif data['amp'] > viruela['low']['amp']:
        result['amp'] = data['amp']
        result['comment'] = 'low'
    else:
        result['amp'] = data['amp']
        result['comment'] = 'no range'
    return

def validacionSarampeon(data):
    sarampeonHighCTsplit = sarampeon['high']['ct'].split('-')
    sarampeonMediumCTsplit = sarampeon['medium']['ct'].split('-')
    sarampeonLowCTsplit = sarampeon['low']['ct'].split('-')

    if data['ct'] > sarampeonHighCTsplit[0] or data['ct'] > sarampeonHighCTsplit[1] or data['amp'] > sarampeon['high']['amp']:
        result['ct'] = data['ct']
        result['amp'] = data['amp']
        result['comment'] = 'high'
    elif data['amp'] > sarampeon['medium']['amp']:
        result['amp'] = data['amp']
        result['comment'] = 'medium'
    elif data['amp'] > sarampeon['low']['amp']:
        result['amp'] = data['amp']
        result['comment'] = 'low'
    else:
        result['amp'] = data['amp']
        result['comment'] = 'no range'
    return

def validacionViruela(data):
    viruelaNoRangeCTsplit = viruela['no_range']['ct'].split('-')

    if data['amp'] > viruela['high']['amp']:
        result['amp'] = data['amp']
        result['comment'] = 'high'
    elif data['amp'] > viruela['medium']['amp']:
        result['amp'] = data['amp']
        result['comment'] = 'medium'
    elif data['amp'] > viruela['low']['amp']:
        result['amp'] = data['amp']
        result['comment'] = 'low'
    else:
        result['amp'] = data['amp']
        result['comment'] = 'no range'
    return

def validacion(data, id):
    test = TransformSTRtoFLOAT(data)
    if 'org1':
        validacionViruela(test)
    #if 'org2':
        #validacionSarampeon(test)
    #if 'org3':
        #validacionViruela(test)
    #if 'org4':
        #validacionViruela(test)

    return result 