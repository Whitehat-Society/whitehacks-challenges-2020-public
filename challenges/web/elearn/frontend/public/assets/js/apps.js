/*
Template Name: Color Admin Responsive Admin Template
Author: Sean Ngu
Author URL: http://www.sean-theme.com/pixel-admin/
Version: 1.0
    ----------------------------
        APPS CONTENT TABLE
    ----------------------------
    
    <!-- ======== GLOBAL SCRIPT SETTING ======== -->
    01. Handle Scrollbar
    
    02. Handle Sidebar - Menu
    03. Handle Sidebar - Mobile View Toggle
    04. Handle Sidebar - Minify / Expand
    05. Handle Page Load - Fade in
    06. Handle Panel - Remove / Reload / Collapse / Expand
    07. Handle Panel - Draggable
    08. Handle Tooltip & Popover Activation
    09. Handle Scroll to Top Button Activation
	
    <!-- ======== APPLICATION SETTING ======== -->
    Application Controller
*/



/* 01. Handle Scrollbar
------------------------------------------------ */
var handleSlimScroll = function() {
  "use strict";
  $('[data-scrollbar=true]').each( function() {
    var dataHeight = $(this).attr('data-height');
        dataHeight = (!dataHeight) ? $(this).height() : dataHeight;
    $(this).slimScroll({height: dataHeight, alwaysVisible: true});
  });
};


/* 02. Handle Sidebar - Menu
------------------------------------------------ */
var handleSidebarMenu = function() {
  "use strict";
  $('.sidebar .nav > .has-sub > a').click(function() {
    var target = $(this).next('.sub-menu');
    var otherMenu = '.sidebar .nav > li.has-sub > .sub-menu';
    
    $(otherMenu).not(target).slideUp(250);
    $(target).slideToggle(250);
  });
  $('.sidebar .nav > .has-sub .sub-menu li.has-sub > a').click(function() {
    var target = $(this).next('.sub-menu');
    $(target).slideToggle(250);
  });
};


/* 03. Handle Sidebar - Mobile View Toggle
------------------------------------------------ */
var handleMobileSidebarToggle = function() {
    $('.sidebar').click(function(e) {
        e.stopPropagation();
    });
    $(document).click(function(e) {
        if (!e.isPropagationStopped()) {
            if ($('#page-container').hasClass('sidebar-toggled')) {
                $('#page-container').removeClass('sidebar-toggled');
            }
        }
    });
    $('[data-click=sidebar-toggled]').click(function(e) {
        e.stopPropagation();
        var sidebarClass = 'sidebar-toggled';
        var targetContainer = '#page-container';
        if ($(targetContainer).hasClass(sidebarClass)) {
            $(targetContainer).removeClass(sidebarClass);
        } else {
            $(targetContainer).addClass(sidebarClass);
        }
    });
};


/* 04. Handle Sidebar - Minify / Expand
------------------------------------------------ */
var handleSidebarMinify = function() {
    $('[data-click=sidebar-minify]').click(function(e) {
        e.preventDefault();
        var sidebarClass = 'sidebar-minified';
        var targetContainer = '#page-container';
        if ($(targetContainer).hasClass(sidebarClass)) {
            $(targetContainer).removeClass(sidebarClass);
        } else {
            $(targetContainer).addClass(sidebarClass);
        }
        
        $(window).trigger('resize');
    });
};


/* 05. Handle Page Load - Fade in
------------------------------------------------ */
var handlePageContentView = function() {
  "use strict";
  $(window).load(function() {
      $.when($('#page-loader').addClass('hide')).done(function() {
        $('#page-container').addClass('in');
      });
  });
};


