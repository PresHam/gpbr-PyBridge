import datetime as dt


def update_sf_opportunity(opportunity, client):
    date = dt.datetime.now().strftime('%Y-%m-%d')
    result_update = client.sobjects. \
        Opportunity.update(opportunity, {'CloseDate': date, 'mundi_charge__c': True})
    return f'Resposta update OPP: {result_update}'

