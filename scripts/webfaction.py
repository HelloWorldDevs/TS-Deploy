# A number of functions to communicate with the Webfaction API for Hello World Devs projects. This module was built to be used on the Tyson Steele projects by Joe Karasek.

def checkApp(server, session_id, appName):
    appList = server.list_apps(session_id)
    for app in appList:
    	if appName == app['name']:
            return True
    return False

def createApp(server, session_id, appName, appType='static_php56'):
    server.create_app(
		session_id,
		appName,
		appType,
		False,
		'',
		False)
