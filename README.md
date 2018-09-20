# 2018全国高校大数据应用创新大赛（技能赛）
===
赛题地址哦：http://117.50.29.62/pc/competition_topic.jsp



<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<link rel="shortcut icon" href="http://117.50.29.62:80/images/logo.ico"/>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>竞赛题目</title>
<!-- 
####################################################################
#  版   本：  1.0
#  版权所有： 联创中控（北京）科技有限公司
#  制 作 人： hubin
#  制作日期： 2018年04月09日
#  IPO图编号 competition_topic.jsp 竞赛题目
####################################################################
-->
<link rel="stylesheet" href="http://117.50.29.62:80/css/main.css">
<link rel="stylesheet" href="http://117.50.29.62:80/css/pc.css">
<script type="text/javascript" src="http://117.50.29.62:80/js/jquery-1.11.1.js"></script>
<script type="text/javascript" src="http://117.50.29.62:80/js/dialog.js"></script>
<script type="text/javascript" src="http://117.50.29.62:80/js/main.js"></script>
<script type="text/javascript">
$(function(){
	$(".noticeNav li").click(function(e) {
		var index = $(this).index();
		$(".noticeNav li a").removeClass("active");
		$(this).find("a").addClass("active");
		$(".guideWrap .eventContent").hide().eq(index).show();
		resetFoot();
	});	
	if(uicc.getQueryString("id") == 1){
		$(".noticeNav a").removeClass("active");
		$(".noticeNav li").eq(1).find("a").addClass("active");
		$(".guideWrap .eventContent").hide();
		$(".guideWrap .eventContent").eq(1).show();
	}else if(uicc.getQueryString("id") == 2){
		$(".noticeNav a").removeClass("active");
		$(".noticeNav li").eq(2).find("a").addClass("active");
		$(".guideWrap .eventContent").hide();
		$(".guideWrap .eventContent").eq(2).show();
	}else if(uicc.getQueryString("id") == 3){
		$(".noticeNav a").removeClass("active");
		$(".noticeNav li").eq(3).find("a").addClass("active");
		$(".guideWrap .eventContent").hide();
		$(".guideWrap .eventContent").eq(3).show();
	}
});

function downloadFile(){
	window.open(ctx+"na/news_fileDown.action?nn.fileName=大数据与人工智能创意赛项目策划书模板.docx&nn.fileUrl=aboutFile/originalityProjectCeHuaTemplate.docx");
}
</script>

</head>
<body>





