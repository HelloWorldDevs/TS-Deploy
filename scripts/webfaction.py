# A number of functions to communicate with the Webfaction API for Hello World Devs projects. This module was built to be used on the Tyson Steele projects by Joe Karasek.

def login(server, siteConfig, version=1):
    session_id, account = server.login(
    	siteConfig.userName,
    	siteConfig.userPass,
    	siteConfig.machineName,
    	1)
    return session_id

def checkApp(server, session_id, siteConfig):
    appList = server.list_apps(session_id)
    for app in appList:
    	if siteConfig.appName == app['name']:
            return True
    return False

def createApp(server, session_id, siteConfig, appType='static_php56'):
    server.create_app(
		session_id,
		siteConfig.appName,
		appType,
		False,
		'',
		False)

def checkSite(server, session_id, siteConfig):
    websiteList = server.list_websites(session_id)
    for website in websiteList:
    	if siteConfig.websiteName == website['name']:
    		return website
    return False

def createSite(server, session_id, siteConfig):
    server.create_website(session_id,
		siteConfig.websiteName,
		siteConfig.ipAddress,
		False,
		[siteConfig.domainName],
		[siteConfig.appName, '/'])

def checkDomain(server, session_id, siteConfig):
    domainList = server.list_domains(session_id)
    for domain in domainList:
    	if domain['domain'] == siteConfig.domainName:
    		return True
    return False

def createDomain(server, session_id, siteConfig):
    server.create_domain(
		session_id,
		siteConfig.domainName)

def gitClone(server, session_id, siteConfig):
    initGit = "cd /home/danlinn/webapps/"+siteConfig.appName+" && rm index.html && git clone -q " + siteConfig.repoUrl + " ."
    server.system(session_id, initGit)

def gitPull(server, session_id, siteConfig):
    gitPull = "cd /home/danlinn/webapps/"+siteConfig.appName+" && git pull -q origin master"
    server.system(session_id, gitPull)

# def addHtaccess(server, session_id, siteConfig):
