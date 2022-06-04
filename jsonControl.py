# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 17:32:09 2022

@author: shimalab
"""

import json
import numpy as np
from operator import itemgetter


# 人を追加
def registerPerson(i, name, exp, history, person_list):
    '''===人を追加===
    i       [int] : 登録ID,
    name    [str] : 名前,
    exp     [int] : これまでの仕事量,
    history [str] : 前回の仕事,
    person_list [dic] : 追加先の辞書リスト（return）
    =============='''
    add_person = {"name": name, "exp": exp, 'history': history}
    person_list['person'+str(i)] = add_person
    return person_list


# 仕事を追加
def registerWork(i, name, weight, need, work_list):
    '''===仕事を追加===
    i      [int] : 登録ID,
    name   [str] : 仕事名,
    weight [int] : この仕事の重さ,
    need   [int] : 必要人数,
    work_list [dic] : 追加先の辞書リスト（return）
    =============='''
    add_work = {"name": name, "weight": weight, 'need': need}
    work_list['work'+str(i)] = add_work
    return work_list


# 人，仕事を削除
def deleteObject(my_list, name):
    my_list.pop(name)
    return my_list


# 人，仕事をJSONファイルへ出力
def jsonWrite(path, my_list):
    with open(path, mode='w') as file:
        json.dump(my_list, file, ensure_ascii=False, indent=2)


# JSONファイルから読み取り，人，仕事オブジェクトへ
def jsonRead(path):
    with open(path, mode='r') as file:
        data = json.load(file)
    return data


# 追加や削除を行う用の配列
def copyArray(array):
    copy = array
    return copy


# 仕事量からメンバーを選択し，出力
# def selectMember():


# 名前探索
def nameSearch(name, person_list):
    person_ids = [key for key, dic in person_list.items() if dic['name'] == name]
    return person_ids

# 履歴チェック
def historyCheck(sorted_person, sorted_work):
    person_count = 0
    history_result = np.zeros(len(sorted_work))  # 履歴のworkと今回のworkが被りフラグ
    for i in range(len(sorted_work)):
        capacity = sorted_work[i]['need']

        for j in range(capacity):
            # 履歴のworkと今回のworkが被ったとき
            if sorted_person[person_count]['history'] == sorted_work[i]['name']:
                history_result[i] = 1
            person_count += 1

    return(history_result)


# #仕事の順番入れ替え
# def change_work(sorted_work,history_result):
#     for i in range(len(sorted_work)):
#         if history_result[i] == 1:
#             if



if __name__ == "__main__":
    person_list = dict()
    work_list = dict()
    history = []
    totalnum = 2

    person_l = dict()

    # path_person='C:\\Users\\shimalab\\Desktop\\person.json'
    # path_work='C:\\Users\\shimalab\\Desktop\\work.json'
    # path_person = '.'
    # path_work = '.'
    # json_person_read(path_person)
    # json_work_read(path_work)

    # テスト用
    person_list = registerPerson(1, 'Aさん', 5, 'pointE', person_list)
    person_list = registerPerson(2, 'Bさん', 6, 'pointC', person_list)
    person_list = registerPerson(3, 'Cさん', 9, 'pointG', person_list)
    person_list = registerPerson(4, 'Dさん', 4, 'pointA', person_list)
    person_list = registerPerson(5, 'Eさん', 2, 'pointC', person_list)
    person_list = registerPerson(6, 'Fさん', 3, 'pointD', person_list)
    person_list = registerPerson(7, 'Gさん', 8, 'pointF', person_list)
    person_list = registerPerson(8, 'Hさん', 6, 'pointB', person_list)
    person_list = registerPerson(9, 'Iさん', 7, 'pointE', person_list)
    person_list = registerPerson(10, 'Jさん', 1, 'pointD', person_list)
    person_list = registerPerson(11, 'Kさん', 5, 'pointF', person_list)
    work_list = registerWork(1, 'pointA', 2, 1, work_list)
    work_list = registerWork(2, 'pointB', 5, 1, work_list)
    work_list = registerWork(3, 'pointC', 3, 2, work_list)
    work_list = registerWork(4, 'pointD', 4, 2, work_list)
    work_list = registerWork(5, 'pointE', 2, 2, work_list)
    work_list = registerWork(6, 'pointF', 1, 2, work_list)
    work_list = registerWork(7, 'pointG', 1, 1, work_list)


    copy_person = copyArray(person_list)
    copy_work = copyArray(work_list)


    # 仕事量順でソート
    p_value = [dic for key, dic in copy_person.items()]
    sorted_person = sorted(p_value, key=itemgetter('exp'))

    w_value = [dic for key, dic in copy_work.items()]
    sorted_work = sorted(w_value, key=itemgetter('weight'), reverse=True)


    # ここから仕事の割り当て
    history_result = historyCheck(sorted_person, sorted_work)