<script type="text/javascript">
	var ctx = "http://117.50.29.62:80/";
	$(function(){
		var belongMenu = $("#belongMenu").val();
		var userType = $("#userType").val();
		if(belongMenu=="index"){
			$(".nav").find("li").eq(0).addClass("active");
		}else if(belongMenu=="saiShiJieShao"){
			$(".nav").find("li").eq(1).addClass("active");
		}else if(belongMenu=="newAndNotice"){
			$(".nav").find("li").eq(2).addClass("active");
		}else if(belongMenu=="classResources"){
			$(".nav").find("li").eq(3).addClass("active");
		}
		if(userType=="1"){
			if(belongMenu=="judgeReviewProjuct"){
				$(".nav").find("li").eq(4).addClass("active");
				$(".searchWrap").find("span").eq(0).html("评审作品");
				$("#searchCon").attr("placeholder","搜索赛队...").focus();
			}
		}else if(userType=="2"){
			if(belongMenu=="baoMingInfo"){
				$(".nav").find("li").eq(4).addClass("active");
			}else if(belongMenu=="uploadProduction"){
				$(".nav").find("li").eq(5).addClass("active");
			}
		}else if(userType=="3"){
			if(belongMenu=="adminTeamManager"){
				$(".nav").find("li").eq(4).addClass("active");
				$(".searchWrap").find("span").eq(0).html("赛队管理");
				$("#searchCon").attr("placeholder","搜索赛队...").focus();
			}else if(belongMenu=="adminNewManager"){
				$(".nav").find("li").eq(2).addClass("active");
				$(".searchWrap").find("span").eq(0).html("赛事新闻");
				$("#searchCon").attr("placeholder","搜索新闻...").focus();
			}else if(belongMenu=="adminNoticeManager"){
				$(".nav").find("li").eq(2).addClass("active");
				$(".searchWrap").find("span").eq(0).html("赛事公告");
				$("#searchCon").attr("placeholder","搜索公告...").focus();
			}else if(belongMenu=="judgeManager"){
				$(".nav").find("li").eq(5).addClass("active");
				var belongSmallMenu = $("#belongSmallMenu").val();
				if(belongSmallMenu=="judgeManager_judge"){
					$(".searchWrap").find("span").eq(0).html("查看评委");
					$("#searchCon").attr("placeholder","搜索评委...").focus();
				}else if(belongSmallMenu=="judgeManager_group"){
					$(".searchWrap").find("span").eq(0).html("查看评委组");
					$("#searchCon").attr("placeholder","搜索评委组...").focus();
				}else if(belongSmallMenu=="judgeManager_arbitration"){
					$(".searchWrap").find("span").eq(0).html("查看仲裁");
					$("#searchCon").attr("placeholder","搜索仲裁...").focus();
				}
			}else if(belongMenu=="arbitrationAndAdminReviewProjuct"){
				$(".nav").find("li").eq(6).addClass("active");
				$(".searchWrap").find("span").eq(0).html("作品管理");
				$("#searchCon").attr("placeholder","搜索赛队...").focus();
			}
		}else if(userType=="4"){
			if(belongMenu=="arbitrationAndAdminReviewProjuct"){
				$(".nav").find("li").eq(4).addClass("active");
				$(".searchWrap").find("span").eq(0).html("查看作品");
				$("#searchCon").attr("placeholder","搜索赛队...").focus();
			}
		}

		//发送ajax查询当前用户有多少未读消息
		var checkUnReadMessageOpt = {
			url:ctx+"mm/messageAction_showUnReadMessage.action",
			dataType:"text",
			type:"post",
			success:function(result){
				if(result!="noLogin"){
					if(result>99){
						result = "99+"
					}else if(result=="0"){
						result = "";
					}
					$(".SMhead .mess").find("b").html(result);
				}
			},
			error:function(){
				uicc.Ualert({font:"获取未读信息条数失败"});
			}
		};
		$.ajax(checkUnReadMessageOpt);
	});
	
	//搜索框搜索
	function checkXiangGuanInfo(){
		var biaoQian = $(".searchWrap").find("span").eq(0).text();
		var inputVal = $("#searchCon").val();
		var url = "";
		if(biaoQian=="赛事公告"){
			url = ctx + "na/announcement_findNaAnnouncementList.action?na.condition=list&na.title="+inputVal;
		}else if(biaoQian=="赛事新闻"){
			url = ctx + "na/news_findNaNewsList.action?nn.condition=list&nn.title="+inputVal;
		}else if(biaoQian=="赛队管理"){
			url = ctx+"ud/udUserAction_teamManagerIndex.action?pageView.pageNow=1&pageView.pageSize=12&udUserVB.hasApproved=-1&udUserVB.district=all";
			if(inputVal){
				url += "&udUserVB.userName="+inputVal;
			}
		}else if(biaoQian=="查看评委"){
			url = ctx+"ud/udUserAction_showAllPingWeiOrZhongCai.action?pageView.pageNow=1&pageView.pageSize=12&udUserVB.userType=1";
			if(inputVal){
				url += "&udUserVB.userName="+inputVal;
			}
		}else if(biaoQian=="查看仲裁"){
			url = ctx+"ud/udUserAction_showAllPingWeiOrZhongCai.action?pageView.pageNow=1&pageView.pageSize=12&udUserVB.userType=4";
			if(inputVal){
				url += "&udUserVB.userName="+inputVal;
			}
		}else if(biaoQian=="查看评委组"){
			url = ctx+"ud/udUserAction_showAllPingWeiGroup.action?pageView.pageNow=1&pageView.pageSize=12&udJudgeGroupVB.competitionItemId=-1&udJudgeGroupVB.phase=-1";
			if(inputVal){
				url += "&udJudgeGroupVB.groupName="+inputVal;
			}
		}else if(biaoQian=="评审作品"){
			var phase = $("#phase").val();
			url = ctx+"cp/cpProductionAction_showImJudgeGroupTeamList.action?reviewProductionVB.phase="+phase+"&reviewProductionVB.reviewStatus=all";
			if(inputVal){
				url += "&reviewProductionVB.teamName="+inputVal;
			}
		}else if(biaoQian=="查看作品"){
			var phase = $("#phase").val();
			url = ctx+"cp/cpProductionAction_showImArbitrationGroupTeamList.action?reviewProductionVB.phase="+phase+"&reviewProductionVB.district=all&reviewProductionVB.competitionItemId=all";
			if(inputVal){
				url += "&reviewProductionVB.teamName="+inputVal;
			}
		}else if(biaoQian=="作品管理"){
			var phase = $("#phase").val();
			url = ctx+"cp/cpProductionAction_showTeamByAdminHandle.action?reviewProductionVB.phase="+phase+"&reviewProductionVB.district=all&reviewProductionVB.competitionItemId=all";
			if(inputVal){
				url += "&reviewProductionVB.teamName="+inputVal;
			}
		}
		window.location.href = url;
	}
</script>
<script type="text/javascript" src="http://117.50.29.62:80/js/bgWebSocket.js"></script>
<input type="hidden" id="userType" value=""/>
<div class="SMhead">
	<div class="w1200">
    	<h1><a href="javascript:;"><img src="http://117.50.29.62:80/images/logo.png" alt=""/></a></h1>
        
        <ul class="nav">
          <li><a href="http://117.50.29.62:80/pc/index.jsp">首页</a></li>
          <li>
          	<a href="javascript:;">赛事介绍</a>
          	<div class="userMenu">
               <a href="http://117.50.29.62:80/pc/competition_notification.jsp">竞赛通知</a>
               <a href="http://117.50.29.62:80/pc/competition_organization.jsp">竞赛组织</a>
               <a href="http://117.50.29.62:80/pc/competition_guide.jsp">参赛指南</a>
               <a href="http://117.50.29.62:80/pc/competition_topic.jsp">竞赛题目</a>
               <a href="http://117.50.29.62:80/na/naCommonProblemAction_showAllCommonProblemListInUser.action?naCommonProblemVB.channelId=-1">常见问题</a>
               
            </div>
          </li>
          <li>
          	<a href="javascript:;">新闻公告</a>
          	<div class="userMenu">
               <a href="http://117.50.29.62:80/na/announcement_findNaAnnouncementList.action?na.condition=pl">赛事公告</a>
               <a href="http://117.50.29.62:80/na/news_findNaNewsList.action?nn.condition=pl">竞赛新闻</a>
               
            </div>
          </li>
          <!-- <li><a href="http://117.50.29.62:80/ts/resource_findCourseList.action?kw=pl">课程资源</a></li> -->
          
        </ul>
        
		
		    		
	        <div class="member">
	        	<a href="javascript:void(0);" class="login">登录</a>
	        	<!--  
		            <span>|</span>
		        	<a href="http://117.50.29.62:80/pc/signUp.jsp">报名</a>
	        	-->
	        </div>
	        
			
        
        
    </div>
