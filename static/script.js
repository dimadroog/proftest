/**
 * Created by droog on 11.04.16.
 */
function c(par){
    return console.log(par)
}
function StayCheck(elm){
    jQuery(elm).parent().find('#yes').prop( "checked", true );
    jQuery(elm).focus();
}

jQuery( document ).ready(function() {

    var learn_subjects_limit = 4;
    jQuery('input.learn-subject-checkbox').on('change', function(evt) {
       if(jQuery(this).siblings(':checked').length >= learn_subjects_limit) {
           this.checked = false;
       }
    });

     var priority_prof_limit = 3;
    jQuery('input.priority-prof-checkbox').on('change', function(evt) {
       if(jQuery(this).siblings(':checked').length >= priority_prof_limit) {
           this.checked = false;
       }
    });

    jQuery('input:radio[class="rad"]').change(function(){
        if(jQuery(this).val() == 'yes') {
            jQuery(this).parent().find('.form-control').show();
            jQuery(this).parent().find('.help-block').show();
            jQuery(this).parent().find('.form-control').focus();
            jQuery(this).parent().find('.form-control').prop('required', true);
        } else {
            jQuery(this).parent().find('.form-control').hide();
            jQuery(this).parent().find('.help-block').hide();
            jQuery(this).parent().find('.form-control').val('');
            jQuery(this).parent().find('.form-control').prop('required', false);
        }
    });

    jQuery('input:radio[class="rad11"]').change(function(){
        if(jQuery(this).val() == 'yes_but_do_not' || jQuery(this).val() == 'no') {
            //virubaem
            jQuery(this).parent().parent().find('.form-control').hide();
            jQuery(this).parent().parent().find('.form-control').val('');
            jQuery(this).parent().parent().find('.help-block').hide();
            jQuery(this).parent().parent().find('.form-control').prop('required', false);
            //vrubaem
            jQuery(this).parent().find('.form-control').show();
            jQuery(this).parent().find('.help-block').show();
            jQuery(this).parent().find('.form-control').focus();
            jQuery(this).parent().find('.form-control').prop('required', true);
        } else {
            jQuery(this).parent().find('.form-control').hide();
            jQuery(this).parent().find('.help-block').hide();
            jQuery(this).parent().find('.form-control').val('');
            jQuery(this).parent().find('.form-control').prop('required', false);
        }
    });


    jQuery('#relative_to_9').find('input:radio[class="rad"]').change(function(){
        if(jQuery(this).val() == 'yes') {
            jQuery('#depended_on_8').removeClass('text-muted');
            jQuery('#depended_on_8').find('.hdyk-checkbox').prop('disabled', false);
            jQuery('#no_9').hide();
            jQuery('#yes_9').show();
        } else {
            jQuery('#depended_on_8').addClass('text-muted');
            jQuery('#depended_on_8').find('.hdyk-checkbox').prop('disabled', true);
            jQuery('#depended_on_8').find('.hdyk-checkbox').prop('checked', false);
            jQuery(this).parent().find('.help-block').show();
            jQuery('#no_9').show();
            jQuery('#yes_9').hide();
        }
    });


    jQuery('#sen_relative_6').find('input:radio').change(function(){
        if(jQuery(this).val() == 'work' || jQuery(this).val() == 'relax' || jQuery(this).val() == 'army'){
            jQuery('.sen_depended_on_6').addClass('text-muted');
            jQuery('.sen_depended_on_6').find('input').prop('disabled', true);
            jQuery('.sen_depended_on_6').find('input:text').val('').hide();
            jQuery('.sen_depended_on_6').find('input').prop('checked', false);
            jQuery(this).parent().find('.help-block').show();
            jQuery('#rel_7_mess').hide();
            jQuery('#rel_6_mess').show();
            jQuery('#other_6_mess').hide();
        } else {
            jQuery('.sen_depended_on_6').removeClass('text-muted');
            jQuery('.sen_depended_on_6').find('input').prop('disabled', false);
            jQuery('#rel_6_mess').hide();
            jQuery('#other_6_mess').show();
        }
    });


    jQuery('#sen_relative_7').find('input:radio').change(function(){
        if(jQuery(this).val() == 'not_know'){
            jQuery('.sen_depended_on_7').addClass('text-muted');
            jQuery('.sen_depended_on_7').find('input').prop('disabled', true);
            jQuery('.sen_depended_on_7').find('input').prop('checked', false);
            jQuery('#rel_7_mess').show();
            jQuery('#other_7_mess').hide();
            jQuery('.sen_depended_on_7').find('input:text').val('').hide();
        } else {
            jQuery('.sen_depended_on_7').removeClass('text-muted');
            jQuery('.sen_depended_on_7').find('input').prop('disabled', false);
            jQuery('#rel_7_mess').hide();
            jQuery('#other_7_mess').show();
        }
    });

    jQuery('input:checkbox[class="self-var-checkbox"]').change(function(){
        if(jQuery(this).is( ":checked" )) {
            jQuery(this).parent().find('.form-control').show();
            jQuery(this).parent().find('.help-block').show();
            jQuery(this).parent().find('.form-control').focus();
            jQuery(this).parent().find('.form-control').prop('required', true);
        } else {
            jQuery(this).parent().find('.form-control').hide();
            jQuery(this).parent().find('.help-block').hide();
            jQuery(this).parent().find('.form-control').val('');
            jQuery(this).parent().find('.form-control').prop('required', false);
        }
    });


    jQuery('input:radio[class="self-var-radio"]').change(function(){
        if(jQuery(this).is( ":checked" )) {

            jQuery(this).parent().parent().find('.form-control').hide();
            jQuery(this).parent().parent().find('.help-block').hide();
            jQuery(this).parent().parent().find('.form-control').val('');
            jQuery(this).parent().parent().find('.form-control').prop('required', false);

            jQuery(this).parent().find('.form-control').show();
            jQuery(this).parent().find('.help-block').show();
            jQuery(this).parent().find('.form-control').focus();
            jQuery(this).parent().find('.form-control').prop('required', true);
        }
    });

    jQuery('input:radio[class="anoter-var-radio"]').change(function(){
        if(jQuery(this).is( ":checked" )) {
            var slf_rad = jQuery(this).parent().find('input:radio[class="self-var-radio"]');
            jQuery(slf_rad).parent().find('.form-control').hide();
            jQuery(slf_rad).parent().find('.help-block').hide();
            jQuery(slf_rad).parent().find('.form-control').val('');
            jQuery(slf_rad).parent().find('.form-control').prop('required', false);
        }
    });

    jQuery('input:checkbox[class="interest-checkbox"]').change(function(){
        if(jQuery(this).is( ":checked" )) {
            jQuery(this).closest('.interest-tr').addClass('bg-primary');
        } else {
            jQuery(this).closest('.interest-tr').removeClass('bg-primary');
            jQuery(this).closest('.interest-tr').find('input:text').val('');
        }
    });


    jQuery(".panel-toggler").click(function() {
        var panel_hidden = jQuery(this).closest('#result_panel').find('.panel-hidden');
        if (panel_hidden.css('display') == 'none'){
            panel_hidden.slideDown(100);
        } else {
            panel_hidden.slideUp(100);
        }
    });


    jQuery(".view-label").click(function(event) {
        event.stopPropagation();
        var elm = jQuery(this);
        var obj = jQuery.parseJSON(jQuery(this).attr('data'));
        jQuery.ajax({
            type: 'POST',
            url: '/change_view/',
            data: {'id': obj.id, 'group': obj.group},
            success: function(data){
                if (data == 1){
                    elm.removeClass('label-primary');
                    elm.addClass('label-success');
                    elm.closest('#result_panel').removeClass('panel-primary');
                    elm.closest('#result_panel').addClass('panel-success');
                    elm.text('Просмотренно')
                } else if (data == 0){
                    elm.removeClass('label-success');
                    elm.addClass('label-primary');
                    elm.closest('#result_panel').removeClass('panel-success');
                    elm.closest('#result_panel').addClass('panel-primary');
                    elm.text('Непросмотренно')
                }
            },
            error: function(){
                alert('error');
            }
        });
    });


});

