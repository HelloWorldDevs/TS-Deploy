#Dependencies
import sys
import xmlrpclib 		#talk to the server using xml
import os.path			#check file directories
import scripts.webfaction as webfaction  #HWD custom webfaction module

#Import siteConfig.py
if os.path.isfile("siteConfig.py"):
	import siteConfig
else:
	sys.exit("Your siteConfig.py file was not found. See example.siteconfig.py for more information on setting up siteConfig.py.")


#Connect to webFaction API, authenticate
server = xmlrpclib.ServerProxy('https://api.webfaction.com/')
session_id = webfaction.login(server, siteConfig)

#Check for the existence of the site on the server, offer to pull if it does
if webfaction.checkSite(server, session_id, siteConfig):
	print "Your site already exists. Here is the info for it..."
	prompt = raw_input("Would you like to pull the latest version of master from GitHub? [Y/n]")
	if prompt == "y" or prompt == "Y":
		print "Pulling latest version..."
		webfaction.gitPull(server, session_id, siteConfig)
		print "Pull successful"
	sys.exit()

#Setting up the server and initial deployment
#=============================
print "Starting server configuration..."


#1. Create Webapp
if webfaction.checkApp(server, session_id, siteConfig):
	print "Warning: The webapp " + siteConfig.appName + " has already been created on the server."
else:
	print "Starting webApp configuration..."
	webfaction.createApp(server, session_id, siteConfig)
	print "Finished webApp configuration"


#2. Create Domain
if webfaction.checkDomain(server, session_id, siteConfig):
	print "Warning: The domain " + siteConfig.domainName + " has already been created on the server."
else:
	print "Starting domain configuration..."
	webfaction.createDomain(server, session_id, siteConfig)
	print "Finished domain configuration"


#3. Create website
print "Starting website configuration..."
webfaction.createDomain(server, session_id, siteConfig)
webfaction.gitClone(server, session_id, siteConfig)
print "Finished website configuration"


#4. Print results of new website setup
print "Your website has been set up and configured."
print webfaction.checkSite(server, session_id, siteConfig)
sys.exit()

#=============================
#End settting up the server
