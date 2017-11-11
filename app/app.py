from os import system
import platform as spec

platform = spec.platform()

if 'Windows' in platform:
    system('..\\venvflask\\Scripts\\activate')
    system('dev_appserver.py app.yaml --admin_port=9000 --host=0.0.0.0 --port=8081')
    system('..\\venvflask\\Scripts\\deactivate')