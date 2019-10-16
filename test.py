import test_firebase

link = 'https://www.youtube.com/watch?v=v07C143sevo'

saved = test_firebase.db.collection(u'links').where(u'link', u'==', link).get()


for sv in saved:
    if(len(sv.to_dict()) > 0):
        print("ture!!!")
