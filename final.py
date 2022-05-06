class Worldcup:
    def golden_globe(defnece,shoot,name):
        defence_well = 0
        defence_well_probability = []
        golden_glove = 0
        for i in range(len(defnece)):
            defence_well = (defnece[i])/(shoot[i])
            defence_well_probability.append(defence_well)
            print(names[i],'선방율:',defence_well_probability[i]*10)
        for j in range(len(shoot)):
            if(golden_glove < defence_well_probability[j]):
                golden_glove = defence_well_probability[j]
                best_1 = j
        print('golden glove:',names[best_1])
        print('최고 경기 선방률:',golden_glove*10)
    def best_attack(shoot_1, goal_1,names):
        pro = 0
        goal_probability = []
        best_shooter = 0
        for i in range(len(goal_1)):
            pro = (goal_1[i])/(shoot_1[i])
            goal_probability.append(pro)
            print(names[i],'득점확률:',goal_probability[i]*100)
        for j in range(len(shoot_1)):
            if(best_shooter < goal_probability[j]):
                best_shooter = goal_probability[j]
                best_2 = j
        print('최고의 슛터:',names[best_2])
        print('슛 성공률:',best_shooter*100)
    def best_defence(try_defence,success_defence,names):
        defnece = 0
        defence_probability = []
        best_defence = 0
        for i in range(len(success_defence)):
            defence = (success_defence[i])/(try_defence[i])
            defence_probability.append(defence)
            print(names[i],'수비 방어율:',defence_probability[i]*100)
        for j in range(len(try_defence)):
            if(best_defence < defence_probability[j]):
                best_defence = defence_probability[j]
                best = j
        print('최고의 수비수:',names[best])
        print('태클 성공률:',best_defence*100)
    def golden_shoe(goals,names):
        max = goals[0]
        count = 0
        count2 = 0
        player = []
        for i in range(len(goals)):
            if (max < goals[i]):
                max = goals[i]
                st = i
            elif (max == goals[i]):
                count += 1
                if count>=3:
                    print('추가 기록 확인 필요')
                    print('maximum_goal:',max)
                    for j in range(len(names)):
                        if (max == goals[j]):
                            print('해당 선수:',names[j])
                            count2 +=1
            else:
                continue
        if count2 == 0:
            print('golden shoe:',names[st],'goal:',max)
        return max
shoot = [15,13,12,7,13,8,16,12,20]
defnece = [8,3,2,5,7,4,2,4,3]
shoot_1 = [8,6,6,4,13,7,2,1,16]
goal_1 = [8,3,2,2,7,4,2,0,12]
try_defence = [10,3,2,7,13,8,6,12,20]
success_defence = [8,3,2,5,7,4,2,4,12]
goals = [10,3,2,7,13,8,6,12,14]
names = ['A선수','B선수','C선수','D선수','E선수','F선수','G선수','H선수','I선수']
Worldcup.golden_globe(shoot,defnece,names)
Worldcup.best_attack(shoot_1, goal_1,names)
Worldcup.best_defence(try_defence,success_defence,names)
max = Worldcup.golden_shoe(goals,names)

#+ 득점기록 같을 때 슛팅 성공률로 판단
#+ 선방률 같으면 경기 수로 판단
#+ 태클 성공률 같으면 태클성공 횟수 더 높은거로 판단
