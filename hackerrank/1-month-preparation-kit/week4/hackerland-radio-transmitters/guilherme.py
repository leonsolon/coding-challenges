from bisect import bisect

def hackerlandRadioTransmitters(x, k):
    x.sort()
    start_signal = -1
    end_signal = -1
    transmitters = 0
    for i, house in enumerate(x):
        if not (house >= start_signal and house <= end_signal):
            next_place_transmitter_idx = bisect(x, house + k) - 1

            start_signal = x[next_place_transmitter_idx] - k
            end_signal = x[next_place_transmitter_idx] + k
            # print(next_place_transmitter_idx,x[next_place_transmitter_idx], start_signal, end_signal)
            transmitters += 1
    return transmitters