/* interests */
function StayCheckInterests(elm){
    jQuery(elm).closest('.interest-tr').find('input:checkbox[class="interest-checkbox"]').prop( "checked", true );
    jQuery(elm).closest('.interest-tr').addClass('bg-primary');
    if (jQuery(elm).val() == ''){
        jQuery(elm).closest('.interest-tr').find('input:checkbox[class="interest-checkbox"]').prop( "checked", false );
        jQuery(elm).closest('.interest-tr').removeClass('bg-primary');
    }
}

function BuildInterests(){
    var arr = [];
    jQuery('.interest-tr').each(function(){
        var tr = jQuery(this);
        var checkbox = tr.find('input:checkbox');
        var id = tr.find('.interest-id');
        var input = tr.find('input:text');
        if(checkbox.is(':checked')) {
            arr.push({ 'id' : id.text(), 'status' : 1, 'value' : input.val()});
        } else {
            arr.push({ 'id' : id.text(), 'status' : 0, 'value' : input.val()});
        }
    });
    jQuery('#build_interests').val(JSON.stringify(arr));
}
/* end interests */

function ViewOtherAnswers(elm, cls, sch, group, field){
    jQuery.ajax({
        type: 'POST',
        url: '/view_other_answers/',
        data: {'field': field, 'group':group, 'school':sch, 'class':cls},
        success: function(data){
            jQuery(elm).parent().find('.other-answers').html(data);
        },
        error: function(){
            alert('error');
        }
    });
}
