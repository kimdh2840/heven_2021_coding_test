'''
시작 시각 :  21:00
종료 시각 :  21:40


다음 코드에서, 출력되는 결과값이 왜 실제 출력되어야 하는 결과값보다 작은지 설명하시오.

해당 문제점을 해결하기 위해 사용해야 하는 해결책을 서술하고,
해당 개념을 자율차 코드에 적용하였을 때
1) 어느 부분에 적용할 수 있을지,
2) 이를 통해 어떤 이점을 얻을 수 있는지
서술하시오.

(Optional) 아래 코드의 실행 결과값이 실제 출력되어야 하는 결과값과 동일하게 출력되도록 변경하시오.

*** Write Your Answer Below ***
원래의 코드대로 돌리면 쓰레드가 돌아가면서 threads에 값이 더해지기 때문에 정확히 limit와 thread_num에 다른 값이 더해지지 않는다.
하지만 for문 안에 tread.join()을 추가해주어 작업이 돌아가면 for문 내에서 쓰레드의 종료까지 대기하기 떄문에
append 작업을 모두 limit 값까지 모두 실행할 수 있게 되어 원하는 값을 얻을 수 있다.
1,2) 자율주행을 구현할 때는 여러가지의 기능(함수?)을 동시에 실행해야 하기 때문에 쓰레드를 통해 여러가지의 작업을 구현할 수 있을 것이다.
     이때 fork와 join을 재때 해주어 작업을 잘 분할하고 끝마치게 관리해줄 수 있다면 작업 효율이 좋아질 것이고
     그만큼 속도도 향상시킬 수 있을 것이다.
     또한 join을 통해 쓰레드를 실행하면서 중간에 다른 작업이 진행될 예정이라도 실행하던 특정 작업을 제대로 끝마치게 할 수 있다.

*** Your Answer Ends Here ***
'''


from threading import Thread


class Count:
    def __init__(self):
        self.count = 0

    def add_offset(self, offset):
        self.count += offset


def worker(idx, limit, count_obj):
    print(idx)
    for _ in range(limit):
        count_obj.add_offset(1)


def run_threads(func, thread_num, limit, count_obj):
    threads = []
    for i in range(thread_num):
        args = (i, limit, count_obj)
        thread = Thread(target=func, args=args)
        threads.append(thread)
        thread.start()

#    for thread in threads:    # 이 부분 빼고 밑의 thread.join 위로 붙이면 됩니다.
        thread.join()



limit = 10 ** 6
thread_num = 7
count = Count()
run_threads(worker, thread_num, limit, count)
print(f"Result should be {thread_num * limit}, but the total count is {count.count}")
