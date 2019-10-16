import os
import subprocess
 
import pytube

import test_firebase

while(True):
    docs = test_firebase.db.collection(u'links').where(u'flag', u'==', 0).stream()

    for doc in docs:
        
        dict_doc = doc.to_dict()    #link
        id_doc = doc.id             #document id

        link = dict_doc.get("link")

        #print(type(link))

        yt = pytube.YouTube(link) #to download

        vids= yt.streams.all()

        vnum = 0

        for i in range(len(vids)):
            if str(vids[i]).find("mp4") != -1 :
                print(i,'. ',str(vids[i]))
                vnum = int(i)
                break
        
        parent_dir = "/home/dongsuk/Downloads" #save path
        vids[vnum].download(parent_dir) #start download
        test_firebase.db.collection("links").document(id_doc).update({"flag": 1})

    

#print('Complete!!')

    # break
# yt = pytube.YouTube("https://www.youtube.com/watch?v=kvBR-cbF1Ag") #다운받을 동영상 URL 지정
 
# vids= yt.streams.all()
 
# #영상 형식 리스트 확인
# for i in range(len(vids)):
#     print(i,'. ',vids[i])
 
# vnum = int(input("다운 받을 화질은? "))
 
# parent_dir = "C:/Users/orio1001/Desktop/workspace/10" #저장 경로 지정(Windows or mac)
# vids[vnum].download(parent_dir) #다운로드 수행
 
# # new_filename = input("변환 할 mp3 파일명은?")
 
# # default_filename = vids[vnum].default_filename 
# # subprocess.call(['ffmpeg', '-i',                 #cmd 명령어 수행
# #     os.path.join(parent_dir, default_filename),
# #     os.path.join(parent_dir, new_filename)
# # ])
 
# print('Complete!!')