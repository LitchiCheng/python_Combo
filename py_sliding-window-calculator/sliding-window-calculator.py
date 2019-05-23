
# encoderLines = 1024
# reductionRatio = 1
# PI = 3.14159265358979
# m_pos_reduce_rate = encoderLines * 4 * reductionRatio
# critical_delta = 55 #(m_pos_reduce_rate * 0.000015) / (2.0 * PI * ((0.09000 * 1000) / 1000.0)) + 1.0
# print("critical_delta:" + str(critical_delta))
# print("一圈count:" + str(m_pos_reduce_rate))
# v1 = ((critical_delta / 4096) * (2 * PI * 0.09)) / 0.5
# v2 = (critical_delta / 4096) * 360 / 0.5
# print("轮周长m：" + str((2 * PI * 0.09)))
# print("最小m/s：" + str(v1))
# print("最小°/s：" + str(v2))

import random
ODO_STOP_TIME_WINDOW = 50
time = 1000                      #50的滑动窗口，100次动作，在高点也可以。
m_odo_sum = 0
m_odo_time_window_counter = 0
m_odo_time_window_data = [0] * ODO_STOP_TIME_WINDOW         #全0的数组
while(time):
    wheelpos = random.randint(-1, 1)
    m_odo_sum = m_odo_sum - m_odo_time_window_data[m_odo_time_window_counter] + wheelpos            #用随机整数来模拟轮子前后摆动+-

    # replace by new value
    m_odo_time_window_data[m_odo_time_window_counter] = wheelpos

    m_odo_time_window_counter = 1 + m_odo_time_window_counter           #python不能用++

    if (m_odo_time_window_counter >= ODO_STOP_TIME_WINDOW): 
        m_odo_time_window_counter = 0

    print('m_odo_time_window_counter: %d' %m_odo_time_window_counter)

    time = time - 1

    print(m_odo_sum)