</div>

<!-- login -->
<div class="loginMain smMain" style="display:none;">
    <div class="loginBg"></div>
    <div class="login">
		<div class="form">
            <a href="javascript:;" class="close"></a>
            <h2>用户登录</h2>
            <ul>
            	<li style="margin:18px auto -18px; color:#888; font-size:14px; text-align:center;">本平台账户可直接登录中国工程科技知识中心</li>
                <li class="userName">
                <input id="userName" type="text" placeholder="请输入用户名或手机号...">
                </li>
                <li class="userPass">
                <input id="userPass" type="password" placeholder="请输入密码...">
                </li>
                <li class="worMessage wor"></li>
                <li class="btn"><a href="javascript:;" id="loginBtn">登录</a></li>
                <li style="margin-top:-18px;">
                	<a href="javascript:;" class="forget">忘记密码？</a>
                	<a href="http://117.50.29.62:80/pc/signUp.jsp" class="register">去注册</a>
                </li>
            </ul>
        </div>
    </div>
</div>

<!-- 找回 -->
<div class="forgetMain smMain" style="display:none;">
    <div class="loginBg"></div>
    <div class="login">
		<div class="form">
            <a href="javascript:;" class="close"></a>
            <h2>找回密码</h2>
            <ul>
                <li class="userPhone">
                <input id="userPhone" type="text" placeholder="请输入手机号...">
                </li>
                <li class="userCode">
                <input id="userCode" type="text" placeholder="请输入验证码..."><span id="getCode">获取验证码</span>
                </li>
                <li class="worMessage wor"></li>
                <li class="btn"><a href="javascript:;" id="nextStep">下一步</a></li>
            </ul>
        </div>
    </div>
</div>

<!-- 密码重置 -->
<div class="passwordMain smMain" style="display:none;">
    <div class="loginBg"></div>
    <div class="login">
		<div class="form">
            <a href="javascript:;" class="close"></a>
            <h2>找回密码</h2>
            <ul>
                <li class="userPass">
                <input id="userPassword" type="password" placeholder="请输入6-16位密码...">
                </li>
                <li class="userPass">
                <input id="userPassword2" type="password" placeholder="请再输入一次密码...">
                </li>
                <li class="worMessage wor"></li>
                <li class="btn"><a href="javascript:;" id="success">完成</a></li>
            </ul>
        </div>
    </div>
</div>

<!-- 修改密码 -->
<div class="changePasswd smMain" style="display:none;">
    <div class="loginBg"></div>
    <div class="login">
		<div class="form">
            <a href="javascript:;" class="close"></a>
            <h2>修改密码</h2>
            <ul>
                <li class="userPass">
                <input id="resetPassword" type="password" placeholder="请输入原密码...">
                </li>
                <li class="userPass">
                <input id="resetPassword1" type="password" placeholder="请输入6-16位密码...">
                </li>
                <li class="userPass">
                <input id="resetPassword2" type="password" placeholder="请再输入一次密码...">
                </li>
                <li class="worMessage wor"></li>
                <li class="btn"><a href="javascript:;" id="changePass">完成</a></li>
            </ul>
        </div>
    </div>
</div>


<script type="text/javascript" src="http://117.50.29.62:80/js/index.js"></script>
<script type="text/javascript">
$(function(){
	 //切换搜索
	$(".searchWrap .list").click(function(){
		$(".searchWrap .list ul").slideToggle(120);
		$(".searchWrap .list a").toggleClass("cur");
		return false;
	});
	$(".searchWrap .list").on("click","li",function(){
		$(".searchWrap .list span").text($(this).text());
		$("#searchCon").attr("placeholder","搜索"+$(this).text()+"...").focus();
	});
	$(document).click(function(){
		$(".searchWrap .list ul").slideUp(120);
		$(".searchWrap .list a").removeClass("cur");
	});	
});
</script>


<input type="hidden" id="belongMenu" value="saiShiJieShao"/>
<div class="evenBanner">
	<div>竞赛题目</div>
</div>

