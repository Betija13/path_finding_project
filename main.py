from cela_algoritms_karte import get_path_map

instructions, output_1, output_2 = get_path_map(start_cab=123, end_cab=609, use_elevator=False,
                                                language='LV',
                                                destination_file_1='./path_pics/123_lifts.png',
                                                destination_file_2='./path_pics/lifts_wc.png')

print(instructions)
print(output_1)
print(output_2)
