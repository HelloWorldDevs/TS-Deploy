#Dependencies
import xmlrpclib 		#talk to the server using xml
import os.path			#check file directories


#Import siteConfig.py
if os.path.isfile("siteConfig.py"):
	import siteConfig
else:
	sys.exit("Your siteConfig.py file was not found. See example.siteconfig.py for more information.")

#Connect to webFaction API and Authenticate	
server = xmlrpclib.ServerProxy('https://api.webfaction.com/')
session_id, account = server.login(
	siteConfig.userName, 
	siteConfig.userPass, 
	siteConfig.machineName, 
	2)

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