<template>
  <div class="header-box">
    <div class="header">
      <div class="content">
        <div class="logo">
          <router-link to="/"><img src="../assets/logo.svg" alt=""></router-link>
        </div>
        <ul class="nav">
          <li v-for="item in nav.header_nav_list">
            <a v-if="item.is_http" :href="item.link">{{ item.name }}</a>
            <router-link v-else :to="item.link">{{ item.name }}</router-link>
          </li>
        </ul>
        <div class="search-warp">
          <div class="search-area">
            <input class="search-input" placeholder="请输入关键字..." type="text" autocomplete="off">
            <div class="hotTags">
              <router-link to="/search/?words=Vue" target="_blank" class="">Vue</router-link>
              <router-link to="/search/?words=Python" target="_blank" class="last">Python</router-link>
            </div>
          </div>
          <div class="showhide-search" data-show="no"><img class="imv2-search2" src="../assets/search.svg"/></div>
        </div>


        <div class="login-bar logined-bar" v-if="store.state.user.user_id">
          <div class="shop-cart ">
            <img src="../assets/cart.svg" alt=""/>
            <span><router-link to="/cart">购物车</router-link></span>
          </div>
          <div class="login-box ">
            <router-link to="">我的课堂</router-link>
            <el-dropdown>
                <span class="el-dropdown-link">
                  <el-avatar class="avatar" size="50"
                             src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBERFBcRFBQXFxcYGhkXGBoYFxkbHRgYGRoaGRcjHCEcISwlGh8pKxcaJDUlKC0vMjMyGiM8PTgxPCwxMi8BCwsLDw4PGxERGTwjISExMy86MTExMTw0NzExMTExPDw6LzExMTM1LzExMTIxLzExMS8xMjEvLzExMS8vMS86Mf/AABEIAOEA4QMBIgACEQEDEQH/xAAcAAEAAgMBAQEAAAAAAAAAAAAABgcEBQgDAgH/xABBEAACAQIEBAQDBQUFCQEBAAABAgMAEQQFEiEGMUFRBxMiYTJxgUJScpGhFCNigrFTkqLB0RUkM0Njk7LC0vAX/8QAGgEBAQADAQEAAAAAAAAAAAAAAAEDBAUCBv/EACMRAQACAgICAQUBAAAAAAAAAAABAgMRBDESIUEFEyJRcRT/2gAMAwEAAhEDEQA/ALmpSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSsDNs0gwkRmnkWNF6t1PQAc2J7Degz6VWs3i/gg1lw+IZfvWjF/kC9/ztUu4d4nweYqWw8t2X40YaXT5qenuLj3oN5SlKBSla/G5zhIP+LiIo7dHkRT+RNBsKVT3FnilKspiwGjy02Mrrq8xuugXACDvvfpYWvhTeLWMaDy1ijSe9jKLldPcIb2b5kj26UF3UrnWPjDOoSmJaebS59JlT91JbchQVCkfgt86vDhTOhj8JHitGguCGXnZlZkax6rdTY9qDdUqp/ETxCmglfB4MhDHYSykAkMQDpQNsLAi7EH2ta9RH/aHEKgTa8fpO+opKV+ekqQB9LUHQtKoDDeKWaRjQ0kLkbEyRDV9dDKP0r9i8U811hvMiYfc8tdJtz5HV/ioul/0qMcK8X4fHwCYssTg6ZEdwNL+xNtQPMH/ADBqSqwO4NxRH1SlKBSo3xZxdhssQGUlpHv5cS21Nbmd9lX3P0udqr2TxhxF/Tg4wvQGRybfMKP6UFzUquuHfFTC4h1ixEZw7sQAxYPGWPIFrAr8yLe9WLQKUpQKUpQKUpQYmOxkcEbzSNpRFLseyqLn51z/AJrmONz/ABioik3JEUV/TFH1Zj0PVm+g6CrO8YsQyZcVXlJLGjfhGqT+qLWr8E8FGIJ8RYGRpfLv1CIisB9S5P0HaisrB+EuAWLRLJK8hG7q+gA/wLYi34tVV5nmUYvIsYjo/Il4ZALCRftK4/RlvuCD1Fuiq03EeQwZhCcPMptzVhsyOOTKeh3+RBINEeHCvE+HzKESRsBIAPMjJGqNuu3Vezcj+lbyRwoLEgAC5J2AA53qic08M8zw73w4E639DxyLG4B7h2Gk/hY1IePc2xWCyzDYCZi088ZWaS9/RHp8xdX2mbWqk9Rq7ig0XGPH2Jx0pw2DZ0hLaE8u4knN7XuPUFPRRzHO97D4y/wrzKYB38mHVuQ7ln37hFIv/NUk8H+GQqHMZV9T3SC/2U5O492NwD2G2zValFV3wl4ZQ4STz8S6zuL6E0WjW4sSQxOtu17AX5XsRuB4d5SJfO/ZRe99Ot/Lv+DVpt7Wt7VLaURg5hlkGJTyZokkTY6XUEAjlbsR7V74bDxxKscaBEUBVVQAFA5AAchXvSgj+K4QwEuKGNeAGYEHVqaxZfhZlvpZhYWJHQdhUgpSgxpsFDIbvGjHuyKT+orAzzIoMZh2wroAjD0lQAY2HwsvYj/UHYmtxSgobEeFGZByq+Q6i+l9ZXUOmxUlSe249zWBkmf5hkeIMLq4VSPMw7n0lT9qM8lPZl2PW/ToeotxzwpHmUNtlmQExSdj1Vu6N17bHpRdtvlmdYfE4cYuN18oqWLMQujT8Qe/wlbG9+VqjeceJeWYdT5chne2yxAkH5uRpA+pPsaqnhvEyRSyZVNrWPFMMPKgHqimLBEcDkSG0gjky/IVNsB4OoGvPi2db/DHGEJHuzM39KIheDw+Kz/MCWNjIQ0jDdYYV2AW/YbAdWJPerkw3AeVRoE/ZImsLanXU59yx3vWzyTI8NgY/Kw8YjXmbbs5ta7Md2PzraUFF+KPB+HwHlTYdSsUhaN0LMwVwNS6SxJAIDbX+ztVj+GuaHFZdCzHU8d4nJNzdDZCfcroP1r68RsvTEZdiNXOJDMh7PEC36i4+RqD+CGKYS4mG/pZEkt2ZWKk/UMP7ooq46UpRClKUClKUEP8UoFfLJy32PLdfZhIoH53I+tRbwOma2Lj+yDEw/EQ6n9FX8qnXG2WPi8BiIEF3ZLoO7IwdR9SoH1qnfDjiyPLZpFmU+XLpV2HxRMhYXI5lfUbjmLcjRXQNK80cMAQbgi4I6g8q9KIVr80yfDYtQmIhSVVN1DqDY8tu1bClB5RRqihFUKqgAACwAGwAA5CvWlKBSlY2OxccEbTSMFRAWZjyAG5oMmlabh/iLCZijSYWTWqtpb0spU8xcMAd+9aPxH4ukyyOMQxq0kpYKzglECadVwCLsdQsLjqd7WITWlVPwJ4jYvFYpMJiUjYS6gjxqVZWVWf1C5DLZT2I96srNMwiwsTzzOEjQamY32HLkNyeQAG5JoM6larIc9wuYR+dhpPMQMVOxUhhY2IYAjmK2tApSlBrGyTCNOMWYIzOOUmkaxtYb97bX52rZ0pQKUpQafiqIvgcUg5mCYD5+W1qqfwVlAxsq/ega30kj/1qa+JfFkeEw8mGRgcRKhQKDvGjixdu219I6n2BqMeCuUOZJsaRZFXyUP3mJDSW9hpUfze1FXFSlKIUpSgUpSgVTPjPkscUkOLjRV8zWkhUW1SABkJtzJAff8Ahq5q1ud5PDjYWw8y6kbtsVI+EqejDvQRTw74twkuEhw7zok0aCIpIwVmCbIV1W13UA7Xtvepp+2w/wBon99f9ap3NvCHFKT+zzRSJ0EmpGA97BlY++3yrVf/AMozT+yg/wC4P/mir/Br9rRcIZVLgsHDhpX8x41IJF7C7Fgq330qCFHsOnKt0rA7g3HtRH3SlKBWuzvLI8ZBJhZL6ZVKkjYjqCL9QQD9K2NabivATYnBzwQvokkjKob2ueeknoGsVJ7NQa/gjhHD5XG6xO0hkYMztp303CgBdgBc/UmtN4x4uJMCImCl5ZVEdwCV0HW7DtsNJP8A1PeqxyTiTMcnaTDoBGSbvFMhOlhtqUAi1+4NjYc68cViMdm84kkYu1tN7aY4l7ADYd+596kzEdvVaTadRG018Ekw5bEM2kzjSFBHqEW+orfoSQDbst+YqzOIcnix+HfCy3CSAXKmxBUhlIv2IBqgcfw/isI4mhZyE9SyRkq6bb/CbjruOlDxFm2NU4bz55g4sY0UEsvW+hdRXvfbfepW0WjcPWTHak6tGl28FcLQZXC0UTtJrfWztbc2CgDTsALfqak1QfwtyDE4HCsuI9JkfWsVwfLXSBvbYM1rkD263qcV6YyleUsyLuzKvzIH9a8ocfC5skqMeyup/oaDKqrfEzi7MsDiY4oLRxFAwcxhvMcltQuwt6QBsN979qtKtTxHk8eOw0mGkAIdTpNvhcfAw7EG1BTi+K+aKN/2c+5ib/KQCsPE+ImbYo+Ukukn7OHj9R+XxP8Aka+vDDExR44RzrHokjdG80KQroNYPq2B9LD61dUGdZah0JicKp7LLEP0BoqouGvDfG4xxNiw8MZOpzIf30n0NypPVn3HY1dWW4CPDRrDEoSNBpVR0H+ZPMk7kk1kRyKwDKQQeRBuDXpRClKUClKUClKUClKUClKUFM+KnGErytl0DFY0sJmUm7sRfRcfZFxcDmSRyG8t8LcixOCwrDEekyOJEivfy10gb9FY8yo5WHW9VUjphs4Z8SPRHjJHe4vsZGZWt1G6v8q6CwGPhxCCWGRJEPJkYMtxzFx19qKzKUpRClKUEJ8VcpOIy93VbvCVlG2+lbiS38rMfpVYcDY8DXh2NrnWnubAMP0B/OugZFBBBAIOxB5EHnVJ8W+GuKgkaXBKZYidSorASRdbWJGpR0IN+hG1z4vXyrpmwZZxXi0fD04qx4hw7rf1yAxqOtjsx+gv9SKzPBLKyXnxhGwUQoe5JDyf0j/Oo3lvAebYyQCSN415NLOfhHWyk62PYAAe451csEWFyfAm3pigQsxNtTHmSe7MT+ZFTHTwjT3yuR963lrUQ++JuJcLlsXnYh7XuEQbvIw6KP8AM2AvuapLiDxOzLGuY8OTh4zsqxXMjD3f4r8/g08+vOtLjcXi88xpdjYtyFyVhjHQewv9SferCyfJYMImmNfVb1Od2b5nt7Dal8kU/r1xuJbN76j9q7XhbMsSfMkVrn7Ur7/W5LV9y8DY5BqARiOivv8A4gKtKla/+izox9Nxa7lXOT8ZZtlLhHZ2Qc4p9TKV/hJ3X5qbexqd5z4xQ/sqNhUP7S9wySA6YbcySLeZf7NvmbW0n8zTLYsUhjkW4PI9UPQqehqv8DwXiDiRHIv7pWOpwRYqO29xfb5XrPTLFo9+mln4N6WiK+4lr8DleNx+p1QEMxZnayKWJubdOfRRWxPAGLtfXET21N/81ZMUaooRVCqosABYADlavqsM57b9N2n03HEflO5VXEc1yhvMjeWIX5odUbfiG6n5MKtvgDxLjx7LhsSFixB2UjZJT2F/hb2PPoelY7oGBVgCDsQRcEe9Vvxjw5+ykYmC4QsLgf8ALboQeinp2P0rJjzeXqe2nyuDOKPKs7h0zSoN4XcVnMsLpka88JCSHq6keh/rYg+6nuKnNZ3PKUpQKUpQKUpQKUpQVJ40ZPAqx45VIleQRSEcmURuykj7w0AX7bHkLbLwVwwXByy6rl5iNN9l0IoG3c3/AC01JuOsiOYYKSFf+ILSR329abge2oXX+aoB4NtjIsRPhnjdYtOqTWjLolUqq2v1YXBH8A7bhcVKUoFKUoFKV5TSoilnYKo5liAB8yaD1qrPHbMzHhIsMpt50hZvdIgDb+8yn6VMZONcqVtJxsFxztICPzG1VN4wZvhsfNAMPMsixo+pluQGdhYA8jsvSg/fD3ACPDebb1SsTf8AhQlQPzDH6ipVUT4Z4hgEceGe8bKoUM1tLH5/ZPz/ADqWVoZYnymZfScSafbrFZ6gpSlY20UpSgUpSgV447CrNG8T8nUqfryP051F864u0Ex4cA22Mjbj+UdfmdvY860y5pmhXzgZynPWIj5f56NNqzVw2n305+bnYo3XtmeEWPbDZosJ5SiSFxfa6guDbvdAPqa6KrmLhIgZnhZ3cLedGdjYC7Nv7AEm31rp2t1wp7KUpRH7SlKBSlKBSlKBSqu4+8R3wspwuE0F4z+9kcalVvuKLi5HUnly53tOOFsxlxWEhnmTRJIgZlsQL3IBAO4DABgD0NBuaUpQKUpQUtxumex42SWI4sxEjyjB5jIEsNikd9Jve5YXJrQLw7nmZMPMjxD/AMWJZo1X3Akt/hU10RSgpeDwexRUF8VEjdVWN3A/mLLf8q2uS+EUcbh8ViPNUG/lohjDfiYsSR7C3zq0qUNqi4u8LLBp8ASbXJgY3/7TH/xb8xyqJ8J548ci4aUnQx0Lq2Mb8gpvva+1jyP1roDHYyLDxvNKwREBZmPIAVznNif27MmmjQqJJ/MA+6gYMSexspJ9zXjJWJrO2fj5LVyR4rGpSlc99MUpSilRvjXMjFGIUNmlvcjpGOf53t8r1JKrnjeQtimH3URR9Rq/9qy4a7u0+bkmmKdfPpNfCzgqOZBmGJUOtyIY2F1Ok2LsDz3BCjltffa1v6Ra3SsXK8KsEMUKCyxoiL8lUAf0r8zPMIsNE88raURSzH5dB3J5AdSa3nzqhvFXBw4fHusKhAY0kYJsFkbVqsByJAVvmb9avzL2Zooy3xFFLfiKi9c/5ZFLnWahnG0svmSD7kMdtv7oVL92HeuiKK+qUpRClKUClKUCtBxpnJwODmxC21hdMd9/3jkKm3UAnUfYGt/XPnHeMmzDM3w6tqAlXDwoSdKtcRk9hdixLW5fKgyPC7hpcdimnmGuOGzsG38yViSoa/MCxY9zbuavqo3wPw2MtwwgLB3Zi8rLyLkAWF97AADfna+17VJaBSlKBSlKBSlKBWuzjN4MHE087hEXvzY9Ao5sx6AVoeMOOsNlt4/+LiLXESn4b8jI32B7bk9B1qoiczz/ABPWRh81hgU/np/Vm97bB6cYcXYjNpBGiOsKkmOFQWZrAnU4W+prAmwuFHLqTreDs9gglYSLp12CyfdHYjopPUe19uV4cH8G4fLUuv7yZhZ5WG57hB9hfbr1JqLcfeF6YkvisEFSY3Z4tgkp6lSdo2P90nnbc15tWLRqWTHkml4tHw+1YEAggg7gjqKVVmX53jMsdsPKjWU2aKQEFfwn7PfqDU+ybiDDYseh7P1jbZh8vvD3Fal8Vq/x3cHMpl9dT+m1pSlYW6VD+NsnZ/8AeUFwFtKOwW9m9x0PyFSbMMwiwyGSVgq9O7Hso5k1W+dZ9iMykXDwo2lmASNN2c9NVuZ625D9az4a28tw5/Oy4/CaT2kOU+JeZYaNYtUUqqLKZUYsANgNSMt/mbn3rFx+eZpnkqw2MliCIoVKxqfvNcm34nbbpa9T3gHwziwqedjUWWZhtG1njiB6b7O/c8hyHc2NhcJFCumNEReyKFH5CtxwkZ4C4QXLITqIeeSxlccgB8KJ10i536kk9gJdSlEKUpQKVg5vj1w0EuIYXWJHkIHUKpNv0rn/APbs3zeZ2jaaRgNZSOQokS32CjUqjsPtG3Xeg6NryeZFIUsATyBIBNc+QcV5zlpaB5ZVJBGjEKXK321IZPVt0sSvcGsXLOFMwzNJMWiebYm7yP6pW66C/wAZHzA6cxaiuicdi0gjeZzZI0Z2PZVBJ/pVDeHOHfF5rHKw3DS4mTrvv/7yLWrm4hx8MEuWyyOIyVV45b649LBtKlt1BsAV3FuQF97L8F8n8vDyYxh6pm0If+nHcX+rFv7ooLMpSlEKUpQKUpQKUpQV5nvhnDjMY2Lad1RyGeNVGosFC+lyfSCFH2T1tU0ynK4MJGsMEaxovQdT1LHmzHud6z6UClKUGj4j4WweYpoxEYYgWVxs6fhbn9Dce1UxxR4U43CEy4QnERjcBdpUt/D9u2267+wroOlBzDlvGOLwx8qYGQKdJV7q622tfnf8QNbnG8fwhLwxsZD0ewVfnY+r6Wq6c+4WwOPFsTAjt0celx2sy2a3te1Q/B+DeXRy+Y0k0iA3EbFQD7MygEj5WrHOOszvTZpy8ta+MSq3JsjzHPJiVuVBs8r7JGOdh7/wrvuL96vPg7gnCZWv7tdcxFnmYDUb8wv3F9h2FyakWEwscKLFGioiiyqihVA9gOVZFZOmvMzM7l+0pSiFKUoFKUoMHNsAmJglw7/DKjISOgYEXHyvXP2ExWOyHGMCtpFGllYHy5or7Ed1NrhhuDseoro+tbnGS4bGp5WIiWReYuN1PdWG6n3BoITB4kZPi4wuLjKEc0lhMq3/AISitt8wD7Vust48yeS0ceJjjAFgHR4VA9i6qv0vUfxnhBhWa8WJmjH3WCyAfI7H8yag/HfCUWVtEi4gyNIGJUoFKqtgDcE7Em1vY9qKsGLjrKMVjFg/Zy5kIiE7xR6WJNlHqOvSTYAkc7bW3qwY41UBVAAAsABYADsByqrvCzg2ExR5jMpaQsWhUkhUVSVDW+0xIJBPIabb71atEKUpQKUryllVAXZgqgEkkgAAcySeQoPWlQDGeK2WxyeWomkUGxkjRdH01MCw9wK3y8YZaYBiv2qMRsdIJNm1Wvp0/Fq9rXoJDStPlHEmCxlxh8RHIRzUGzD+VrNb3tW4oFKUoFKUoFY2OMgjcxgGTQ2gHkXsdN/a9qyaUFJcF8a5hHjUwuMkd1lk8p1kUBopGOlbWAt6rKV5WO3KrsrnzjjB4jL8zOJK31TDEQuQdLWYOAfdSLEc7WPUVb3BPFUeZwtIEKSIQsiXuASLgqeqne3yNFSalKUQpSlApSlApSlApSlB+VznKXzvNLaiBNIVVh/y4EuRa/KyLftqb3roDNCwglK/F5b2+ek2qj/BsL/tFb/2Emj8V4+XvbV+tFXpgcIkMaQoNKRqqIOyqAB/SsmlfDOBzIHzoj7pXyDetNxDxLhMuVGxDldZIQKrMzWtqNlBNhcXPuO9BscdjI4I2llcIiglmJsAB/8AuVUTxjxhiM2lGGgVxCWCxxKPXK3QuBz7heQ5ncXG98UpsbjZMOmGSWXCSRrLGYkZleRiw9ZA2IGmwa1tR+ks8P8AglMuTzpQHxTj1NzEan7Cf5t1+VqCNZR4RBoCcTMyTMLqsekpF7NcfvD3sQO1+daMeFOZ+bo/c6L283Xtp76bar+369avelDaic48LMwgbVAUxCjcFSI5AfwsbfUNWvbKuIYfVpx6239Esjfojm9dD0oKJyHxNx+Gfy8VeeMGzB1CSp8iALkdnFz3FXNlOZw4uJJ4XDxuNj1B6gjmGHIg1ouN+D4MyiYhVTEKLxycrkclY9UPL2vce9W+H3Ej5Zi2w890ikfy5lb/AJUgOkP2FiNLe2/2aKv+lflftEKUpQQ7xS0f7MnLKDYxabgGzGWNQRfkfUf1qK+BqH/fG6fuR9R5pP8AUU8ZuILBMtUHfRNIx5aQWEaj6rqJ/hHc23/hJk74bA+a6lXnfzbHmI7BY/lcAt/NRU8pSlEKUpQKUpQKUpQKUpQfhFc98S5LicjxgnhusYcth5LXWxv6G9wCVIPxDcdbdC14YrDRzI0ciK6MLMrqGVh7g7Ggh/BnGUmZwT6YgmIhUbA3R2dX8si+4uUNweXc1UWCyLMs2mcFJJJUuZGnJXQSfhOv4T2QcgOVhXQmV5ThsIpjw8SRKTqIQAXPc9+1bCg5vRs1ySRlXzIDyPp1QuD1FwUb5jccu4r3wuV5rnc4d9b8lM0i6Y40ufhsAD19K7k8+9dEUoMHKMvjwsEeHjvpiUIL8zYcz7nn9az6UoFKUoFKUoFVL4ucJEk5lCt9gMQoHQCyyfQCzewB6Grar8oKr8LeNJJimXTKXKRsY5AbnQlvS462BsG62AO+58X8Y/U2nB3S/pJlsxHQkaLA+1zVjZfkODwztLDh443f4mRApIvcjbkCd7CtbjeBMqmYu+ETUxJJQvHcncn0MN6CEv4yN9nBD6z2/pHU/wCEOIFzLDLiQhjJLKyE3symxsbC45G9uvtWFH4d5QvLCKfxSSt/5OakOCwcUCCKJFRF2VFAVRvc2A+ZP1oMPM8gweKZJJ4EkZPgLrcje9vcX3sbitrX7SgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSg//9k="></el-avatar>
                </span>
              <template #dropdown>
                <el-dropdown-menu>
                  <el-dropdown-item :icon="UserFilled">学习中心</el-dropdown-item>
                  <el-dropdown-item :icon="List">订单列表</el-dropdown-item>
                  <el-dropdown-item :icon="Setting">个人设置</el-dropdown-item>
                  <el-dropdown-item :icon="Position" @click="logout">注销登录</el-dropdown-item>
                </el-dropdown-menu>
              </template>
            </el-dropdown>
          </div>
        </div>

        <div class="login-bar" v-else>
          <div class="shop-cart full-left">
            <img src="../assets/cart.svg" alt=""/>
            <span><router-link to="/cart">购物车</router-link></span>
          </div>
          <div class="login-box full-left">
            <span @click="state.show_login=true">登录</span>
            &nbsp;/&nbsp;
            <router-link to="/register">注册</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
  <el-dialog :width="600" v-model="state.show_login">
    <Login @successhandle="login_success"/>
  </el-dialog>
