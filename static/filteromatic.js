//-*- coding: utf-8 -*-
//filter-o-matic jquery functions
//    Copyright (c) 2016 office(ish).com
//
//    https://github.com/benavram/filter-o-matic
//
//    This file is part of filter-o-matic.
//
//    filter-o-matic is free software: you can redistribute it and/or modify
//    it under the terms of the GNU General Public License as published by
//    the Free Software Foundation, either version 3 of the License, or
//    (at your option) any later version.
//
//    Foobar is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//    GNU General Public License for more details.
//
//    You should have received a copy of the GNU General Public License
//    along with [app name].  If not, see <http://www.gnu.org/licenses/> or
//    <https://github.com/benavram/filter-o-matic/blob/master/LICENSE>
//
//  # Configuration variables
//
//API docs at https://github.com/benavram/filter-o-matic
//# Authors:

//variables: setup unicode for FontAwesome fonts
var _fom_rpsp = '\uf256'
var _fom_rpsr = '\uf255'
var _fom_spss = '\uf257'
var _fom_rpsl = '\uf258'
var _fom_rpssp = '\uf259'
var _fom_asterisk = "\uf069"
//var _fom_hashtag = "\uf292""\uf155"
var _fom_hashtag = "\uf155"
var _fom_exclamation = "\uf12a"
var _fom_at = "\uf1fa"
var _fom_question = "\uf128"
var _fom_close = "\uf00d"
var _fom_dollar = "\uf155"
var _fom_gbp = "\uf154"
var _fom_yen = "\uf157"
var _fom_eur = "\uf153"
var _fom_bolt = "\uf0e7"
var _fom_heart = "\uf004"
var _fom_ra = "\uf1d0"
var _fom_empire = "\uf1d1"

//replacement set: FontAwesome rpsls
var fom_rpsls = {
  1: _fom_rpsp,
  2: _fom_rpsr,
  3: _fom_spss,
  4: _fom_rpsl,
  5: _fom_rpssp
};

//replacement set: FontAwesome symbols
var fom_syms = {
  1: _fom_at, 
  2: _fom_asterisk,
  3: _fom_hashtag,
  4: _fom_exclamation,
  5: _fom_at,
  6: _fom_question,
  7: _fom_close,
  8: _fom_dollar,
  9: _fom_gbp,
  10: _fom_yen,
  11: _fom_eur,
  12: _fom_bolt,
  13: _fom_heart,
  14: _fom_exclamation,

};

//replacement set: FontAwesome combined
var fom_all = {
  1: _fom_at,
  2: _fom_asterisk,
  3: _fom_hashtag,
  4: _fom_exclamation,
  5: _fom_at,
  6: _fom_question,
  7: _fom_close,
  8: _fom_dollar,
  9: _fom_gbp,
  10: _fom_yen,
  11: _fom_eur,
  12: _fom_bolt,
  13: _fom_heart,
  14: _fom_ra,
  15: _fom_empire,
  16: _fom_exclamation,
  17: _fom_at,
  18: _fom_rpsp,
  19: _fom_rpsr,
  20: _fom_spss,
  21: _fom_rpsl,
  22: _fom_rpssp
};
var text
var clean_text
var string_replacement
var rep_type

$.fn.filteromatic = function(rep_type) {
// main funciton = grabs text to be cleaned from element (by id)
// makes a json request to Filter-o-matic to get marked up text
// then applies the filtered text to the elements
// arguments:
//      rep_type:  replacement set type.  defaults to symbols
  if (typeof(rep_type)==='undefined') rep_type = fom_syms;
  var ele = this
  var text = $(this).html();
    //dev path for json request
    $.getJSON($SCRIPT_ROOT + '/evaluate/', {
      replacement_type: 'font_awesome',
      eval_string: text
    }, function(data) {
     clean_text = (data.clean_string);
     no_reps = (clean_text.match(/_fom_item/g) || []).length;
     string_replacement = get_replacement(clean_text, no_reps, rep_type);
     $(ele).html(string_replacement);
    });
};

function get_replacement(str_input, no_reps, rep_type) {
// construct the replacment elements s <span>s for insert
  for (var i = 0; i < no_reps; i++) {
    var g = build_replacements(rep_type);
    var e = "<span class='fom_inline' data-content=" + g + "></span>"
    str_input = str_input.replace('_fom_item', e);
  };
  return str_input;
};

function build_replacements(rep_type) {
// adds icons to strings as unicode
  var y = Object.keys(rep_type).length;
  var n = 1 + Math.floor(Math.random() * y);
  var u_item = ''
  var tmp_item = ''
  var grawlix = ''
  
  for (var i = 0; i < 5; i++) {
    var n = 1 + Math.floor(Math.random() * y);
    u_item = rep_type[n]
    while (u_item == tmp_item) {
        var n = 1 + Math.floor(Math.random() * y);
        u_item = rep_type[n]
    }
    tmp_item = u_item
    grawlix = grawlix + tmp_item
    }
  
  grawlix = ' ' + grawlix + ' '
  return grawlix
};