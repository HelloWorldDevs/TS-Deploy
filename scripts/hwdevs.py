#!/usr/bin/env python

# A number of functions to communicate with the Webfaction API for Hello World Devs projects. This module was built to be used on the Tyson Steele projects by Joe Karasek.

class Webfaction(object):
    def __init__(self, server, siteConfig):
        self.siteConfig = siteConfig
        self.server = server
        self.session_id, self.account = server.login(
        	siteConfig.userName,
        	siteConfig.userPass,
        	siteConfig.machineName,
        	1)

    def checkApp(self):
        appList = self.server.list_apps(self.session_id)
        for app in appList:
            if self.siteConfig.appName == app['name']:
                return True
        return False

    def createApp(self, appType='static_php56'):
        self.server.create_app(
    		self.session_id,
    		self.siteConfig.appName,
    		appType,
    		False,
    		'',
    		False)

    def checkSite(self):
        websiteList = self.server.list_websites(self.session_id)
        for website in websiteList:
        	if self.siteConfig.websiteName == website['name']:
        		return website
        return False

    def createSite(self):
        self.server.create_website(self.session_id,
    		self.siteConfig.websiteName,
    		self.siteConfig.ipAddress,
    		False,
    		[self.siteConfig.domainName],
    		[self.siteConfig.appName, '/'])

    def checkDomain(self):
        domainList = self.server.list_domains(self.session_id)
        for domain in domainList:
        	if domain['domain'] == self.siteConfig.domainName:
        		return True
        return False

    def createDomain(self):
        self.server.create_domain(
    		self.session_id,
    		self.siteConfig.domainName)

    def gitClone(self):
        initGit = "cd /home/danlinn/webapps/"+self.siteConfig.appName+" && if [ -e index.html ]; then rm index.html; fi && git clone -q " + self.siteConfig.repoUrl + " . 2>&1 | grep -v 'warning: You appear to have cloned an empty repository.'"
        self.server.system(self.session_id, initGit)

    def gitPull(self):
        gitPull = "cd /home/danlinn/webapps/"+self.siteConfig.appName+" && git pull -q origin master"
        self.server.system(self.session_id, gitPull)

    # def addHtaccess(server, session_id, siteConfig):