</template>


<script setup>
import nav from "../api/nav.js"
import {reactive} from "vue";
import Login from "./Login.vue";
import Register from "../views/Register.vue";
import {UserFilled, List, Setting, Position} from '@element-plus/icons-vue';
import {useStore} from "vuex";

const store = useStore();

const state = reactive({
  show_login: false,
})


// 请求头部导航
nav.get_header_nav().then(response => {
  // console.log(response.data);
  nav.header_nav_list = response.data;
})

// 用户登陆成功后的处理
const login_success = () => {
  state.show_login = false;
}

// 登录注销的处理
const logout = () => {
  store.commit("logout");
}

</script>


<style scoped>

.header-box {
  height: 72px;
}

.header {
  width: 90%;
  height: 72px;
  box-shadow: 0 0.5px 0.5px 0 #c9c9c9;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  margin: auto;
  z-index: 99;
  background: #fff;
}

.header .content {
  max-width: 1366px;
  width: 100%;
  margin: 0 auto;
}

.header .content .logo a {
}

.header .content .logo {
  height: 72px;
  line-height: 72px;
  margin: 0 20px;
  float: left;
  cursor: pointer; /* 设置光标的形状为爪子 */
}

.header .content .logo img {
  vertical-align: middle;
  width: 240px;
  margin: -40px;
}

