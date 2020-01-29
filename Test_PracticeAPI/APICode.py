import requests
from SampleProject.loggingpackage.custom_logger_new import cust_log
import pytest
import unittest
import json
#*******************************************************************************************
'''
    getMethod will fetch the data for all the users
'''
#*******************************************************************************************
class API_Methods():
    __tLog_Obj = cust_log()

#********************************************************************************************
    '''
        Get token method will retrive the generfted token which will be used for an authorization
    '''
#********************************************************************************************
    def getToken(self):
        data = {'username': 'root', 'password': 'default'}
        r = requests.post('https://reqres.in/api/users', data=json.dumps(data), verify=False)
        token = json.loads(r.text)['session']
        return token

    def setHeader(self):
        token = self.getToken()
        headers = {'Authorization': 'Token ' + token}
        return headers

    def getMethod(self, url):
        __ResPass = '[200]'
        __ResFail = ['[406]','[500]','[404]','[401]']
        __ResCreate = '[201]'
        #token = self.getToken()

        resStatus = requests.get(url, headers=self.setHeader())
        #assert resStatus.status_code == 200
        print(resStatus)
        respText = resStatus.json()
        resultFile = open('Getjson_result.txt','w')
        resultFile.write(str(respText))
        if __ResPass in str(resStatus):
            print('Response code is "{}": Get method is successfully executed'.format(__ResPass))
            print("json Response is: '{}'".format(respText))
            self.__tLog_Obj.info('Response code is "{}": Get method is successfully executed.'.format(__ResPass))

        else:
            for x in __ResFail:
                if x in str(resStatus):
                    if x == '[406]':
                        print('Response code is "{}": Get method is failed.'.format(x))
                        self.__tLog_Obj.error('Response code is "{}": Get method is failed.'.format(x))
                        return x
                    if x == '[500]':
                        print('Response code is "{}": Get method is failed.'.format(x))
                        self.__tLog_Obj.error('Response code is "{}": Get method is failed.'.format(x))
                        return x
                    if x == '[404]':
                        print('Response code is "{}": Get method is failed.'.format(x))
                        self.__tLog_Obj.error('Response code is "{}": Get method is failed.'.format(x))
                        return x
                    if x == '[401]':
                        print('Response code is "{}": Get method is failed.'.format(x))
                        self.__tLog_Obj.error('Response code is "{}": <Authorization error>.'.format(x))
                        return x

#*********************************************************************
    '''
    getSingleUser method will return an information about only one user
    '''
#**********************************************************************
    def getSingleUser(self, url):
        __resPass = '[200]'
        __ResFail = ['[406]', '[500]', '[404]', '[401]']
        resStatus = requests.get(url)
        print(resStatus)
        respText = resStatus.json()
        if __resPass in str(resStatus):
            print('Response code is {}, get method is successfully executed for user with id "{}"'.format(__resPass,id))
            print('JSON resonse is: {}'.format(respText))
            self.__tLog_Obj.info('Response code is "{}": Get method is successfully executed.'.format(__resPass))
        else:
            for x in __ResFail:
                if x in resStatus:
                    print('Response code is {}, get method is failed'.format(x))

#*********************************************************************************************
    '''
    Put method will update the existing data.
    '''
#*********************************************************************************************
    def putMethod(self, url, data):
        __ResPass = '[200]'
        __ResFail = ['[406]','[500]','[404]']
        __ResCreate = '[201]'
        resStatus = requests.put(url, data)
        print(resStatus)
        respText = requests.Response.json(resStatus)
        putResult = open('putRequest_result.txt','w')
        putResult.write(str(respText))
        if __ResPass in str(resStatus):
            print('Response code is "{}": Put method is successfully passed'.format(__ResPass))
            print("json Response is: '{}'".format(respText))
            self.__tLog_Obj.info('Response code is "{}": Put method is successfully executed.'.format(__ResPass))
        else:
            for x in __ResFail:
                if x in str(resStatus):
                    print('Response code is "{}": Get method is failed'.format(x))
                    self.__tLog_Obj.error('Response code is "{}": Get method is failed'.format(x))
        return respText

#**********************************************************************************************
    '''
    This post method is for registration of user
    '''
#**********************************************************************************************
    '''def postMethod(self, url, data):
        __ResPass = '[200]'
        __ResFail = ['[406]', '[500]', '[404]','[400]']
        __ResCreate = '[201]'
        headers = {'Content-Type': 'application/json'}
        resStatus = requests.post(url, data = json.dumps(data,indent=4), headers=headers)
        assert resStatus.status_code == 201
        print(resStatus)
        respText = requests.Response.json(resStatus)
        with open('postMethod_result.txt','w') as postResult:
            postResult.write(str(respText))
        if __ResCreate in str(resStatus):
            print('Response code is "{}": Post method is successfully passed'.format(__ResCreate))
            print("json Response is: '{}'".format(respText))
            self.__tLog_Obj.info('Response code is "{}": Post method is successfully executed.'.format(__ResCreate))

        else:
            for x in __ResFail:
                if x in str(resStatus):
                    print('Response code is "{}": Post method is failed'.format(x))
                    self.__tLog_Obj.error('Response code is "{}": Post method is failed'.format(x))
        return respText'''
#*********************************************************************************************
    def postMethod(self, url, kwargs):
        __ResPass = '[200]'
        __ResFail = ['[406]', '[500]', '[404]', '[400]']
        __ResCreate = '[201]'
        headers = {'Content-Type': 'application/json'}
        for arg in kwargs:
            resStatus = requests.post(url, data=arg, headers=headers)
            assert resStatus.status_code == 201
            print(resStatus)
            respText = requests.Response.json(resStatus)
            token = respText['id']
            if token is not None:
                with open('postMethod_result.txt', 'a+') as postResult:
                    postResult.write("Below sets of Data has been successfully posted:-->> "+'\n' + str(respText) + '\n')
            else:
                print("Post request is not successful")
            if __ResCreate in str(resStatus):
                print('Response code is "{}": Post method is successfully passed'.format(__ResCreate))
                print("json Response is: '{}'".format(respText))
                self.__tLog_Obj.info('Response code is "{}": Post method is successfully executed.'.format(__ResCreate))

            else:
                for x in __ResFail:
                    if x in str(resStatus):
                        print('Response code is "{}": Post method is failed'.format(x))
                        self.__tLog_Obj.error('Response code is "{}": Post method is failed'.format(x))
                return respText
#*******************************************************************************************

#**********************************************************************************************
    '''
    Delete method will delete the required data based on the value passed
    '''
#**********************************************************************************************
    def deleteMethod(self, url):
        __ResPass = ['[200]', '[204]']
        __ResFail = ['[406]', '[500]', '[404]']
        __ResCreate = '[201]'
        resStatus = requests.delete(url)
        print(resStatus)

        for x in __ResPass:
            if x in str(resStatus):
                print('Response code is "{}": Delete method is successfully executed.'.format(x))
                self.__tLog_Obj.info('Response code is "{}": Delete method is successfully passed'.format(x))

        else:
            for x in __ResFail:
                if x in str(resStatus):
                    print('Response code is "{}": Delete method is failed'.format(x))
                    self.__tLog_Obj.error('Response code is "{}": Get method is failed'.format(x))
        return resStatus




