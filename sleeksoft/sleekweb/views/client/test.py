import json
from bs4 import BeautifulSoup

# Mã HTML được nhập vào dưới dạng chuỗi
html_content = """
<div class="grid grid-cols-1 lg:grid-cols-2 w-full lg:w-[1597px] mt-[20px] lg:mt-[50px] gap-6 px-[20px] lg:px-none">
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/Facebook-photo-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Citrine Derma Clinic</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">Số 6 – 8 Raymondienne, Phường Tân Phú, Quận 7, TP.HCM</span>
                <a href="https://citrinedermaclinic.vn/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/Facebook-Photo-1-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Shine Premium Clinic</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">6 Trương Quyền, phường Võ Thị Sáu, Quận 3</span>
                <a href="https://www.facebook.com/Shinepremium.TSBSAnh?mibextid=JRoKGi" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/ROHTO-AOHAL-CLINIC-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">ROHTO AOHAL CLINIC</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">CN 1: 02 Phạm Đình Toái, Phường Võ Thị Sáu, Quận 3, TP. HCM CN 2: 207/4 Nguyễn Văn Thủ, Phường Đa Kao, Quận 1, TP. HCM CN 3: 50 Nguyễn Thị Thập, Phường Tân Hưng, Quận 7, TP. HCM</span>
                <a href="https://rohtoaohalclinic.com.vn/en/main.html" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/A-Dong-logo-640x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Á Đông Clinic</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">236 Điện Biên Phủ, P6, TP Sóc Trăng, tỉnh Sóc Trăng</span>
                <a href="https://thammyadong.com/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="https://hydrinity.com.vn/wp-content/uploads/2023/12/about_icon.png">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Phòng khám da liễu bác sĩ Trương Lê Anh Tuấn</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">19 Mai Văn Vĩnh, Tân Quy, Quận 7, Thành phố Hồ Chí Minh</span>
                <a href="https://drthuyan.com/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/share_fb_home-764x400.webp">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Pk Thẩm Mỹ Yenclinic</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">Hẻm 320 Độc Lập, phường Tân Quý, quận Tân Phú, tp. Hồ Chí Minh</span>
                <a href="https://yenclinic.com.vn/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/Facebook-Photo-1-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Shine Premium Clinic</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">6 Trương Quyền, phường Võ Thị Sáu, Quận 3</span>
                <a href="https://www.facebook.com/Shinepremium.TSBSAnh?mibextid=JRoKGi" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/Bv-Da-Khoa-Tam-Anh-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Bv Đa Khoa Tâm Anh</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">2B Phổ Quang, Phường 2, Q. Tân Bình, TPHCM</span>
                <a href="https://tamanhhospital.vn/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/home_bs_tu_vn-01-800x292.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">PKCK Thẩm Mỹ Bs Tú</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">290 - 292 Trần Hưng Đạo, Quận 1, Tp.HCM.</span>
                <a href="https://www.bacsitu.com/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/DR-REU-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Bs Hồng Cẩm - Reju Beauty Medi</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">L3_ RR13 Hồng Lĩnh, phường 15, quận 10, Tp.HCM.</span>
                <a href="https://www.facebook.com/bsvananh/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/416190363_866345498832204_985366787642224682_n-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Dr Chang Skin</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">241 Chu Văn An, phường 12, quận Bình Thạnh, Ho Chi Minh City, Vietnam</span>
                <a href="https://www.facebook.com/drchangskin.com.vn" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/Dermatology-Clinic-Logo-1-1.png">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Phòng khám da liễu bác sĩ Hà Thị Thúy An</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">121/28 Phạm Ngọc Thạch, Hiệp Thành, Thủ Dầu Một, Bình Dương</span>
                <a href="https://drthuyan.com/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/Facebook-post-image-1.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Thẩm mỹ viện bác sĩ Tú</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">290 - 292 Trần Hưng Đạo, Quận 1</span>
                <a href="https://www.bacsitu.com/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/Facebook-post-image-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Hanah Clinic</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">59 Trần Quốc Thảo, phường Võ Thị Sáu, quận 3, Ho Chi Minh City, Vietnam</span>
                <a href="https://hanahskin.com/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/Screenshot-2024-06-04-at-17.05.49.png">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Phòng khám da liễu Skinone</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">259 đường 3/2, phường 10, Quận 10, Tp.HCM</span>
                <a href="https://skinone.vn/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/images-2.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Phòng Khám Da Liễu Thẩm Mỹ - MYSS By Dr Anna</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">33 Đường 34A, Phường An Phú, Quận 2, Ho Chi Minh City, Vietnam</span>
                <a href="https://myss.clinic/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/355506793_154128127673065_8476678691730276950_n-398x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Au aesthetic clinic</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">290/24 Nam Kỳ Khởi Nghĩa, Phường Võ Thị Sáu, Quận 3, Ho Chi Minh City, Vietnam</span>
                <a href="https://www.facebook.com/p/Au-aesthetic-clinic-100092276352290/?_rdr" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/images-3.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">PENSILIA BEAUTY CLINIC</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">413 – 415 Nguyễn Đình Chiểu, P5, Q.3, TP.HCM</span>
                <a href="https://pensilia.com/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/images.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">BichNa Clinic</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">157-159 Nguyễn Đình Chiểu, P. Võ Thị Sáu, Q. 3, Ho Chi Minh City, Vietnam</span>
                <a href="https://www.bichnaclinic.com/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/335662628_215967730984175_7565151089519993478_n-402x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">TS.BS Ngọc Trai - Da liễu Thẩm mỹ Pearl Clinic</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">595 Quang Trung, Hà Đông, H1057 Nguyễn Trãi, Phường 14, Quận 5, TP HCMN</span>
                <a href="https://www.facebook.com/pkdalieubsngoctrai" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/447771388_122095982438355281_9091761410356574983_n-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Skin Plus Dermatology</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">85 Hoa Lan, Phường 2, Quận Phú Nhuận, Ho Chi Minh City, Vietnam</span>
                <a href="https://www.facebook.com/skinplusdermatologychamsocda/?_rdr" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/images-4.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">BRIGHT BEAUTY BY Dr. Brian</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">393/26 Trần Hưng Đạo, P Cầu Kho, Q1</span>
                <a href="https://www.facebook.com/DrBroi2202/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/4-400x400.png">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Goncy Clinic</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">196 Đ. Lê Lai, Phường Phạm Ngũ Lão, Quận 1, Hồ Chí Minh</span>
                <a href="https://www.goncy.vn/vi" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/alma-clinic-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">ALMA Clinic by Ts.Bs Trần Ngọc Ánh</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">290 Nguyễn Thị Minh Khai phường 5 quận 3 , Ho Chi Minh City</span>
                <a href="https://phongkhamalma.com/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/cropped-PMT-Aesthetic-Clinic-Logo-512-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">PMT Aesthetic Clinic - Phòng Khám Chuyên Điều Trị Nám Da</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">60 Đường Sương Nguyệt Ánh, Phường Phạm Ngũ Lão, Quận 1,             Hồ Chí Minh</span>
                <a href="https://pmtclinic.vn/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/337243983_971551137594571_7309998303933008674_n-710x400.png">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">TS.BS. Hồng Chuyên - PK Da liễu Thẩm mỹ da</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">35/5D Trần Đình Xu, Quận 1, Tp.HCM</span>
                <a href="https://www.facebook.com/hongchuyenclinic/?locale=hi_IN" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/428703625_811440191027789_1490755852771109775_n-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">ROHTO AOHAL CLINIC</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">207/4 Đ. Nguyễn Văn Thủ, Đa Kao, Quận 1, Hồ Chí Minh</span>
                <a href="https://rohtoaohalclinic.com.vn/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/BS-Mi-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">PKDL Bs Mi</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">51 Nguyễn Hiền, Quận 3, Tp.HCM.</span>
                <a href="https://www.facebook.com/BSCKIIDALIEUNGUYENLETRAMI/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/444455627_122148431012227706_2781616255863926001_n-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">BS Trần Anh Đức</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">33/20B Nguyễn Đình Chính, Phường 15, Quận Phú Nhuận, Tp.HCM</span>
                <a href="https://www.facebook.com/share/19sQEVqbfu/?mibextid=wwXIfr" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/DR-LE-Tam.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">PK da Laser TM Lê Tâm</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">198 Lê Hồng Phong, phường 3, TP Sóc Trăng</span>
                <a href="https://www.facebook.com/p/Ph%C3%B2ng-Kh%C3%A1m-Da-Li%E1%BB%85u-Laser-Th%E1%BA%A9m-M%E1%BB%B9-L%C3%AA-T%C3%A2m-100063983466011/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/PK-da-Lieu-TM-AV-Bs-Thuy-Anh.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">PK da Liễu TM AV</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">50 Hẻm 449 Sư Vạn Hạnh, Phường 12, Q10, Tp.HCM.</span>
                <a href="https://www.bsthuyanhdalieu.com/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/procare-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Bs Đông Hải - Procare Skin Clinic</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">19 Nhiêu Tứ, P.7, Q. Phú Nhuận, Tp.HCM.</span>
                <a href="https://www.facebook.com/procareskinclinic/?locale=vi_VN" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/medskin-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Medskin Clinic - BS Nguyễn Minh Phát Đạt</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">60 Đinh Công Tráng, p.Tân Định, q.1, Tp.HCM.</span>
                <a href="https://www.facebook.com/MEDSkinClinicHCM" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/BS-Phuong-Trang-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Bs Trang  PT Clinic Beauty Cosmetic</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">21 lô C khu đô thị Golden Kim Oanh, quốc lộ 13, khu phố 3,  phường Mỹ Phước, Tx.Bến Cát, tỉnh Bình Dương</span>
                <a href="https://www.facebook.com/Dalieuthammy93/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/Phong-Kham-Nha-Khoa-Kaiyen.png">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Phòng Khám Nha Khoa Kaiyen  MS Diễm</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">99 Trần Não, P.An Khánh,  Q. 2, Tp.Thủ Đức</span>
                <a href="https://nhakhoakaiyen.com/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/vita-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">TMV VITA CLINIC - Bs Tuấn</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">Lầu 4, SC Vivo City - 1058 Nguyễn Văn Linh, P. Tân Phong, Q.7</span>
                <a href="https://vitaclinic.vn/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/images.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Dr Duy Hải</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">Số 10, Đường số 4, Hà Đô Centrosa Garden, P.12, Q.10, TP. HCM</span>
                <a href="https://drduyhai.com/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/Min-Skinlab-800x400.png">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Mịn Skinlab</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">41 Đặng Thị Nhu , Phường Nguyễn Thái Bình , Quận 1 , TP.Hồ Chí Minh</span>
                <a href="https://www.facebook.com/minskinlab" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/MP.png">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">PKQT Minh Phúc - Ms Như Hương</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">74 Bắc Hải, P.6, Q.Tân Bình, Tp.HCM.</span>
                <a href="http://phongkhamminhphuc.com/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/PKDL-Ts.Bs_.Mai-Phi-Long-267x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">PKDL Ts.Bs.Mai Phi Long</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">124 Hồ Bá Kiện Q10</span>
                <a href="http://maiphilong.com/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/iskin-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Iskin Aesthetic Clinic Spa</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">271 Nguyễn Đình Chiểu, Phường 5, Quận 3, Tp.HCM.</span>
                <a href="https://www.facebook.com/iskinaestheticclinicandspa/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/bsvinh1-365x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">PKDL Bs Ngô Minh Vinh</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">419/1 Đ.Cách Mạng Tháng 8, P.13, Q.10, Tp.Hồ Chí Minh.</span>
                <a href="http://www.bacsivinh.com.vn/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/Libeauty-800x305.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Libeauty Spa</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">Số 2 Bát Nàn, Thạnh Mỹ Lợi, Q.2, Tp.HCM.</span>
                <a href="https://www.instagram.com/libeauti.ru/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/Chu-medi-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Chuu Medi Spa - Ms Phượng</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">71 Thống Nhất, Bình Thọ, Thủ Đức</span>
                <a href="https://www.facebook.com/chuumedi.spa/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/em-may-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Em Mây Skincenter</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">Em Mây Clinic 1: 26 Tăng Bạt Hổ, Phường 12, Quận 5, HCMC. Em Mây Clinic 2: 219 Nguyễn Đình Chính, Phường 11, Phú Nhuận, HCMC. Em Mây Clinic 3: 168, 3 Tháng 2, Phường 12, Quận 10, HCMC</span>
                <a href="https://www.facebook.com/emmayskincenter" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/360126325_948833206208350_7261734181740933013_n-387x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">PKDL Bs Nay Mai Sương</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">19A1 Đ. Số 25, Hiệp Bình Chánh, Thủ Đức, Hồ Chí Minh</span>
                <a href="https://www.facebook.com/p/Ph%C3%B2ng-Kh%C3%A1m-Da-Li%E1%BB%85u-Th%E1%BA%A9m-M%E1%BB%B9-B%C3%A1c-S%C4%A9-CKII-NAY-MAI-S%C6%AF%C6%A0NG-100032450392298/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/ktyna-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Ktyna Beauty Center - Bs Nguyễn Vũ Ty Na</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">TK 14/6 Võ Văn Kiệt, phường Cầu Kho, quận 1, Ho Chi Minh</span>
                <a href="https://www.facebook.com/NguyenVuTyNaMD/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/hms-476x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">HMS Beauty</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">CS 2: 107 Nguyễn cửu vân, P.17, Quận Bình Thạnh, Tp.HCM.</span>
                <a href="https://www.facebook.com/people/HMS-Beauty-Tp-H%E1%BB%93-Ch%C3%AD-Minh/61557215954020/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/shin-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Shin Cosmeceuticals</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">220/74 Hoàng Hoa Thám, Phường 5, Q.Bình Thạnh, Tp.HCM.</span>
                <a href="https://www.facebook.com/ShinCosmeceuticalsmall/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/hhv-553x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">HHV Beauty Clinic</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">652/12 Cộng Hòa, Phường 13, Q.Tân Bình, Tp.HCM</span>
                <a href="https://hhvclinic.vn/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/shynh-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Shynh Group</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">79 Nguyễn Trãi, Quận 1, Tp.HCM</span>
                <a href="https://shynhgroup.vn/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/473073329_626451743067296_4200667796363239512_n-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Carina Beauty Clinic - Bs Tuấn anh</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">số 9 đường B4, Khu đô thị Sala, Q.2, Tp.HCM.</span>
                <a href="https://www.facebook.com/carinatherealluxury/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/keji-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Kefi Skinlab - Ms Ngọc Hà</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">58 Phước Hưng, Q.5, Tp.HCM</span>
                <a href="https://www.facebook.com/KefiSkinlab/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/trang-skinlab-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">Ms Thu Trang - Trang Skinlab</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">50/13 Dân Chủ, KP3, Bình Thọ, TP.Thủ Đức</span>
                <a href="https://www.facebook.com/Trangskinlabb/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/emcas-400x400.png">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">BV TM Emcas - bs Như</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">14/27 Hoàng Dư Khương, phường 12, Quận 10, TPHCM</span>
                <a href="https://www.facebook.com/EMCAS.Hospital/?locale=vi_VN" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
        <div class="flex gap-2 ">
            <div class="pt-2 ">
                <img class="min-w-[50px] max-w-[50px] h-auto " src="/upload/kvmn/wedo-clinic-400x400.jpg">
            </div>
            <div class="flex flex-col gap-1">
                <span class="uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb ">PK Wedo - Bs Quỳnh Trang</span>
                <span class="uppercase font-medium text-[13px] text-[#11284A] ">11 Trần Doãn Khanh, Đa Kao, Quận 1</span>
                <a href="https://wedoskinclinic.com/" class=" uppercase flex justify-center items-center w-[110px] font-medium text-[12px] lg:text-[16px] text-white bg-[#11284A] rounded-full py-1">Xem thêm</a>
            </div>
        </div>
    </div>
"""

