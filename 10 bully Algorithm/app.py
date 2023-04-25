import time

class Process:
    def __init__(self, process_id, num_processes):
        self.process_id = process_id
        self.coordinator_id = None
        self.num_processes = num_processes
        self.is_coordinator = False

    def send_election_message(self):
        print(f"Process {self.process_id} sends election message to higher priority processes")
        for i in range(self.process_id + 1, self.num_processes + 1):
            # send election message to higher priority processes
            time.sleep(0.5)
            print(f"Process {self.process_id} sends election message to Process {i}")
            if i == self.num_processes:
                self.become_coordinator()

    def become_coordinator(self):
        self.is_coordinator = True
        self.coordinator_id = self.process_id
        print(f"Process {self.process_id} becomes coordinator")

    def send_coordinator_message(self):
        print(f"Process {self.process_id} sends coordinator message to other processes")
        for i in range(1, self.num_processes + 1):
            if i != self.process_id:
                # send coordinator message to all other processes
                time.sleep(0.5)
                print(f"Process {self.process_id} sends coordinator message to Process {i}")

    def run(self):
        while True:
            if self.is_coordinator:
                # do coordinator tasks
                time.sleep(1)
                print(f"Process {self.process_id} is doing coordinator tasks")
            else:
                # send election message to higher priority processes
                self.send_election_message()

            time.sleep(2)

if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))

    processes = []

    for i in range(1, num_processes + 1):
        processes.append(Process(i, num_processes))

    # start the processes
    for process in processes:
        process.run()