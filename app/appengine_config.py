from google.appengine.ext import vendor
import os, sys

vendor.add('lib')

if os.environ.get('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    sys.path.insert(0, 'lib.zip')
    
else:
    if os.name == 'nt':
        os.name = None
        sys.platform = ''