import boto3
ses = boto3.client("ses")

def handler(event, context):
    try:
        data = ses.send_email(
            Source="testsigma18+April20th2022GSK@gmail.com",
            Destination={
                'ToAddresses': ["kumudika@adroitlogic.com"]
            },
            Message={
                'Subject': {
                    'Data': "tt"
                },
                'Body': {
                    'Html': {
                        'Data': ""
                    }
                }
            }
        )
        print(data)
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