<div class="w1200">
	<div class="noticeNav">
    	<ul>
        	<li><a class="active" href="javascript:;">赛项概要</a></li>
        	<li><a href="javascript:;">技术技能赛</a></li>
        	<li><a href="javascript:;">创意赛</a></li>
        	<li><a href="javascript:;">企业命题赛</a></li>
    	</ul>
    </div>
    
    <div class="guideWrap">
    	<div class="eventContent" style="display:block;">
            <p>本竞赛设有大数据技术技能赛、大数据与人工智能创意赛和企业命题赛3类赛项，分预赛、分赛区决赛和全国总决赛三个阶段。以下为赛项规程概要，详细规程见官网通知。</p>
            <p class="bold">（1）大数据技术技能赛</p>
            <div style="margin-left:3em;">
                <p>大数据技术技能赛（简称“技术赛”）重点考察参赛队伍的大数据相关技术掌握水平。</p>
                <p><i></i>预赛阶段，参赛队伍从竞赛官网上下载训练数据集、预赛数据集，根据赛项题目要求，在本地进行环境搭建、算法设计和调试。参赛队伍须在预赛作品提交截止时间前，在竞赛平台队伍管理后台上，按要求和规范提交结果文件。系统自动完成作品评分和排名。</p>
                <p><i></i>分赛区决赛阶段，参赛队伍从竞赛官网上下载决赛数据集，本数据集的规模将远高于预赛数据集。参赛队伍在本地完成算法设计和程序调试，并于分赛区决赛作品提交截止时间前在竞赛平台队伍管理后台上提交结果文件，系统自动完成作品技术部分的评分和排名。各分赛区决赛时间并不一定一致，请各参赛队伍留意本赛区通知。参加分赛区决赛的团队，在决赛现场需要演示作品、展示计算结果并完成答辩。评委会根据作品和答辩对参赛队伍进行综合评价，并评选出获奖队伍。分赛区特等奖、一等奖队伍获得进入全国总决赛的资格。</p>
                <p><i></i>全国总决赛阶段，进入决赛的团队可以继续优化作品，并在规定时间内完成作品提交，系统自动完成作品技术部分的评分和排名。在决赛现场，参赛队伍需要演示作品、展示计算结果并完成答辩。评委会根据作品和答辩对参赛队伍进行综合评价，并评选出获奖队伍。</p>
            </div>
            <p class="bold">（2）大数据与人工智能创意赛</p>
            <div style="margin-left:3em;">
                <p>大数据与人工智能创意赛（简称“创意赛”）重点考察参赛队伍的创造力和应用设计能力，参赛团队围绕大数据和人工智能相关技术和应用场景进行自由创作，并按照模版提交商业模式策划书。专家组将对参赛作品主题和内容进行审核，非原创的、违反赛事精神或章程、具有攻击性质、不符合普适价值观或是与国家有关法律法规相违背的作品将不允许参加竞赛，组委会有权要求参赛队伍进行修改或取消其参赛资格。</p>
                <p><i></i>预赛阶段，参赛队伍从竞赛官网下载策划书模版，并通过策划书提交作品创意。评委会通过竞赛平台在线评分，并遴选出进入分赛区决赛的参赛队伍。分赛区决赛前，参赛队伍可继续完善创意设计。</p>
                <p><i></i>分赛区决赛阶段，参赛队伍需要完成创意作品的初步设计和策划书优化，在分赛区决赛现场展示创意作品并做答辩。评委会根据作品和答辩对参赛队伍进行综合评价，并评选出获奖队伍。分赛区特等奖、一等奖队伍获得进入全国总决赛的资格。</p>
                <p><i></i>全国总决赛阶段，参赛队伍需要最终完成创意作品设计和策划书定稿，在决赛现场展示创意作品并完成答辩。评委会根据创意作品和答辩情况对参赛队伍进行综合评价，最终评选出获奖队伍。</p>
                <p><i></i>作品评价标准包含5个维度：创新性、可行性、体现大数据或人工智能技术特征、社会价值或商业价值、评委综合评分。</p>
            </div>
            <p class="bold">（3）企业命题赛</p>
            <div style="margin-left:3em;">
                <p>企业命题赛将以大数据常见应用场景为出发点，由协办单位或金牌赞助企业设计场景问题作为赛题，赛事流程根据具体赛项规则单独制定。</p>
            </div>
        </div>
    
        <div class="eventContent">
        	<h1>Facebook的大数据科学家</h1>
            <p class="bold">（1）题目背景信息</p>
        	<p class="indent">在Facebook注册用户超过20亿人，每天会产生超过百亿条的消息、近10亿张新图片，借助大数据技术，Facebook可以跟踪用户网络行为、进行面部识别和标注、分析用户喜好等等，从而向广告客户的市场营销人员展示受众对于品牌、事件、活动和主题的反应。Facebook实际上已经成为一家大数据驱动的广告公司。为了展示其收集和挖掘大数据的能力，Facebook找伦敦创意机构Human After All设计了一副【市场洞察扑克牌】，每张牌都图文并茂地提供了一条关于用户的数据洞察信息，例如：</p>
            <p class="indent"><i></i>41%的英国人在11月就开始圣诞节采购</p>
            <p class="indent"><i></i>已婚人士比单身更喜欢讨论食物（31% vs 24%）</p>
            <p class="indent"><i></i>63%谈论奢侈品话题的用户年龄在18-34岁之间</p>
            <p class="indent"><i></i>61%的英国Facebook用户提前一周就开始为情人节做准备</p>
            <p class="indent"><i></i>刚刚有宝宝的父母们花在手机上的时间是没有宝宝的用户的 1.6 倍</p>
            <p class="indent"><i></i>母亲节那天，关于母亲节的讨论多达 9430 万次</p>
            <p class="img">
                <img src="http://117.50.29.62:80/images/topicImg.jpg" alt="">
            </p>
            <p class="indent">假设你是Facebook的大数据科学家，你的职责是为某个目标客户群，提供一组【市场洞察扑克牌】组合，为其提供市场营销策略指导，在帮助客户成功的同时也为Facebook获得广告收入。</p>
            <p class="indent">基础规则是：你只能给客户5张牌。客户基于这5条不同的市场洞察信息制定市场营销策略，因此5张牌的不同组合方案，会产生截然不同的经济效果，也为Facebook带来不一样的收入。</p>
            <p class="indent">52张牌对应52条市场洞察信息，会产生过百万的组合方式，你需要通过大数据技术，找出不同组合方案所对应的效果，并分出“市场洞察信息组合优化等级”，Facebook广告销售人员就可以根据这个优化等级表开展销售工作。</p>
            <p class="indent">经Facebook允许，你做了一次小规模内测，通过内测你收到了6000条的反馈数据，根据客户反馈回来的收益，你对每条数据进行了0~9的组合优化等级标注。</p>
            <p class="indent">接下去，你需要设计算法，根据上述 6000条内测数据及其优化等级标注，找出内在规律，为剩余100万条随机组合方案进行优化等级标注。</p>
            <p class="indent">更多关于Facebook市场洞察扑克牌信息，请点击查看<a target="_blank" href="http://news.iresearch.cn/content/2016/03/258924.shtml">报道</a>。</p>
            <p class="bold">（2）竞赛要求</p>
            <p class="indent"><i></i>训练阶段：组委会提供6000条数据作为训练数据，参赛队伍报名后可从大赛官网下载训练数据集，并进行算法设计、训练和优化。</p>
            <p class="indent"><i></i>全国总决赛阶段：组委会提供100万条正式比赛数据，参赛队伍使用自己的算法，对这100万条数据进行“优化等级”标注。</p>
            <p class="bold">（3）数据集描述</p>
            <p class="indent">训练数据集包括11个字段，字段的含义如下所示，牌面花色用C,D,H,S表示，分表代表梅花、方块、红桃和黑桃，牌面大小用1-10以及J、Q、K来表示。需要注意，字段11是每条数据的优化等级标注。</p>
            <table class="tabbleNormal" style="margin:10px 0 10px 30px;">
              <tbody>
                    <tr>
                      <th class="hidden_20">字段列</th>
                      <th class="hidden_40">字段取值</th>
                      <th class="hidden_40">字段含义</th>
                    </tr>
                    <tr>
                        <td>字段1</td>
                        <td>C、D、H、S</td>
                        <td>牌面1花色</td>
                    </tr>
                    <tr>
                        <td>字段2</td>
                        <td>1、2、3、4、5、6、7、8、9、10、J、Q、K</td>
                        <td>牌面1大小</td>
                    </tr>
                    <tr>
                        <td>字段3</td>
                        <td>C、D、H、S </td>
                        <td>牌面2花色</td>
                    </tr>
                    <tr>
                        <td>字段4</td>
                        <td>1、2、3、4、5、6、7、8、9、10、J、Q、K</td>
                        <td>牌面2大小</td>
                    </tr>
                    <tr>
                        <td>字段5</td>
                        <td>C、D、H、S </td>
                        <td>牌面3花色</td>
                    </tr>
                    <tr>
                        <td>字段6</td>
                        <td>1、2、3、4、5、6、7、8、9、10、J、Q、K</td>
                        <td>牌面3大小</td>
                    </tr>
                    <tr>
                        <td>字段7</td>
                        <td>C、D、H、S </td>
                        <td>牌面4花色</td>
                    </tr>
                    <tr>
                        <td>字段8</td>
                        <td>1、2、3、4、5、6、7、8、9、10、J、Q、K</td>
                        <td>牌面4大小</td>
                    </tr>
                    <tr>
                        <td>字段9</td>
                        <td>C、D、H、S</td>
                        <td>牌面5花色</td>
                    </tr>
                    <tr>
                        <td>字段10</td>
                        <td>1、2、3、4、5、6、7、8、9、10、J、Q、K</td>
                        <td>牌面5大小</td>
                    </tr>
                    <tr>
                        <td>字段11</td>
                        <td>0、1、2、3、4、5、6、7、8、9</td>
                        <td>优化等级标注</td>
                    </tr>
                </tbody>
            </table>
            <p class="indent">预赛和决赛数据集包括10个字段，字段的含义如下所示，牌面花色用C,D,H,S表示，分表代表梅花、方块、红桃和黑桃，牌面大小用1-10以及J、Q、K来表示。</p>
            <table class="tabbleNormal" style="margin:10px 0 10px 30px;">
              <tbody>
                    <tr>
                      <th class="hidden_20">字段列</th>
                      <th class="hidden_40">字段取值</th>
                      <th class="hidden_40">字段含义</th>
                    </tr>
                    <tr>
                        <td>字段1</td>
                        <td>C、D、H、S</td>
                        <td>牌面1花色</td>
                    </tr>
                    <tr>
                        <td>字段2</td>
                        <td>1、2、3、4、5、6、7、8、9、10、J、Q、K</td>
                        <td>牌面1大小</td>
                    </tr>
                    <tr>
                        <td>字段3</td>
                        <td>C、D、H、S </td>
                        <td>牌面2花色</td>
                    </tr>
                    <tr>
                        <td>字段4</td>
                        <td>1、2、3、4、5、6、7、8、9、10、J、Q、K</td>
                        <td>牌面2大小</td>
                    </tr>
                    <tr>
                        <td>字段5</td>
                        <td>C、D、H、S </td>
                        <td>牌面3花色</td>
                    </tr>
                    <tr>
                        <td>字段6</td>
                        <td>1、2、3、4、5、6、7、8、9、10、J、Q、K</td>
                        <td>牌面3大小</td>
                    </tr>
                    <tr>
                        <td>字段7</td>
                        <td>C、D、H、S </td>
                        <td>牌面4花色</td>
                    </tr>
                    <tr>
                        <td>字段8</td>
                        <td>1、2、3、4、5、6、7、8、9、10、J、Q、K</td>
                        <td>牌面4大小</td>
                    </tr>
                    <tr>
                        <td>字段9</td>
                        <td>C、D、H、S</td>
                        <td>牌面5花色</td>
                    </tr>
                    <tr>
                        <td>字段10</td>
                        <td>1、2、3、4、5、6、7、8、9、10、J、Q、K</td>
                        <td>牌面5大小</td>
                    </tr>
                </tbody>
            </table>
            <p class="bold">（4）评分标准</p>
            <p class="indent"><i></i>选手请将识别出的牌面组合等级的等级编号保存到txt文件中，并提交到大赛平台，提交的结果表只允许包含一个字段（等级编号），不同字段值需要通过回车换行进行分割。</p>
            <p class="indent"><i></i>预赛提交的txt文件名：dsjyycxds_preliminary.txt</p>
            <p class="indent"><i></i>分赛区决赛和全国总决赛提交的txt文件名：dsjyycxds_semifinal.txt</p>
            <p class="indent"><i></i>所提交的txt文件的内容如下所示：</p>
            <p class="img">
                <img src="http://117.50.29.62:80/images/textDemo.jpg" alt="">
            </p>
            <p class="indent"><i></i>大赛平台将自动计算测试数据集的牌面等级划分（即预测牌面的大小）的准确率。</p>
            <p class="indent"><i></i>准确率=100*预测正确的行数/测试数据集的行数</p>
            <p class="indent"><i></i>进入决赛的团队可以在8月1日-8月31日优化作品，并在竞赛官网提交作品。</p>
            <p class="indent"><i></i>竞赛平台从8月2日凌晨1点起开始更新参赛队伍作品准确率。</p>
            <p class="indent"><i></i>全国总决赛现场需要使用PPT进行答辩，答辩所用PPT需于9月5日前提交到竞赛平台上。组委会不提供答辩PPT模板，参赛队依照评分项设计PPT，从算法创新性、时间复杂度、代码可读性、代码可维护性等方面充分展示自己的程序设计。</p>
            <p class="indent"><i></i>最终得分：准确率60%+答辩评分40%。</p>
            <p class="indent"><i></i>大数据技术技能赛答辩评分项：</p>
            <p class="indent">
            	<table class="tabbleNormal" style="margin:10px 0 10px 40px;">
                	<thead>
                    	<tr>
                    	  <th class="hidden_10">序号</th>
                    	  <th class="hidden_15">评分项</th>
                    	  <th class="hidden_15">分值系数</th>
                    	  <th class="hidden_60">评分说明</th>
                    	</tr>
                    </thead>
                    <tbody>
                    	<tr>
                    	  <td>1</td>
                    	  <td>算法创新性</td>
                    	  <td>20%</td>
                    	  <td>创新性算法>对经典算法进行改进>编码实现经典算法>直接调用已封装好的经典算法的类库</td>
                    	</tr>
                    	<tr>
                    	  <td>2</td>
                    	  <td>时间复杂度</td>
                    	  <td>20%</td>
                    	  <td>时间复杂度越小得分越高</td>
                    	</tr>
                    	<tr>
                    	  <td>3</td>
                    	  <td>代码可读性</td>
                    	  <td>20%</td>
                    	  <td>从编码规范、代码结构、代码注释等方面进行评价</td>
                    	</tr>
                    	<tr>
                    	  <td>4</td>
                    	  <td>代码可维护性</td>
                    	  <td>20%</td>
                    	  <td>从设计模式、代码复用、封装、抽象等方面进行评价</td>
                    	</tr>
                    	<tr>
                    	  <td>5</td>
                    	  <td>答辩表现</td>
                    	  <td>20%</td>
                    	  <td>评委根据竞赛队伍现场答辩的表现给出综合评分</td>
                    	</tr>
                    </tbody>
                </table>
            </p>
            <p class="bold">（5）数据下载</p>
            <p class="file">训练数据集：<a href="http://117.50.29.62:80/training-final.csv">training-final.csv</a></p>
            <p class="file">全国总决赛数据集：<a href="http://117.50.29.62:80/Semifinal-testing-final.csv">Semifinal-testing-final.csv</a></p>
        </div>
        
        <div class="eventContent">
            <p style="margin-top:12px;">大数据与人工智能创意赛（简称“创意赛”）重点考察参赛队伍的创造力和应用设计能力，参赛团队围绕大数据和人工智能相关技术和应用场景进行自由创作，并按照模版提交商业模式策划书。专家组将对参赛作品主题和内容进行审核，非原创的、违反赛事精神或章程、具有攻击性质、不符合普适价值观或是与国家有关法律法规相违背的作品将不允许参加竞赛，组委会有权要求参赛队伍进行修改或取消其参赛资格。</p>
            <div style="margin-left:1em;">
                <p><i></i>创意赛作品包括两部分：项目策划书、作品。</p>
                <p><i></i>参赛队根据组委会所提供的《大数据与人工智能创意赛项目策划书模板》完成作品策划书设计，并与8月31日前提交。</p>
                <p><i></i>参赛队伍需要最终完成创意作品设计，并在决赛答辩现场进行演示，参赛队伍自行准备演示环境，现场可提供网络。</p>
                <p><i></i>答辩过程分为两部分：答辩（15分钟）+演示（5分钟）。</p>
                <p><i></i>大数据与人工智能创意赛答辩评分项：</p>
                <p class="indent">
                    <table class="tabbleNormal" style="margin:10px 0 10px 40px;">
                        <thead>
                            <tr>
                              <th class="hidden_10">序号</th>
                              <th class="hidden_15">评分项</th>
                              <th class="hidden_15">分值系数</th>
                              <th class="hidden_60">评分说明</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                              <td>1</td>
                              <td>创新性</td>
                              <td>20%</td>
                              <td>体现或部分体现新发现、新方法、新成果</td>
                            </tr>
                            <tr>
                              <td>2</td>
                              <td>可行性</td>
                              <td>20%</td>
                              <td>技术路线可行、设计构想能够实现，需要用作品证实</td>
                            </tr>
                            <tr>
                              <td>3</td>
                              <td>体现大数据或人工智能技术特征</td>
                              <td>20%</td>
                              <td>用大数据或人工智能的思维、算法、方法来解决问题</td>
                            </tr>
                            <tr>
                              <td>4</td>
                              <td>社会价值或商业价值</td>
                              <td>20%</td>
                              <td>能够解决社会问题，后续有产品化、产业化的可能性</td>
                            </tr>
                            <tr>
                              <td>5</td>
                              <td>答辩表现</td>
                              <td>20%</td>
                              <td>评委根据竞赛队伍现场答辩的表现给出综合评分</td>
                            </tr>
                        </tbody>
                    </table>
                </p>
            </div>
         </div>
        
        <div class="eventContent">
        	<h1>[浪潮杯] 美丽中国-2018全域旅游年</h1>
            <p class="bold">（1）赛题背景</p>
        	<p class="indent">国家旅游局宣布2018年为“美丽中国—全域旅游年”，详见<a target="_blank" href="http://www.cnta.gov.cn/xxfb/jdxwnew2/201801/t20180112_853351.shtml">链接</a>。</p>
            <p class="indent">世界那么大，我想去看看，其实不用旅游局的口号，我们都想去各地逛逛。但是，由于地域发展不够平衡、服务水平差、周边服务薄弱、基础设施不健全或是虚假宣传等各种各样的原因，旅游景区鱼龙混杂，乘兴而去败兴而归的旅程还是经常会遇到的，我们在百度上搜索“旅游景点 坑”等关键词，可以搜到超过400万条结果，吓得宝宝都不敢出门了。</p>
            <p class="indent">现在，浪潮集团给我们提供了海量的景区评价数据，你能否对这些数据集进行分析处理，把全国的旅游景点做个评价排序？</p>
            <p class="bold">（2）赛题详述</p>
            <p class="indent"><i></i>任务描述</p>
            <p class="indent">训练阶段：组委会提供20000条数据作为训练数据，这些训练数据含有评论详情和评论等级，参赛队伍可以借助数据挖掘技术，设计算法分析评论内容和评论等级。</p>
            <p class="indent">全国总决赛阶段：组委会提供100万条正式比赛数据，这些数据仅有评论内容，参赛队伍需要根据评论内容计算出评论等级。</p>
            <p class="indent"><i></i>数据集描述</p>
            <p class="indent">训练数据集包括3个字段，评论等级好/中/差 用1/2/3标识，如下所示：</p>