.header .nav li {
  float: left;
  height: 80px;
  line-height: 80px;
  margin-right: 30px;
  font-size: 16px;
  color: #4a4a4a;
  cursor: pointer;
}

.header .nav li span {
  padding-bottom: 16px;
  padding-left: 5px;
  padding-right: 5px;
}

.header .nav li span a {
  display: inline-block;
}

.header .nav li .this {
  color: #4a4a4a;
  border-bottom: 4px solid #ffc210;
}

.header .nav li:hover span {
  color: #000;
}

/*首页导航全局搜索*/
.search-warp {
  position: relative;
  float: left;
  margin-left: 24px;
}

.search-warp .showhide-search {
  width: 20px;
  height: 24px;
  text-align: right;
  position: absolute;
  display: inline-block;
  right: 0;
  bottom: 24px;
  padding: 0 8px;
  border-radius: 18px;
}

.search-warp .showhide-search i {
  display: block;
  height: 24px;
  color: #545C63;
  cursor: pointer;
  font-size: 18px;
  line-height: 24px;
  width: 20px;
}

.search-area {
  float: right;
  position: relative;
  height: 40px;
  padding-right: 36px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.4);
  zoom: 1;
  background: #F3F5F6;
  border-radius: 4px;
  margin: 16px 0;
  width: 324px;
  box-sizing: border-box;
  font-size: 0;
  -webkit-transition: width 0.3s;
  -moz-transition: width 0.3s;
  transition: width 0.3s;
}

