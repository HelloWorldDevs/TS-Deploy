#Dependencies
import sys
import xmlrpclib 		#talk to the server using xml
import os.path			#check file directories



#Import siteConfig.py
if os.path.isfile("siteConfig.py"):
	import siteConfig
else:
	sys.exit("Your siteConfig.py file was not found. See example.siteconfig.py for more information on setting up siteConfig.py.")


#Connect to webFaction API and Authenticate
server = xmlrpclib.ServerProxy('https://api.webfaction.com/')
session_id, account = server.login(
	siteConfig.userName,
	siteConfig.userPass,
	siteConfig.machineName,
	2)

#Check for the existence of the site on the server
websiteList = server.list_websites(session_id)
websiteFound = False
for website in websiteList:
	if siteConfig.websiteName == website['name']:
		websiteFound = True
if websiteFound:
	print "Your site " + siteConfig.websiteName + " is already set up!"
	sys.exit()
else:
	print "Starting server configuration..."


#Setting up the initial deploy
#=============================

#1. Create Webapp
#Check for the existence of the site on the server
appList = server.list_apps(session_id)
appFound = False
appName = siteConfig.websiteName + "_app"
for app in appList:
	if appName == app['name']:
		appFound = True
if appFound:
	print "Warning: The webapp " + appName + " has already been created on the server."
else:
	print "Starting webApp configuration..."
	server.create_app(
		session_id,
		appName,
		'static_php56',
		False,
		'',
		False)

#2. Create Domain
#Check for the existence of the domain on the server and create it if needed
domainList = server.list_domains(session_id)
domainFound = False
domainName = siteConfig.websiteName + ".webfactional.com"
for domain in domainList:
	if domainName == domain['domain']:
		domainFound = True
if domainFound:
	print "Warning: The domain " + domainName + " has already been created on the server."
else:
	print "Starting domain configuration..."
#	server.create_app(
#		session_id,
#		appName,
#		'static_php56',
#		False,
#		'',
#		False)

#cmd = "rm -f index.html && git clone https://github.com/HelloWorldDevs/lacey.git ."
#test existence of webapp
#testAppPresence = "if [ -d ~/home/danlinn/webapps/lacey ]; then echo ; fi"
#
#server.system(session_id, testAppPresence)

#
#appList = server.list_apps(session_id)
#appExists = False
#
#for app in appList:
#	if siteConfig.webappName + "_app" == app['name']:
#		appExists = True
#
#if appExists:
#	print "WebApp " + siteConfig.webappName + " already exists on the server"
#else:
#	print "WebApp does not exist yet, building app..."
##	Creates a new app
#	server.create_app(session_id, siteConfig.webappName + "_app", 'static_php56', False, '', False)
##	Removes the dummy index.html from app creation
#	server.system(session_id, "cd /home/danlinn/webapps/" + siteConfig.webappName + "_app" + " && rm -f index.html")
#
#
#siteList = server.list_websites(session_id)
#siteExists = False
#for site in siteList:
#	if siteConfig.siteName == site['name']:
#		siteExists = True
#
#if siteExists:
#	print "Website " + siteConfig.siteName + " already exists on the server"
#else:
#	print "Website does not yet exist, building website..."
#	print session_id
##	Create a new website
#	appAddress = "/home/danlinn/webapps/" + siteConfig.webappName + "_app/"
#	print appAddress
#	server.create_website(
#		session_id,
#		siteConfig.siteName,
#		"198.58.114.22",
#		False,
#		[siteConfig.siteName],
#		"",
#		[[ siteConfig.webappName  + "_app", "http://" + siteConfig.siteName + ".hwdevs.site" ]]
#		)