<table class="tabbleNormal" style="margin:10px 0 10px 30px;">
              <tbody>
                    <tr>
                      <th class="hidden_20">字段列</th>
                      <th class="hidden_40">字段取值</th>
                      <th class="hidden_40">字段含义</th>
                    </tr>
                    <tr>
                        <td>ROWKEY</td>
                        <td>1001</td>
                        <td>主键</td>
                    </tr>
                    <tr>
                        <td>COMMCONTENT</td>
                        <td>服务还不错...</td>
                        <td>评论详情</td>
                    </tr>
                    <tr>
                        <td>COMMLEVEL</td>
                        <td>1/2/3</td>
                        <td>评论等级</td>
                    </tr>
                </tbody>
            </table>        
            <p class="indent">预赛和决赛数据集包括2个字段，含义如下所示：</p>
<table class="tabbleNormal" style="margin:10px 0 10px 30px;">
              <tbody>
                    <tr>
                      <th class="hidden_20">字段列</th>
                      <th class="hidden_40">字段取值</th>
                      <th class="hidden_40">字段含义</th>
                    </tr>
                    <tr>
                        <td>ROWKEY</td>
                        <td>1001</td>
                        <td>主键</td>
                    </tr>
                    <tr>
                        <td>COMMCONTENT</td>
                        <td>服务太差啦...</td>
                        <td>评论详情</td>
                    </tr>
                </tbody>
            </table>        
            <p class="indent"><i></i>2.3 数据集下载</p>
            <p class="indent">训练数据集：<a href="http://117.50.29.62:80/training-inspur.csv">training.csv</a>。</p>
            <p class="indent">浪潮杯企业命题赛预赛、决赛数据集下载地址：<a target="_blank" href="https://www.tdata.cn/operate/competition/index">https://www.tdata.cn/operate/competition/index</a>。</p>
            <p class="indent">下载步骤：</p>
            <p class="indent">① 登陆上述网址，进入企业命题赛主题页，在“数据集下载”区域可看到“下载”按钮。</p>
            <p class="indent">② 如您未注册过天元数据网账号，需要先注册账号。在完成账号注册后，系统会自动跳转会上述页面。</p>
            <p class="indent">③ 点击“下载”按钮，输入下载码即可下载预赛和决赛数据集。</p>
            <p class="indent">下载码：</p>
            <p class="indent">4T13A5FP8、4U348GY86、4UW3ALR25、4X3IJF287、4X5Z42S27、4ZB9A3142、5054632Y6、512V77PC3、51D9553T0、524887933（注：任选其一使用即可）</p>
            <p class="bold">（3）开发平台</p>
            <p class="indent">竞赛队伍可以使用任何平台来完成本竞赛题目。</p>
            <p class="indent">参赛队伍也可使用浪潮“云海Insight HD”大数据平台（非大赛指定平台）进行算法开发。云海Insight HD是一套经过调优和功能增强的Hadoop与Spark企业发行版，包含Hadoop生态中的20+主要组件，帮助参赛队伍轻松应对海量数据的采集、存储、计算、分析挖掘和数据安全等应用场景。云海Insight HD提供涵盖多源数据接入、数据特征提取、算法模型管理、算法模型评估和结果预测等完整机器学习过程的可视化大数据分析功能。支持多元分类、回归分析、协同推荐等分析模式，SVM、朴素贝叶斯、K-Means、线性回归等10+种算法，支持批量预测和实时预测功能并提供API。预测过程基于内存进行迭代式计算，并且支持分布式计算，具备极强的扩展性，可以应对海量数据分析。</p>
            <p class="indent">详细产品介绍可点击<a href="http://www.inspur.com/lcjtww/2315499/2315503/2317666/2318123/2350188/index.html" target="_blank">链接</a>查看，云海Insight HD平台为商业级付费平台，如有使用需求，可和浪潮古经理联系，联系电话13104150510。</p>
            <p class="bold">（4）作品提交与评分</p>
            <p class="indent"><i></i>选手请将识别出的景点评价分类值保存到txt文件中，并提交到大赛平台，提交的结果表只允许包含一个字段（等级编号），不同字段值需要通过回车换行进行分割。</p>
            <p class="indent"><i></i>分赛区决赛和全国总决赛提交的txt文件名：dsjyycxds_semifinal.txt</p>
            <p class="indent"><i></i>所提交的txt文件的内容如下所示：</p>
            <p class="img">
                <img src="http://117.50.29.62:80/images/txtDemo.png" alt="">
            </p>
            <p class="indent"><i></i>大赛平台将自动计算参赛队伍所提交作品的分类值的准确率。</p>
            <p class="indent"><i></i>准确率=100*预测正确的行数/竞赛数据集的行数</p>
            <p class="indent"><i></i>进入决赛的团队可以在8月1日-8月31日优化作品，并在竞赛官网提交作品。</p>
            <p class="indent"><i></i>竞赛平台从8月2日凌晨1点起开始更新参赛队伍作品准确率。</p>
            <p class="indent"><i></i>全国总决赛现场需要使用PPT进行答辩，答辩所用PPT需于9月5日前提交到竞赛平台上。组委会不提供答辩PPT模板，参赛队依照评分项设计PPT，从算法创新性、时间复杂度、代码可读性、代码可维护性等方面充分展示自己的程序设计。</p>
            <p class="indent"><i></i>最终得分：准确率60%+答辩评分40%。</p>
            <p class="indent"><i></i>企业命题赛答辩评分项：</p>
            <p class="indent">
                <table class="tabbleNormal" style="margin:10px 0 10px 40px;">
                    <thead>
                        <tr>
                          <th class="hidden_10">序号</th>
                          <th class="hidden_15">评分项</th>
                          <th class="hidden_15">分值系数</th>
                          <th class="hidden_60">评分说明</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                          <td>1</td>
                          <td>算法创新性</td>
                          <td>20%</td>
                          <td>创新性算法>对经典算法进行改进>编码实现经典算法>直接调用已封装好的经典算法的类库</td>
                        </tr>
                        <tr>
                          <td>2</td>
                          <td>时间复杂度</td>
                          <td>20%</td>
                          <td>时间复杂度越小得分越高</td>
                        </tr>
                        <tr>
                          <td>3</td>
                          <td>代码可读性</td>
                          <td>20%</td>
                          <td>从编码规范、代码结构、代码注释等方面进行评价</td>
                        </tr>
                        <tr>
                          <td>4</td>
                          <td>代码可维护性</td>
                          <td>20%</td>
                          <td>从设计模式、代码复用、封装、抽象等方面进行评价</td>
                        </tr>
                        <tr>
                          <td>5</td>
                          <td>答辩表现</td>
                          <td>20%</td>
                          <td>评委根据竞赛队伍现场答辩的表现给出综合评分</td>
                        </tr>
                    </tbody>
                </table>
            </p>
        </div>
    </div>