/* 06. Handle Panel - Remove / Reload / Collapse / Expand
------------------------------------------------ */
var handlePanelAction = function() {
    "use strict";
    
    // remove
    $('[data-click=panel-remove]').hover(function() {
        $(this).tooltip({
            title: 'Remove',
            placement: 'bottom',
            trigger: 'hover',
            container: 'body'
        });
        $(this).tooltip('show');
    });
    $('[data-click=panel-remove]').click(function(e) {
        e.preventDefault();
        $(this).closest('.panel').remove();
    });
    
    // collapse
    $('[data-click=panel-collapse]').hover(function() {
        $(this).tooltip({
            title: 'Collapse / Expand',
            placement: 'bottom',
            trigger: 'hover',
            container: 'body'
        });
        $(this).tooltip('show');
    });
    $('[data-click=panel-collapse]').click(function(e) {
        e.preventDefault();
        $(this).closest('.panel').find('.panel-body').slideToggle();
    });
    
    // reload
    $('[data-click=panel-reload]').hover(function() {
        $(this).tooltip({
            title: 'Reload',
            placement: 'bottom',
            trigger: 'hover',
            container: 'body'
        });
        $(this).tooltip('show');
    });
    $('[data-click=panel-reload]').click(function(e) {
        e.preventDefault();
        var target = $(this).closest('.panel');
        if (!$(target).hasClass('panel-loading')) {
            var targetBody = $(target).find('.panel-body');
            var spinnerHtml = '<div class="panel-loader"><span class="spinner-small"></span></div>';
            $(target).addClass('panel-loading');
            $(targetBody).prepend(spinnerHtml);
            setTimeout(function() {
                $(target).removeClass('panel-loading');
                $(target).find('.panel-loader').remove();
            }, 2000);
        }
    });
    
    
    // expand
    $('[data-click=panel-expand]').hover(function() {
        $(this).tooltip({
            title: 'Expand / Compress',
            placement: 'bottom',
            trigger: 'hover',
            container: 'body'
        });
        $(this).tooltip('show');
    });
    $('[data-click=panel-expand]').click(function(e) {
        e.preventDefault();
        var target = $(this).closest('.panel');
    
        if ($('body').hasClass('panel-expand') && $(target).hasClass('panel-expand')) {
            $('body, .panel').removeClass('panel-expand');
            $('.panel').removeAttr('style');
            $('[class*=col]').sortable('enable');
        } else {
            $('body').addClass('panel-expand');
            $(this).closest('.panel').addClass('panel-expand');
            $('[class*=col]').sortable('disable');
        }
        $(window).trigger('resize');
    });
};


/* 07. Handle Panel - Draggable
------------------------------------------------ */
var handleDraggablePanel = function() {
  "use strict";
  var target = '[class*=col]';
  var targetHandle = '.panel-heading';
  var connectedTarget = '.row > [class*=col]';
  
  $(target).sortable({
    handle: targetHandle,
    connectWith: connectedTarget
  });
};


/* 08. Handle Tooltip & Popover Activation
------------------------------------------------ */
var handelTooltipPopoverActivation = function() {
  "use strict";
  $('[data-toggle=tooltip]').tooltip();
  $('[data-toggle=popover]').popover();
};


/* 09. Handle Scroll to Top Button Activation
------------------------------------------------ */
var handleScrollToTopButton = function() {
  "use strict";
  $(document).scroll( function() {
    var totalScroll = $(document).scrollTop();
    
    if (totalScroll >= 200) {
      $('[data-click=scroll-top]').addClass('in');
    } else {
      $('[data-click=scroll-top]').removeClass('in');
    }
  });
  
  $('[data-click=scroll-top]').click(function(e) {
    e.preventDefault();
    $('html, body').animate({
      scrollTop: $("body").offset().top
    }, 500);
  });
};


/* Application Controller
------------------------------------------------ */
var App = function () {
	"use strict";
	
	return {
		//main function
		init: function () {
		  
			// slimscroll
			handleSlimScroll();
			
			// sidebar
			handleSidebarMenu();
			handleMobileSidebarToggle();
			handleSidebarMinify();
			
			handlePageContentView();
			handlePanelAction();
			handleDraggablePanel();
			handelTooltipPopoverActivation();
			handleScrollToTopButton();
		}
  };
}();