import numpy as np

from .max30102 import MAX30102
from .hrcalc import calc_hr_and_spo2
from infra.hardware.max30102.models.max30102_response import MAX30102Response


class HeartRateMonitor(object):
    def __init__(self, print_raw=False, print_result=True) -> None:
        self.bpm = 0
        self.print_raw = print_raw
        self.print_result = print_result

    def get_readings(self) -> MAX30102Response:
        sensor = MAX30102()
        ir_data = []
        red_data = []
        bpms = []

        i = 0
        bpm_list = []
        spo2_list = []

        # run until told to stop
        while i <= 4:
            # check if any data is available
            num_bytes = sensor.get_data_present()
            if num_bytes > 0:
                # grab all the data and stash it into arrays
                while num_bytes > 0:
                    red, ir = sensor.read_fifo()
                    num_bytes -= 1
                    ir_data.append(ir)
                    red_data.append(red)

                while len(ir_data) > 100:
                    ir_data.pop(0)
                    red_data.pop(0)

                if len(ir_data) == 100:
                    bpm, valid_bpm, spo2, valid_spo2 = calc_hr_and_spo2(
                        ir_data, red_data
                    )
                    if valid_bpm:
                        bpms.append(bpm)
                        while len(bpms) > 4:
                            bpms.pop(0)
                        self.bpm = np.mean(bpms)
                        if np.mean(ir_data) < 50000 and np.mean(red_data) < 50000:
                            self.bpm = 0
                            if self.print_result:
                                print("Finger not detected")
                        if self.print_result:
                            if spo2 != -999:
                                i += 1
                                bpm_list.append(float(self.bpm))
                                spo2_list.append(spo2)

        return MAX30102Response(
            bpm=round(sum(bpm_list) / len(bpm_list), 2),
            oxygenation_percentage=round(sum(spo2_list) / len(spo2_list), 2),
        )