</div>







<div class="foot">
	<div class="top">
    	<div class="wrap">
            <h2>关于我们</h2>
            <p>竞赛官方网站：www.bigdataedu.com</p>
            <p>竞赛官方邮箱：bdc2018@bigdataedu.com</p>
            <p>赛事组织联系人：周璧成 18610110628</p>
            <p>报名工作联系人：凌潇 13426213688</p>
            <p>赛事合作联系人：刘芳 13681424390</p>
            <p>秘书处邮寄地址：北京市海淀区上地中关村软件园一期立思辰大厦（邮政编码 100193）</p>
        </div>
    </div>
    <div class="bot"></div>
</div>

<script type="text/javascript">

function resetFoot(){
	var temH = $(".foot").css("position") == "fixed" ? 218 : 0;
	if(($("body").height() + temH ) >= $(window).height()){
		$(".foot").css({"position":"static"})
	}else{
		$(".foot").css({"position":"fixed"})
	}
}



$(function(){
	
	resetFoot();
	$(window).resize(function(){
		resetFoot();
	})
	
	$(document).scroll(function(){
		if($(this).scrollTop() > ($(window).height()/2)){
			if($("#returnTop").length == 0){
				$("body").append("<a href='javascript:;' class='returnTop' id='returnTop'>返回顶部</a>");
			}else{
				$("#returnTop").fadeIn(120);
			}
		}else{
			$("#returnTop").fadeOut(120);
		}	
	})
	
	$("body").on("click","#returnTop",function(){
		$("html,body").animate({scrollTop:0});	
	});
	
})

</script>

</body>
</html>
