import csv
import os

default_members = [
    {"id":1,"name":"田中","age":15},{"id":2,"name":"佐藤","age":21}
]


def export_to_csv(filename,members=None):
    if members is None:
        members =[]
        
    with open(filename,"w",newline="",encoding="utf-8")as file:
        fieldnames=["id","name","age"]
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(members)
        
    full_path = os.path.abspath(filename)  
    print(f"{filename}に書き込みを行いました\n保存場所:{full_path}")
        
def import_from_csv(filename):
    members=[]
    if os.path.exists(filename):
        with open(filename,"r",newline="",encoding="utf-8") as file:
            reader =csv.DictReader(file)
            for row in reader:
                members.append({
                  "id":int(row["id"]),"name":row["name"],"age":int(row["age"])
                })
            return members
filename = "members.csv"
members=import_from_csv(filename) or default_members
    

#リストに追加する
while True:
    menu = int(input("行いたい動作を選択してください\n0:リスト参照\n1:リストの追加\n2:会員を検索\n3:会員を削除\n4:csv出力\n>>"))
    #0:リストの参照
    if(menu==0):
        print(members) 
    #1:リストの追加
    if(menu==1):
        while True:
            answer=input("メンバーを追加しますか?(yes/no)").lower()
            if answer in ["yes","no"]:
                break
            print("yesかnoを入力してください")

        if answer == "yes":
            new_name=input("名前を入力してください>>")
            new_age=int(input("年齢を入力してください>>"))
            new_id = max([member["id"]for member in members],default=0)+1
            new_member={"id":new_id,"name":new_name,"age":new_age} #{}は辞書
            members.append(new_member)
            print("追加しました\n",members)

    #2:会員を検索
    elif(menu==2):
        search_id =int(input("検索したいidを入力してください"))
        found = False
        
        for member in members:
            if member["id"]==search_id: #1回目のループ: member に {"id": 1, "name": "田中", "age": 15} が入る。membersだと{id:2~}も含んでしまう
                print("会員情報",member)
                found =True
                break
        if not found:
            print("指定されたidは見つかりませんでした")
            
    #3:会員を削除
    elif(menu==3):
        delete_id =int(input("削除したいidを入力してください"))
        found = False
        
        for member in members:
            if member["id"]==delete_id: #1回目のループ: member に {"id": 1, "name": "田中", "age": 15} が入る。membersだと{id:2~}も含んでしまう
                members.remove(member)
                print(f"ID{delete_id}は削除できました\n",members)
                found =True
                break
        if not found:
            print("指定されたidは見つかりませんでした")
            
    elif(menu==4):
        while True:
            answer=input("csv出力しますか?(yes/no)").lower()
            if answer in ["yes","no"]:
                break
            print("yesかnoを入力してください")
        if answer == "yes":
            export_to_csv(filename,members)

            
         
