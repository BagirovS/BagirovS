from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker

#Defalt values
menu = """
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
"""
today = datetime.today()
Base = declarative_base()


class Table (Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        #return self.task
        return self.task



engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base.metadata.create_all(bind=engine)

def read_task(today):
    #Read tasks in table 'task'
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(Table).filter(Table.deadline == today.date()).order_by(Table.deadline).all()
    session.close()
    return rows

def insert_task(string_value, date):
    #Insert tasks in table 'task'
    Session = sessionmaker(bind=engine)
    session = Session()
    new_row = Table(task=string_value,
                    deadline=datetime.strptime(date, '%Y-%m-%d').date())
    session.add(new_row)
    session.commit()
    session.close()

def read_all_task():
    #Read tasks in table 'task'
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(Table).order_by(Table.deadline).all()
    session.close()
    return rows

def read_missed_tasks():
    #Read tasks in table 'task'
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(Table).filter(Table.deadline < datetime.today()).order_by(Table.deadline).all()
    session.close()
    return rows

def del_task(row_number):
    #Read tasks in table 'task'
    Session = sessionmaker(bind=engine)
    session = Session()
    #rows = session.query(Table).filter(Table.task == task_name).all()
    rows = session.query(Table).order_by(Table.deadline).all()
    specific_row = rows[row_number]
    session.delete(specific_row)
    session.commit()
    session.close()
    pass

def main_engine():
    while True:
        step = int(input(menu))
        if step == 1:
            print(f'Today {today.strftime("%-d %b")}:')
            to_day = read_task(today)
            if len(to_day) > 0:
                number = 1
                for t in to_day:
                    print(f'{number}. {t}')
                    number += 1
            else:
                print('Nothing to do!')
        elif step == 2:
            for i in range(7):
                date_week = today + timedelta(days=i)
                print(f'\n{date_week.strftime("%A %-d %b")}:')
                week_task = read_task(date_week)
                if len(week_task) > 0:
                    number = 1
                    for w in week_task:
                        print(f'{number}. {w}')
                        number += 1
                else:
                    print('Nothing to do!')
        elif step == 3:
            print('All tasks:')
            all_task = read_all_task()
            if len(all_task) > 0:
                number = 1
                for a in all_task:
                    print(f'{number}. {a}. {a.deadline.strftime("%-d %b")}')
                    number += 1
            else:
                print('Nothing to do!')
        elif step == 4:
            missed_tasks = read_missed_tasks()
            if len(missed_tasks) > 0:
                number = 1
                for m in missed_tasks:
                    print(f'{number}. {m}. {m.deadline.strftime("%-d %b")}')
                    number += 1
            else:
                print('Nothing is missed!')
        elif step == 5:
            new_task = input('Enter task')
            date = input('Enter deadline')
            insert_task(new_task, date)
            print('The task has been added!')
        elif step == 6:
            print('Choose the number of the task you want to delete:')
            all_task = read_all_task()
            if len(all_task) > 0:
                number = 1
                for a in all_task:
                    print(f'{number}. {a}. {a.deadline.strftime("%-d %b")}')
                    number += 1
                del_row = int(input()) - 1
                print(del_row)
                del_task(del_row)
                print('The task has been deleted!')
            else:
                print('Nothing to delete')
        elif step == 0:
            print('Bye!')
            break

main_engine()











