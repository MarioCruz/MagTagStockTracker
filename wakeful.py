import json
import math
import alarm

def store_data(data: dict) -> None:
    dump = json.dumps(data).encode('utf-8')
    mem_size = len(dump)
    n = math.floor(mem_size/255)
    m = mem_size % 255
    alarm.sleep_memory [0] = n
    alarm.sleep_memory [1] = m
    alarm.sleep_memory [2:mem_size+2] = dump


# Load data stored on the RAM
def load_data() -> dict:
    try:
        mem_size = 255 * alarm.sleep_memory[0] + alarm.sleep_memory[1]
        data = json.loads(alarm.sleep_memory[2:mem_size+2].decode('utf-8'))
        return data

    except (ValueError, RuntimeError) as e:
        data=99999
        return data
