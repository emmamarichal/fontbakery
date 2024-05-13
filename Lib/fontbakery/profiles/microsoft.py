PROFILE = {
    "sections": {
        "Metadata Checks": [
            "com.microsoft/check/copyright",
            "com.microsoft/check/version",
            "com.microsoft/check/trademark",
            "com.microsoft/check/manufacturer",
            "com.microsoft/check/vendor_url",
            "com.microsoft/check/license_description",
            "com.microsoft/check/fstype",
        ],
        "Name Checks": [
            "com.microsoft/check/name_id_1",
            "com.microsoft/check/name_id_2",
            "com.microsoft/check/office_ribz_req",
            "com.microsoft/check/typographic_family_name",
            "com.microsoft/check/name_length_req",
        ],
        "Metrics Checks": [
            "com.microsoft/check/vertical_metrics",
        ],
        "Variable Fonts Checks": [
            "com.microsoft/check/STAT_axis_values",
            "com.microsoft/check/STAT_table_eliding_bit",
            "com.microsoft/check/STAT_table_axis_order",
            "com.microsoft/check/fvar_STAT_axis_ranges",
        ],
        "Sanity Checks": [
            "com.microsoft/check/vtt_volt_data",
        ],
        "Glyph Checks": [
            "com.microsoft/check/tnum_glyphs_equal_widths",
        ],
        "Superfamily Checks": [
            "com.google.fonts/check/superfamily/list",
            "com.google.fonts/check/superfamily/vertical_metrics",
        ],
        "Universal Profile Checks": [
            "com.google.fonts/check/alt_caron",
            "com.google.fonts/check/arabic_high_hamza",
            "com.google.fonts/check/arabic_spacing_symbols",
            "com.google.fonts/check/case_mapping",
            "com.google.fonts/check/cjk_chws_feature",
            "com.google.fonts/check/contour_count",
            "com.google.fonts/check/family/single_directory",
            "com.google.fonts/check/family/vertical_metrics",
            "com.google.fonts/check/family/win_ascent_and_descent",
            # "com.google.fonts/check/fontbakery_version",  # We update at our own pace
            "com.adobe.fonts/check/freetype_rasterizer",
            "com.google.fonts/check/gpos7",
            "com.google.fonts/check/interpolation_issues",
            "com.google.fonts/check/legacy_accents",
            "com.google.fonts/check/linegaps",
            "com.google.fonts/check/mandatory_glyphs",
            "com.google.fonts/check/math_signs_width",
            "com.google.fonts/check/name/trailing_spaces",
            "com.google.fonts/check/os2_metrics_match_hhea",
            "com.google.fonts/check/ots",
            "com.google.fonts/check/required_tables",
            "com.google.fonts/check/rupee",
            "com.adobe.fonts/check/sfnt_version",
            "com.google.fonts/check/soft_hyphen",
            # "com.google.fonts/check/STAT_in_statics",  # Difference of opinion
            "com.google.fonts/check/STAT_strings",
            # "com.google.fonts/check/tabular_kerning",  # We have tnum_glyphs_equal_widths
            "com.google.fonts/check/transformed_components",
            "com.google.fonts/check/ttx_roundtrip",
            "com.google.fonts/check/unique_glyphnames",
            "com.google.fonts/check/unreachable_glyphs",
            "com.google.fonts/check/unwanted_tables",
            "com.google.fonts/check/valid_glyphnames",
            "com.google.fonts/check/whitespace_glyphnames",
            "com.google.fonts/check/whitespace_glyphs",
            "com.google.fonts/check/whitespace_ink",
            "com.google.fonts/check/whitespace_widths",
        ],
        "OpenType Specification Checks": [
            "com.google.fonts/check/family/underline_thickness",
            "com.google.fonts/check/family/panose_familytype",
            "com.google.fonts/check/family/equal_font_versions",
            "com.adobe.fonts/check/family/bold_italic_unique_for_nameid1",
            "com.adobe.fonts/check/family/max_4_fonts_per_family_name",
            "com.adobe.fonts/check/family/consistent_family_name",
            "com.adobe.fonts/check/name/postscript_vs_cff",
            "com.adobe.fonts/check/name/postscript_name_consistency",
            "com.adobe.fonts/check/name/empty_records",
            "com.google.fonts/check/name/no_copyright_on_description",
            "com.google.fonts/check/name/match_familyname_fullfont",
            "com.google.fonts/check/varfont/regular_wght_coord",
            "com.google.fonts/check/varfont/regular_wdth_coord",
            "com.google.fonts/check/varfont/regular_slnt_coord",
            "com.google.fonts/check/varfont/regular_ital_coord",
            "com.google.fonts/check/varfont/regular_opsz_coord",
            "com.google.fonts/check/varfont/slnt_range",
            "com.typenetwork/check/varfont/ital_range",
            "com.google.fonts/check/varfont/wght_valid_range",
            "com.google.fonts/check/varfont/wdth_valid_range",
            "com.google.fonts/check/varfont/stat_axis_record_for_each_axis",
            "com.google.fonts/check/loca/maxp_num_glyphs",
            "com.adobe.fonts/check/cff2_call_depth",
            "com.adobe.fonts/check/cff_call_depth",
            "com.adobe.fonts/check/cff_deprecated_operators",
            "com.google.fonts/check/font_version",
            "com.google.fonts/check/post_table_version",
            "com.google.fonts/check/monospace",
            "com.google.fonts/check/xavgcharwidth",
            "com.adobe.fonts/check/fsselection_matches_macstyle",
            "com.google.fonts/check/unitsperem",
            "com.google.fonts/check/dsig",
            "com.google.fonts/check/gdef_spacing_marks",
            "com.google.fonts/check/gdef_mark_chars",
            "com.google.fonts/check/gdef_non_mark_chars",
            "com.google.fonts/check/gpos_kerning_info",
            "com.google.fonts/check/kern_table",
            "com.google.fonts/check/glyf_unused_data",
            "com.google.fonts/check/family_naming_recommendations",
            "com.google.fonts/check/maxadvancewidth",
            "com.adobe.fonts/check/postscript_name",
            "com.google.fonts/check/points_out_of_bounds",
            "com.google.fonts/check/glyf_non_transformed_duplicate_components",
            "com.google.fonts/check/code_pages",
            "com.google.fonts/check/layout_valid_feature_tags",
            "com.google.fonts/check/layout_valid_script_tags",
            "com.google.fonts/check/layout_valid_language_tags",
            "com.google.fonts/check/italic_angle",
            "com.google.fonts/check/mac_style",
            "com.google.fonts/check/fsselection",
            "com.google.fonts/check/name/italic_names",
            "com.adobe.fonts/check/varfont/valid_axis_nameid",
            "com.adobe.fonts/check/varfont/valid_subfamily_nameid",
            "com.adobe.fonts/check/varfont/valid_postscript_nameid",
            "com.adobe.fonts/check/varfont/valid_default_instance_nameids",
            "com.adobe.fonts/check/varfont/same_size_instance_records",
            "com.adobe.fonts/check/varfont/distinct_instance_records",
            "com.adobe.fonts/check/varfont/foundry_defined_tag_name",
            "com.google.fonts/check/varfont/family_axis_ranges",
            "com.adobe.fonts/check/stat_has_axis_value_tables",
            "com.thetypefounders/check/vendor_id",
            "com.google.fonts/check/caret_slope",
            "com.google.fonts/check/italic_axis_in_stat",
            "com.google.fonts/check/italic_axis_in_stat_is_boolean",
            "com.google.fonts/check/italic_axis_last",
        ],
    },
}