# Tạo đối tượng BeautifulSoup để phân tích HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Tạo danh sách chứa thông tin các phòng khám
clinics = []

# Tìm tất cả các phần tử chứa thông tin phòng khám
for clinic in soup.find_all('div', class_='flex gap-2'):
    # Tìm tên phòng khám
    name = clinic.find('span', class_='uppercase font-medium text-[18px] lg:text-[25px] text-[#11284A] ff-bb').text.strip()
    
    # Tìm địa chỉ phòng khám
    address = clinic.find('span', class_='uppercase font-medium text-[13px] text-[#11284A]').text.strip()
    
    # Tìm link ảnh
    img_url = clinic.find('img')['src']
    
    # Tìm link thẻ a
    link = clinic.find('a')['href']
    
    # Lưu thông tin phòng khám vào danh sách
    clinics.append({
        'name': name,
        'address': address,
        'img_url': img_url,
        'link': link
    })

# Chuyển đổi danh sách phòng khám thành chuỗi JSON
clinics_json = json.dumps(clinics, ensure_ascii=False, indent=4)

# Lưu dữ liệu JSON vào file
with open('clinics_data.json', 'w', encoding='utf-8') as f:
    f.write(clinics_json)

print("Dữ liệu đã được lưu vào file 'clinics_data.json'.")
