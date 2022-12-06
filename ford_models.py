maverick_path = '//div[@class="veh-item-2"]/div[@class="img-wrap"]/a[@class="img-link"]/picture/img[@alt="2023 Ford Maverick® XLT in Area 51"]'
maverick_url = "https://www.ford.com/trucks/maverick/?gnav=header-trucks-vhp"
maverick_txt = "2023 FORD MAVERICK"

f150_path = '//div[@class="veh-item-2"]/div[@class="img-wrap"]/a[@class="img-link"]/picture/img[@alt="2023 Ford F-150® XLT passenger side profile in Atlas Blue"]'
f150_url = "https://www.ford.com/trucks/f150/?gnav=header-trucks-vhp"
f150_txt = "2023 FORD F-150"


maverick = [maverick_path, maverick_url, maverick_txt]
f150 = [f150_txt, f150_url, f150_path]

ford_trucks = (maverick, f150)