.search-area .search-input {
  padding: 8px 12px;
  font-size: 14px;
  color: #9199A1;
  line-height: 24px;
  height: 40px;
  width: 100%;
  float: left;
  border: 0;
  -webkit-transition: background-color 0.3s;
  -moz-transition: background-color 0.3s;
  transition: background-color 0.3s;
  background-color: transparent;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  -ms-box-sizing: border-box;
  box-sizing: border-box;
}

.search-area .search-input.w100 {
  width: 100%;
}

.search-area .hotTags {
  display: inline-block;
  position: absolute;
  top: 0;
  right: 32px;
}

.search-area .hotTags a {
  display: inline-block;
  padding: 4px 8px;
  height: 16px;
  font-size: 14px;
  color: #9199A1;
  line-height: 16px;
  margin-top: 8px;
  max-width: 60px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.search-area .hotTags a:hover {
  color: #F21F1F;
}

.search-area input::-webkit-input-placeholder {
  color: #A6A6A6;
}

.search-area input::-moz-placeholder {
  /* Mozilla Firefox 19+ */
  color: #A6A6A6;
}

.search-area input:-moz-placeholder {
  /* Mozilla Firefox 4 to 18 */
  color: #A6A6A6;
}

.search-area input:-ms-input-placeholder {
  /* Internet Explorer 10-11 */
  color: #A6A6A6;
}

.search-area .btn_search {
  float: left;
  cursor: pointer;
  width: 30px;
  height: 38px;
  text-align: center;
  -webkit-transition: background-color 0.3s;
  -moz-transition: background-color 0.3s;
  transition: background-color 0.3s;
}

.search-area .search-area-result {
  position: absolute;
  left: 0;
  top: 57px;
  width: 300px;
  margin-bottom: 20px;
  border-top: none;
  background-color: #fff;
  box-shadow: 0 8px 16px 0 rgba(7, 17, 27, 0.2);
  font-size: 12px;
  overflow: hidden;
  display: none;
  z-index: 800;
  border-bottom-right-radius: 8px;
  border-bottom-left-radius: 8px;
}

.search-area .search-area-result.hot-hide {
  top: 47px;
}

.search-area .search-area-result.hot-hide .hot {
  display: none;
}

.search-area .search-area-result.hot-hide .history {
  border-top: 0;
}

.search-area .search-area-result h2 {
  font-size: 12px;
  color: #1c1f21;
  line-height: 12px;
  margin-bottom: 8px;
  font-weight: 700;
}

.search-area .search-area-result .hot {
  padding: 12px 0 8px 12px;
  box-sizing: border-box;
}

.search-area .search-area-result .hot .hot-item {
  background: rgba(84, 92, 99, 0.1);
  border-radius: 12px;
  padding: 4px 12px;
  line-height: 16px;
  margin-right: 4px;
  margin-bottom: 4px;
  display: inline-block;
  cursor: pointer;
  font-size: 12px;
  color: #545c63;
}

.search-area .search-area-result .history {
  border-top: 1px solid rgba(28, 31, 33, 0.1);
  box-sizing: border-box;
}

.search-area .search-area-result .history li {
  height: 40px;
  line-height: 40px;
  padding: 0 10px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  color: #787d82;
  cursor: pointer;
}

.search-area .search-area-result .history li:hover,
.search-area .search-area-result .history li .light {
  color: #1c1f21;
  background-color: #edf0f2;
}


.header .login-bar {
  margin-top: 20px;
  height: 80px;
  float: right;
}

.header .login-bar .shop-cart {
  float: left;
  margin-right: 20px;
  border-radius: 17px;
  background: #f7f7f7;
  cursor: pointer;
  font-size: 14px;
  height: 28px;
  width: 88px;
  line-height: 32px;
  text-align: center;
}

.header .login-bar .shop-cart:hover {
  background: #f0f0f0;
}

.header .login-bar .shop-cart img {
  width: 15px;
  margin-right: 4px;
  margin-left: 6px;
}

.header .login-bar .shop-cart span {
  margin-right: 6px;
}

.header .login-bar .login-box {
  float: left;
  height: 28px;
  line-height: 30px;
}

.header .login-bar .login-box span {
  color: #4a4a4a;
  cursor: pointer;
}

.header .login-bar .login-box span:hover {
  color: #000000;
}


/* 登陆后状态栏 */
.logined-bar {
  margin-top: 0;
  height: 72px;
  line-height: 72px;
}

.header .logined-bar .shop-cart {
  height: 32px;
  line-height: 32px;
}

.logined-bar .login-box {
  height: 72px;
  line-height: 72px;
  position: relative;
}

.logined-bar .el-avatar {
  float: right;
  width: 50px;
  height: 50px;
  position: absolute;
  top: -10px;
  left: 10px;
  transition: transform .5s ease-in .1s;
}

.logined-bar .el-avatar:hover {
  transform: scale(1.3);
}
</style>
