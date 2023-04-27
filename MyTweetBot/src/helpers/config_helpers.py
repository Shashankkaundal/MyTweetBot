import os
def get_base_url():
    env=os.environ.get('ENV','test')
    if env.lower()=='test':
        return 'https://twitter.com/login'
    elif env.lower()=='prod':
        raise Exception("PROD env is not available")
    else:
        raise Exception("env is not known")

def get_amazon_url():
    env = os.environ.get('ENV', 'test')
    if env.lower() == 'test':
        return 'https://www.amazon.in/'
    elif env.lower() == 'prod':
        raise Exception("PROD env is not available")
    else:
        raise Exception("env is not known")

