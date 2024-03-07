PROFILE = {
    "include_profiles": ["universal", "outline", "shaping", "ufo_sources"],
    "sections": {
        "Metadata Checks": [
            "com.google.fonts/check/metadata/parses",
            "com.google.fonts/check/metadata/unknown_designer",
            "com.google.fonts/check/metadata/multiple_designers",
            "com.google.fonts/check/metadata/designer_values",
            "com.google.fonts/check/metadata/unique_full_name_values",
            "com.google.fonts/check/metadata/unique_weight_style_pairs",
            "com.google.fonts/check/metadata/license",
            "com.google.fonts/check/metadata/menu_and_latin",
            "com.google.fonts/check/metadata/subsets_order",
            "com.google.fonts/check/metadata/includes_production_subsets",
            "com.google.fonts/check/metadata/copyright",
            "com.google.fonts/check/metadata/familyname",
            "com.google.fonts/check/metadata/has_regular",
            "com.google.fonts/check/metadata/regular_is_400",
            "com.google.fonts/check/metadata/nameid/post_script_name",
            "com.google.fonts/check/metadata/nameid/family_and_full_names",
            "com.google.fonts/check/metadata/nameid/copyright",
            # FIXME! The check below (metadata/nameid/font_name) looks
            #        suspiciously similar to the now deprecated
            #          com.google.fonts/check/metadata/nameid/family_name
            #        which is similar to
            #          com.google.fonts/check/metadata/nameid/family_and_full_names
            #
            #        See also: issue #4581
            "com.google.fonts/check/metadata/nameid/font_name",
            "com.google.fonts/check/metadata/match_fullname_postscript",
            "com.google.fonts/check/metadata/match_filename_postscript",
            "com.google.fonts/check/metadata/match_weight_postscript",
            "com.google.fonts/check/metadata/minisite_url",
            "com.google.fonts/check/metadata/valid_full_name_values",
            "com.google.fonts/check/metadata/valid_filename_values",
            "com.google.fonts/check/metadata/valid_post_script_name_values",
            "com.google.fonts/check/metadata/valid_nameid25",
            "com.google.fonts/check/metadata/valid_copyright",
            "com.google.fonts/check/metadata/reserved_font_name",
            "com.google.fonts/check/metadata/copyright_max_length",
            "com.google.fonts/check/metadata/filenames",
            "com.google.fonts/check/metadata/italic_style",
            "com.google.fonts/check/metadata/normal_style",
            "com.google.fonts/check/metadata/match_name_familyname",
            "com.google.fonts/check/metadata/canonical_weight_value",
            "com.google.fonts/check/metadata/os2_weightclass",
            "com.google.fonts/check/metadata/canonical_style_names",
            "com.google.fonts/check/metadata/broken_links",
            "com.google.fonts/check/metadata/undeclared_fonts",
            "com.google.fonts/check/metadata/category",
            "com.google.fonts/check/metadata/gf_axisregistry_valid_tags",
            "com.google.fonts/check/metadata/gf_axisregistry_bounds",
            "com.google.fonts/check/metadata/consistent_axis_enumeration",
            "com.google.fonts/check/metadata/escaped_strings",
            "com.google.fonts/check/metadata/designer_profiles",
            "com.google.fonts/check/metadata/family_directory_name",
            "com.google.fonts/check/metadata/can_render_samples",
            "com.google.fonts/check/metadata/unsupported_subsets",
            "com.google.fonts/check/metadata/unreachable_subsetting",
            "com.google.fonts/check/metadata/category_hints",
            "com.google.fonts/check/metadata/consistent_repo_urls",
            "com.google.fonts/check/metadata/primary_script",
            "com.google.fonts/check/metadata/empty_designer",
            "com.google.fonts/check/metadata/has_tags",
        ],
        "Glyphset Checks": [
            "com.google.fonts/check/glyphsets/shape_languages",
        ],
        "Description Checks": [
            "com.google.fonts/check/description/broken_links",
            "com.google.fonts/check/description/valid_html",
            "com.google.fonts/check/description/min_length",
            "com.google.fonts/check/description/git_url",
            "com.google.fonts/check/description/eof_linebreak",
            "com.google.fonts/check/description/family_update",
            "com.google.fonts/check/description/urls",
            "com.google.fonts/check/description/noto_has_article",
            "com.google.fonts/check/description/has_unsupported_elements",
        ],
        "Family Checks": [
            "com.google.fonts/check/family/equal_codepoint_coverage",
            "com.google.fonts/check/family/has_license",
            "com.google.fonts/check/family/control_chars",
            "com.google.fonts/check/family/tnum_horizontal_metrics",
            "com.google.fonts/check/family/italics_have_roman_counterparts",
        ],
        "Name table checks": [
            "com.google.fonts/check/name/unwanted_chars",
            "com.google.fonts/check/name/license",
            "com.google.fonts/check/name/license_url",
            "com.google.fonts/check/name/family_and_style_max_length",
            "com.google.fonts/check/name/line_breaks",
            "com.google.fonts/check/name/rfn",
            "com.google.fonts/check/name/family_name_compliance",
        ],
        "Repository Checks": [
            "com.google.fonts/check/repo/dirname_matches_nameid_1",
            "com.google.fonts/check/repo/vf_has_static_fonts",
            "com.google.fonts/check/repo/upstream_yaml_has_required_fields",
            "com.google.fonts/check/repo/fb_report",
            "com.google.fonts/check/repo/zip_files",
            "com.google.fonts/check/repo/sample_image",
            "com.google.fonts/check/license/OFL_copyright",
            "com.google.fonts/check/license/OFL_body_text",
        ],
        "Font File Checks": [
            "com.google.fonts/check/glyph_coverage",
            "com.google.fonts/check/canonical_filename",
            "com.google.fonts/check/usweightclass",
            "com.google.fonts/check/fstype",
            "com.google.fonts/check/vendor_id",
            "com.google.fonts/check/ligature_carets",
            "com.google.fonts/check/production_glyphs_similarity",
            # DISABLED: "com.google.fonts/check/production_encoded_glyphs",
            "com.google.fonts/check/glyf_nested_components",
            "com.google.fonts/check/varfont/generate_static",
            "com.google.fonts/check/kerning_for_non_ligated_sequences",
            "com.google.fonts/check/name/description_max_length",
            "com.google.fonts/check/fvar_name_entries",
            "com.google.fonts/check/version_bump",
            "com.google.fonts/check/epar",
            "com.google.fonts/check/font_copyright",
            "com.google.fonts/check/slant_direction",
            "com.google.fonts/check/has_ttfautohint_params",
            "com.google.fonts/check/name/version_format",
            "com.google.fonts/check/name/familyname_first_char",
            "com.google.fonts/check/hinting_impact",
            "com.google.fonts/check/file_size",
            "com.google.fonts/check/varfont/has_HVAR",
            "com.google.fonts/check/font_names",
            "com.google.fonts/check/gasp",
            "com.google.fonts/check/name/mandatory_entries",
            "com.google.fonts/check/name/copyright_length",
            "com.google.fonts/check/fontdata_namecheck",
            "com.google.fonts/check/name/ascii_only_entries",
            "com.google.fonts/check/fvar_instances",
            "com.google.fonts/check/old_ttfautohint",
            "com.google.fonts/check/vttclean",
            "com.google.fonts/check/aat",
            "com.google.fonts/check/smart_dropout",
            "com.google.fonts/check/integer_ppem_if_hinted",
            "com.google.fonts/check/unitsperem_strict",
            "com.google.fonts/check/vertical_metrics",
            "com.google.fonts/check/vertical_metrics_regressions",
            "com.google.fonts/check/cjk_vertical_metrics",
            "com.google.fonts/check/cjk_vertical_metrics_regressions",
            "com.google.fonts/check/cjk_not_enough_glyphs",
            "com.google.fonts/check/varfont_duplicate_instance_names",
            "com.google.fonts/check/varfont/consistent_axes",
            "com.google.fonts/check/varfont/unsupported_axes",
            "com.google.fonts/check/varfont/duplexed_axis_reflow",
            "com.google.fonts/check/gf_axisregistry/fvar_axis_defaults",
            "com.google.fonts/check/STAT/gf_axisregistry",
            "com.google.fonts/check/STAT/axis_order",
            "com.google.fonts/check/mandatory_avar_table",
            "com.google.fonts/check/missing_small_caps_glyphs",
            "com.google.fonts/check/stylisticset_description",
            "com.google.fonts/check/os2/use_typo_metrics",
            "com.google.fonts/check/meta/script_lang_tags",
            "com.google.fonts/check/no_debugging_tables",
            "com.google.fonts/check/render_own_name",
            "com.google.fonts/check/STAT",
            "com.google.fonts/check/colorfont_tables",
            "com.google.fonts/check/color_cpal_brightness",
            "com.google.fonts/check/empty_glyph_on_gid1_for_colrv0",
            "com.google.fonts/check/varfont/bold_wght_coord",
        ],
    },
    "configuration_defaults": {
        "com.google.fonts/check/file_size": {
            "WARN_SIZE": 1 * 1024 * 1024,
            "FAIL_SIZE": 9 * 1024 * 1024,
        }
    },
    "overrides": {
        "com.google.fonts/check/italic_angle": [
            {
                "code": "positive",
                "status": "FAIL",
                "reason": "Google Fonts has different policies on checking for italic angle.",
            },
            {
                "code": "negative",
                "status": "FAIL",
                "reason": "Google Fonts has different policies on checking for italic angle.",
            },
            {
                "code": "over-30-degrees",
                "status": "FAIL",
                "reason": "Google Fonts has different policies on checking for italic angle.",
            },
        ],
        "com.google.fonts/check/italic_axis_in_stat_is_boolean": [
            {
                "code": "wrong-ital-axis-value",
                "status": "FAIL",
                "reason": "For Google Fonts, all messages from this check are considered FAILs",
            },
            {
                "code": "wrong-ital-axis-flag",
                "status": "FAIL",
                "reason": "For Google Fonts, all messages from this check are considered FAILs",
            },
            {
                "code": "wrong-ital-axis-linkedvalue",
                "status": "FAIL",
                "reason": "For Google Fonts, all messages from this check are considered FAILs",
            },
        ],
        "com.google.fonts/check/italic_axis_last": [
            {
                "code": "ital-axis-not-last",
                "status": "FAIL",
                "reason": "For Google Fonts, the 'ital' axis must be last in the axes order.",
            },
        ],
        "com.google.fonts/check/alt_caron": [
            {
                "code": "bad-mark",
                "status": "FAIL",
                "reason": "For Google Fonts, one of the comma-lookalikes is a FAIL",
            },
        ],
    },
}
