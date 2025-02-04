class Worker:
    def __init__(self, worker_num, fname, lname, work_experience_company, total_years_experience,
                 salary, age):
        self.worker_num = worker_num
        self.fname = fname
        self.lname = lname
        self.work_experience_company = work_experience_company
        self.total_years_experience = total_years_experience
        self.salary = salary
        self.age = age

    def worker_information(self):
        print(f"{self.fname} {self.lname} със служебен номер {self.worker_num} със трудов стаж във фирмата от"
              f"{self.work_experience_company} години и общо със стаж от {self.total_years_experience} години.")

    def salary_bonus(self):
        bonus = 0.0
        if self.work_experience_company >= 5 and self.work_experience_company <= 10:
            bonus = 0.015
        elif self.work_experience_company > 10:
            bonus = 0.02
        elif self.total_years_experience < 5:
            bonus = 0.005
        self.salary =+ (self.salary * bonus)

n = int(input())
worker_list = list()

for i in range(n):
    print("Въведете информация за работник:")
    worker_num = int(input("Служебен номер: "))
    fname = input("Име: ")
    lname = input("Фамилия: ")
    work_exp_company = int(input("Стаж във фирмата: "))
    total_exp = int(input("Общ стаж: "))
    salary = float(input("Заплата: "))
    age = int(input("Възраст: "))

    worker = Worker(worker_num, fname, lname, work_exp_company, total_exp, salary, age)
    worker_list.append(worker)

def search_by_num(worker_list, worker_num):
    if worker_list.index(worker_num) > -1:
        return True
    else:
        return False

search_by_num(worker_list, 121224070)

def search_by_name_experience(worker_list, name, experience):
    for w in worker_list:
        if w.fname == name and w.work_experience_company == experience:
            w.worker_information()

def add_worker(worker_list):
    print("Въведете информация за работник:")
    w_num = int(input("Служебен номер: "))
    name = input("Име: ")
    family = input("Фамилия: ")
    company_experience = int(input("Стаж във фирмата: "))
    total_experience = int(input("Общ стаж: "))
    salary = float(input("Заплата: "))
    age = int(input("Възраст: "))

    worker = Worker(w_num, name, family, company_experience, total_experience, salary, age)
    worker_list.append(worker)

def remove_worker(worker_list, worker_num):
    ind = worker_list.index(worker_num)
    if ind > -1:
        worker_list.pop(ind)
        print("Information deleted!")
    else:
        print("Wrong worker num")







