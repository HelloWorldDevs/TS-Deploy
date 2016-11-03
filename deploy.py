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
	1)

#Check for the existence of the site on the server,
# if it exists do a git pull and exit
websiteList = server.list_websites(session_id)
websiteFound = False
for website in websiteList:
	if siteConfig.websiteName == website['name']:
		print "Your site " + siteConfig.websiteName + " is already set up!"
		print website
		pullCmd = "cd webapps/"+ siteConfig.websiteName + "_app && git pull -q origin master"
		print "Pulling most recent changes"
		server.system(session_id, pullCmd)
		sys.exit()


#Setting up the server and initial deployment
#=============================
print "Starting server configuration..."

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
domainName = siteConfig.websiteName + ".hwdevs.com"
for domain in domainList:
	if domainName == domain['domain']:
		domainFound = True
if domainFound:
	print "Warning: The domain " + domainName + " has already been created on the server."
else:
	print "Starting domain configuration..."
	server.create_domain(
		session_id,
		domainName)

		
#3. Create website
#Build the site
print "Starting website configuration..."
if websiteFound:
	print "Website already configured"
else:
	server.create_website(session_id,
		siteConfig.websiteName,
		siteConfig.ipAddress,
		False,
		[domainName],
		[appName, '/'])
	initGit = "cd /home/danlinn/webapps/"+appName+" && rm index.html && git clone -q " + siteConfig.repoUrl + " ."
	server.system(session_id, initGit)

#Print results of new website setup
print "Your website has been set up and configured."
for website in websiteList:
	if siteConfig.websiteName == website['name']:
		print website

#=============================
#End settting up the server