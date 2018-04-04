# -*- coding: utf-8 -*-
import json
import requests
import vk_api
import getpass
import datetime
import time



def main():
    url = 'https://api.github.com/repos/Svotin/chat-bot/commits?sha= '

    session = requests.Session()

    login =  input("login")
    password =  getpass.getpass()

    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        exit(0)
    vk = vk_session.get_api()

    comits = requests.get(url).json()
    try:
        lastCommit = comits[0]
    except Exception as error:
        vk.messages.send(user_id = 445159253, message = "Ваша программа остановилась с ошибкой: '"+ str(error)+ "'")
        exit(0)

    lastDate = lastCommit['commit']['author']['date'].replace("-"," ").replace('T'," ").replace(':'," ").replace("Z"," ").split()
    lastDate = datetime.datetime(int(lastDate[0]),int(lastDate[1]),int(lastDate[2]),int(lastDate[3])
                ,int(lastDate[4]),int(lastDate[5]))

    while(True):
        time.sleep(60)
        comits = requests.get(url).json()
        try:
            newCommit = comits[0]
        except Exception as error:
            vk.messages.send(user_id = 445159253, message ="Ваша программа остановилась с ошибкой: '"+ str(error)+"'")
            exit(0)
        newCommitDate = newCommit['commit']['author']['date'].replace("-"," ").replace('T'," ").replace(':'," ").replace("Z"," ").split()
        newCommitDate = datetime.datetime(int(newCommitDate[0]),int(newCommitDate[1]),int(newCommitDate[2]),int(newCommitDate[3])
                ,int(newCommitDate[4]),int(newCommitDate[5]))
        if newCommitDate>lastDate:
            message = 'New Git\n\n' + newCommit["commit"]['message']+"\n"+newCommit['html_url']
            vk.messages.send(user_id = 445159253, message = message)
            lastDate = newCommitDate


if __name__ == '__main__':
    main()