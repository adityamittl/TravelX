def extract_bill(bill_image_path):
    from azure.ai.formrecognizer import FormRecognizerClient, FormTrainingClient
    from azure.core.credentials import AzureKeyCredential
    import json

    config = { "endpoint": "https://for-hackathon.cognitiveservices.azure.com/","key": "625cca750bb3484ca4dd443655eecd0a"}
    client = FormRecognizerClient(config["endpoint"], AzureKeyCredential(config["key"]))
    
    f =  open(bill_image_path, "rb")
    receipt_recognizer = client.begin_recognize_receipts(f)
    receipt_recognizer = receipt_recognizer.result()
    receipt = receipt_recognizer[0].to_dict()
    try:
        Date = str(receipt['fields']['TransactionDate']['value'])
    except:
        Date = "NA"
    try:
        Time = str(receipt['fields']['TransactionTime']['value'])
    except:
        Time = "NA"
    try:
        MerchantName = str(receipt['fields']['MerchantName']['value'])
    except:
        MerchantName = "NA"
    try:
        Total = float(receipt['fields']['Total']['value'])
    except:
        Total = 0.0
    result = [{
        'date' : Date,
        'time' : Time,
        'merchant' : MerchantName,
        'total' : Total
    }]
    return result
