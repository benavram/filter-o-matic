function get_replacement() {
    var grawlix=''
    var _fom_rpsp = '\uf256'
    var _fom_rpsr = '\uf255'
    var _fom_spss = '\uf257'
    var _fom_rpsl = '\uf258'
    var _fom_rpssp = '\uf259'
    var fom_options = {
        1 : _fom_rpsp,
        2: _fom_rpsr,
        3: _fom_spss,
        4: _fom_rpsl,
        5: _fom_rpssp
        };
     var c = 4 + Math.floor(Math.random() * 6); //character limit 
     console.log(c)
    for (var i = 0; i < c; i++) {
     var n = 1 + Math.floor(Math.random() * 5);
     grawlix = grawlix + fom_options[n]
        } ; 
    $('#item').attr('data-content',grawlix);
};








    ////for grawlixes
    //var _fom_wrench= "\uf0ad"
    //var _fom_asterisk= "\uf069"
    //var _fom_hashtag= "\uf292"
    //var _fom_exclamation= "\uf12a"
    //var _fom_at= "\uf1fa"
    //var _fom_question= "\uf128"
    //var _fom_close= "\uf00d"
    //var _fom_dollar= "\uf155"
    //var _fom_gbp= "\uf154"
    //var _fom_yen= "\uf157"
    //var _fom_eur= "\uf153"
    //var _fom_bolt= "\uf0e7"
    //var _fom_heart= "\uf004"
    ////rpsls
    //var _fom_paper-o= "\uf256"
    //var _fom_rock-o= "\uf255"
    //var _fom_scissors-o= "\uf257"
    //var _fom_lizard-o= "\uf258"
    //var _fom_spock-o= "\uf259"
    ////sw
    //var _fom_ra= "\uf1d0"
    //var _fom_empire= "\uf1d1"