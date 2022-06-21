function construct_bv(bv)
{
   return ("https://player.bilibili.com/player.html?bvid=" + bv + "&as_wide=1&high_quality=1&danmaku=0");
};
function change_src_by_bv(bv)
{
    document.getElementById("player").src = construct_bv(bv);
}
