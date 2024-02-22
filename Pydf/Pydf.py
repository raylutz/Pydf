# Pydf.py
"""

# Pydf -- Python Dataframes

The Pydf class provides a lightweight, simple and fast alternative to provide 
2-d data arrays with mixed types.

"""

"""
    MIT License

    Copyright (c) 2024 Ray Lutz

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""


"""
See README file at this location: https://github.com/raylutz/Pydf/blob/main/README.md
"""

"""
    v0.1.X (pending)
            Started creating separate package, moved comment text to README.md
            For apply_formulas(), added relative row and column references $r and $c plus $d to reference the pydf object.
            Changed the result of a row access, such as $d[$r, :$c] to return a list so it could be compatible with sum.
                use pydf.select_irow() to select a row with dict as the result.
    
    v0.2.0  (2024-02-03) 
            Copied related code to Pydf repo and resolved all imports. All tests running.
            Added option of appending a plain list to pydf instance using .append()
            Added 'omit_nulls' option to col(), col_to_la(), icol_to_la(), valuecounts_for_colname()
            Added ability to groupby multiple cols
            in select_records_pydf(self, keys_ls: T_ls, inverse:bool=False), added inverse boolean.
            Started to add selcols for zero-copy support.
            Added _num_cols() 
            Added unit tests.
            Add groupby_cols_reduce() and sum_np()
            Fixed bug in item setter for str row.
            Added demo of making list of file in a folder.
            groupby_cols_reduce() added, unit tests added. Demo added.
            Fix demo to run on windows, mac or linux.
            Add produced test files to gitignore.
            changed _num_cols() to num_cols()
            removed selcols_ls from class. 
            Pulled in from_csv_file()
            Added buff_to_file()
            improved is_d1_in_d2() by using idiom in Python 3.
            moved sanitize_cols to set_cols() method.
                1. read with no headers.
                2. pull off first row using indexing (could add pop_row())
                3. set set_cols with sanitize_cols=True.
            
            tests added
                initialization from dtypes and no cols.
                set_cols()
                set_keyfield()
                pydf_utils.is_d1_in_d2()
                improved set_cols() to test sanitize_cols flag.
                

    TODO
            Refactor get_item and set_item
            
            tests: need to add 
                .len()
                __str__ and __repr__
                .isin <-- keep this?
                calc_cols
                    no hd defined.
                    include_cols > 10
                    exclude_cols > 10
                    exclude_types
                normalize() <-- keep this?
                
                row_idx_of()
                apply_dtypes()
                unflatten_cols()
                unflatten_dirname() <-- remove?
                unflatten_by_dtypes()
                flatten_cols()
                flatten_by_dtypes()
                flatten_dirname() <-- remove?
                cols_to_strbool() <-- remove?
                set_lol()
                from_lod() with empty records_lod
                from_dod()
                from_excel_buff()
                from_csv_buff()
                from_pandas_df()
                from_numpy()
                to_csv_buff()
                to_dod()
                to_pandas_df()
                append()  
                    empty data item
                    simple list with columns defined.
                    no columns defined, just append to lol.
                concat()
                    not other instance
                    empty current pydf
                    self.hd != other_instance.hd
                extend()
                    no input records
                    some records empty
                record_append()
                    empty record
                    overwrite of existing
                remove_key -- keyfield not set.
                get_existing_keys
                select_record_da -- row_idx >= len(self.lol)
                _basic_get_record_da -- no hd, include_cols
                select_records_pydf
                    no keyfield
                    inverse
                        len(keys_ls) > 10 and len(self.kd) > 30
                        smaller cases
                iloc
                    no hd
                select_first_row_by_dict    
                select_where_idxs <-- remove?
                icol_to_la
                    unique
                    omit_nulls
                select_cols
                from_selected_cols <-- remove! but check for usage!
                assign_record_da
                    no keyfield defined.
                update_by_keylist <-- remove?
                insert_icol()
                    keyfield <-- remove!  use set_keyfield instead
                insert_irow()
                insert_col()
                    colname already exists.
                set_col_irows() <-- remove.
                set_icol()  <-- remove.
                set_icol_irows() <-- remove.
                find_replace
                sort_by_colname(
                apply_formulas()
                    no self
                    formula shape differs
                    error in formula
                apply
                    keylist without keyfield
                update_row()
                apply_in_place()
                    keylist without keyfield
                reduce 
                    by == 'col'
                manifest_apply()
                manifest_reduce()
                manifest_process()
                groupby()
                groupby_reduce()
                pydf_valuecount()
                groupsum_pydf()
                set_col2_from_col1_using_regex_select
                    not col2
                apply_to_col
                sum_da 
                    one col
                    cols_list > 10
                count_values_da()
                sum_dodis -- needed?
                valuecounts_for_colname
                    omit_nulls
                valuecounts_for_colnames_ls_selectedby_colname
                    not colnames_ls
                gen_stats_pydf()
                to_md()
                dict_to_md() <-- needed?
                value_counts_pydf()
                
            pydf_utils
                is_linux()
                apply_dtypes_to_hdlol()
                    empty case
                select_col_of_lol_by_col_idx()
                    col_idx out of range.
                unflatten_hdlol_by_cols 
                json_encode
                make_strbool <-- remove?
                test_strbool >-- remove?
                xlsx_to_csv
                add_trailing_columns_csv()
                insert_col_in_lol_at_icol()
                    col_la empty
                insert_row_in_lol_at_irow() unused?
                calc_chunk_sizes
                    not num_items or not max_chunk_size
                sort_lol_by_col
                set_dict_dtypes 
                    various cases
                list_stats
                    REMOVE?
                list_stats_index
                list_stats_attrib
                list_stats_filepaths
                list_stats_scalar
                list_stats_localidx
                is_list_allints
                profile_ls_to_loti
                reduce_lol_cols
                s3path_to_url
                parse_s3path
                transpose_lol
                safe_get_idx
                shorten_str_keeping_ends
                safe_max
                smart_fmt
                str2bool
                safe_del_key
                dod_to_lod
                lod_to_dod
                safe_eval
                safe_min
                safe_stdev
                safe_mean
                sts
                split_dups_list
                clean_numeric_str
                is_numeric
            pydf_indexing
                many cases
            pydf_md
                not tested at all.
                
"""            
    
    
#VERSION  = 'v0.1.X'
#VERSDATE = '2024-01-21'  

import sys
import io
import csv
import copy
import re
import numpy as np
    
sys.path.append('..')

from Pydf.pydf_types import T_ls, T_lola, T_di, T_hllola, T_loda, T_da, T_li, T_dtype_dict, \
                            T_dola, T_dodi, T_la, T_lota, T_doda, T_buff, T_df, T_ds, T_lb
                     
import Pydf.pydf_utils as utils
import Pydf.pydf_md    as md
import Pydf.pydf_indexing as indexing

from typing import List, Dict, Any, Tuple, Optional, Union, cast, Type, Callable #
def fake_function(a: Optional[List[Dict[str, Tuple[int,Union[Any, str]]]]] = None) -> Optional[int]:
    return None or cast(int, 0)       # pragma: no cover

T_Pydf = Type['Pydf']



class Pydf:

    """ my_pydf = Pydf() """

    def __init__(self, 
            lol:        Optional[T_lola]        = None,     # Optional List[List[Any]] to initialize the data array. 
            cols:       Optional[T_ls]          = None,     # Optional column names to use.
            dtypes:     Optional[T_dtype_dict]  = None,     # Optional dtype_dict describing the desired type of each column.
                                                            #   also used to define column names if provided and cols not provided.
            keyfield:   str                     = '',       # A field of the columns to be used as a key.
            name:       str                     = '',       # An optional name of the Pydf array.
            use_copy:   bool                    = False,    # If True, make a deep copy of the lol data.
            disp_cols:  Optional[T_ls]          = None,     # Optional list of strings to use for display, if initialized.
            #sanitize_cols: bool                 = False,    # check for blank or missing cols and make complete and unique.
        ):
        if lol is None:
            lol = []
        if dtypes is None:
            dtypes = {}
        if cols is None:
            cols = []
            
        self.name           = name              # str
        self.keyfield       = keyfield          # str
        self.hd             = {}                # hd_di
        
        if use_copy:
            self.lol        = copy.deepcopy(lol)
        else:
            self.lol        = lol
        
        self.kd             = {}
        self.dtypes         = dtypes
        
        self.md_max_rows    = 10    # default number of rows when used with __repr__ and __str__
        self.md_max_cols    = 10    # default number of cols when used with __repr__ and __str__

        # Initialize iterator variables        
        self._iter_index = 0

        if not cols:
            if dtypes:
                self.hd = {col: idx for idx, col in enumerate(dtypes.keys())}
        # elif sanitize_cols:        
                # # make sure there are no blanks and columns are unique.
                # # this does column renaming, and builds hd
                # # Note: This is time consuming and should only be done when required!
                # cols = self.__class__.sanitize_colnames(colnames=cols)
        else:
            self._cols_to_hd(cols)
            if len(cols) != len(self.hd):
                raise AttributeError ("AttributeError: cols not unique")
            
        if self.hd and dtypes:
            effective_dtypes = {col: dtypes.get(col, str) for col in self.hd}
        
            # setting dtypes may be better done manually if required.
            if self.num_cols():

                self.lol = utils.apply_dtypes_to_hdlol((self.hd, self.lol), effective_dtypes)[1]
            
        # rebuild kd if possible.
        self._rebuild_kd()
        
            
    #===========================
    # basic attributes and methods

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self) -> Dict[str, int]:
        if self._iter_index < len(self.lol):
            row_dict = dict(zip(self.hd.keys(), self.lol[self._iter_index]))
            self._iter_index += 1
            return row_dict
        else:
            self._iter_index = 0
            raise StopIteration

    def __bool__(self):
        """ test pydf for existance and not empty 
            test exists in test_pydf.py            
        """
        return bool(self.num_cols())


    def __len__(self):
        """ Return the number of rows in the Pydf instance.
            test exists in test_pydf.py            
        """
        return len(self.lol)
        
        
    def len(self):
        return len(self.lol)
        
        
    def shape(self):
        """ return the number of rows and cols in the pydf data array
            number of columns is based on the first record
        """
        # test exists in test_pydf.py
        
        if not len(self): return (0, 0)
        
        return (len(self.lol), self.num_cols()) 
        
        
    def __eq__(self, other):
        # test exists in test_pydf.py            

        if not isinstance(other, Pydf):
            return False

        return (self.lol == other.lol and self.columns() == other.columns() and self.keyfield == other.keyfield)

    
    def __str__(self) -> str:
        return self.md_pydf_table_snippet()
        
        
    def __repr__(self) -> str:
        return "\n"+self.md_pydf_table_snippet()
    

    def num_cols(self) -> int:
        """ return 0 if self.lol is empty.
            return the length of the first row otherwise.
            
            this only works well if the array has rows that are all the same length.            
        """
    
        if not self.lol:
            return 0
        return len(self.lol[0])
        

    #===========================
    # column names
    def columns(self):
        """ Return the column names 
        """
        # test exists in test_pydf.py            
        return list(self.hd.keys())
        
        
    def _cols_to_hd(self, cols: T_ls):
        """ rebuild internal hd from cols provided """
        self.hd = {col:idx for idx, col in enumerate(cols)}
        
        
    @staticmethod
    def isin(listlike1: Union[T_da, T_la], listlike2: Union[T_da, T_la]) -> T_lb:
        """ creates a boolean mask (list of bools) for each item in list1 which is in list2
        
            this can be used particularly for omitting columns, like:
            
                my_pydf[:, ~my_pydf.columns().isin(colnames_to_omit_list)]
            
            can also be used to select columns
            
                my_pydf[:, my_pydf.columns().isin(colnames_to_keep_list)]

            but this is easier done by providing the list directly
            
                my_pydf[:, colnames_to_keep_list]

            as long as the colnames are not numbers, because then the indexing will 
            assume they are column numbers. So this can be a workaround if the colnames
            are numbers and using them directly can be confusing, but mainly it is used
            to exclude columns. Can be also used for rows, but it is best to use 
            direct selection if possible.
            
            This will directly select rows with the keys selected.
            
                my_pydf[rowkeys_to_keep_list]
                
            But can also select with a boolean mask, but it is not as efficient.
            
                my_pydf[my_pydf.keys().isin(rowkeys_to_keep_list)]
                
            However, that may be good if you just want to exclude rows
            
                my_pydf[~my_pydf.keys().isin(rowkeys_to_keep_list)]
        
        """
        if isinstance(listlike2, list) and len(listlike1) > 10 and len(listlike2) > 30:
            searchable2 = dict.fromkeys(listlike2)
        else:
            searchable2 = listlike2
        
        bool_mask_lb = [col in searchable2 for col in listlike1]
        
        return bool_mask_lb
                

    def calc_cols(self, 
            include_cols: Optional[T_la]=None,
            exclude_cols: Optional[T_la]=None,
            include_types: Optional[List[Type]]=None,
            exclude_types: Optional[List[Type]]=None,
           ) -> T_la:
        """ this method helps to calculate the columns to be specified for a apply or reduce operation.
            Can use any combination of listing columns to be included, or excluded by name,
                or included by type.
            If using a groupby function, the cols spec should not include the groupby column(s)
        """
            
            
        # start with all cols.
        selected_cols = list(self.hd.keys())
        if not selected_cols:
            return []
            
        if include_cols:
            if len(include_cols) > 10:
                include_cols_dict = dict.fromkeys(include_cols)
                selected_cols = [col for col in selected_cols if col in include_cols_dict]
            else:
                selected_cols = [col for col in selected_cols if col in include_cols]

        if exclude_cols:
            if len(exclude_cols) > 10:
                exclude_cols_dict = dict.fromkeys(exclude_cols)
                selected_cols = [col for col in selected_cols if col not in exclude_cols_dict]
            else:
                selected_cols = [col for col in selected_cols if col not in exclude_cols]

        if include_types and self.dtypes:
            if not isinstance(include_types, list):
                include_types = [include_types]
            selected_cols = [col for col in selected_cols if self.dtypes.get(col) in include_types]

        if exclude_types and self.dtypes:
            if not isinstance(exclude_types, list):
                exclude_types = [exclude_types]
            selected_cols = [col for col in selected_cols if self.dtypes.get(col) not in exclude_types]

        return selected_cols
        
        
    def normalize(self, defined_cols: T_ls):
        # add or subtract columns and place in order per defined_cols.
        if not self:
            return
        
        # from utilities import utils

        for irow, da in enumerate(self):
            record_da = utils.set_cols_da(da, defined_cols)
            self.update_record_da_irow(irow, record_da)
            
        return self
        

    @staticmethod
    def _calculate_single_column_name(index: int) -> str:
        """ provide the spreadsheet-style column name for integer offset.
        """
        
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ''
        
        while index >= 0:
            index, remainder = divmod(index, 26)
            result = letters[remainder] + result
            index -= 1
    
        return result
        
    
    @staticmethod
    def _generate_spreadsheet_column_names_list(num_cols: int) -> T_ls:
        """ generate a full list of column names for the num_columns specified 
        """
    
        return [Pydf._calculate_single_column_name(i) for i in range(num_cols)]


    def rename_cols(self, from_to_dict: T_ds):
        """ rename columns using the from_to_dict provided. 
            respects dtypes and rebuilds hd
        """
        # unit tests exist
        
        self.hd     = {from_to_dict.get(col, col):idx for idx, col in enumerate(self.hd.keys())}
        self.dtypes = {from_to_dict.get(col, col):typ for col, typ in self.dtypes.items()}
        if self.keyfield:
            self.keyfield = from_to_dict.get(self.keyfield, self.keyfield)
            # no need to rebuild the kd, it should be the same.
            
        return self

    @staticmethod
    def _sanitize_cols(cols: T_ls, unnamed_prefix='col') -> str:
        """ make sure there are no blanks and columns are unique.
            if missing, substitute with {unnamed_prefix}{col_idx}
            if duplicated, substitute with prior_name_{col_idx}
        """
        
        if cols:
            # first make sure all columns have names.
            try:
                cols = [col if col else f"{unnamed_prefix}{idx}" for idx, col in enumerate(cols)] 
            except Exception as err:
                print(f"{err}")
                import pdb; pdb.set_trace() #temp
                pass
                
            # next make sure they are all unique    
            col_hd = {}
            for idx, col in enumerate(cols):
                if col not in col_hd:
                    col_hd[col] = idx
                else:
                    # if not unique, add _NNN after the name.
                    col_hd[f"{col}_{idx}"] = idx
            return list(col_hd.keys())
            
            
    def set_cols(self, new_cols: Optional[T_ls]=None, sanitize_cols: bool=True, unnamed_prefix: str='col'):
        """ set the column names of the pydf using an ordered list.
        
            if new_cols is None, then we generate spreadsheet colnames like A, B, C... AA, AB, ...
            
            if sanitize_cols is True (default) then check new_cols for any missing or duplicate names.
                if missing, substitute with {unnamed_prefix}{col_idx}
                if duplicated, substitute with prior_name_{col_idx}
        """
        num_cols = self.num_cols() or len(self.hd)
        
        if new_cols is None:
            new_cols = self.__class__._generate_spreadsheet_column_names_list(num_cols)
            
        elif sanitize_cols:
            new_cols = self.__class__._sanitize_cols(new_cols, unnamed_prefix=unnamed_prefix)
        
        if num_cols and len(new_cols) < num_cols:
            raise AttributeError("Length of new_cols not the same as existing cols")
        
        if self.keyfield and self.hd:
            # if column names are already defined (hd) then we need to repair the keyfield.
            keyfield_idx = self.hd[self.keyfield]
            self.keyfield = new_cols[keyfield_idx]
        
        # set new cols to the hd
        self._cols_to_hd(new_cols)
        
        # convert dtypes dict to use the new names.
        if self.dtypes:
            self.dtypes = dict(zip(new_cols, self.dtypes.values()))
            
        return self
            

    #===========================
    # keyfield
        
    def keys(self):
        """ return list of keys from kd of keyfield
            test exists in test_pydf.py            
        """
        
        if not self.keyfield:
            return []
        
        return list(self.kd.keys())

    def set_keyfield(self, keyfield: str=''):
        """ set the indexing keyfield to a new column
            if keyfield == '', then reset the keyfield and reset the kd.
            if keyfield not in columns, then KeyError
        """
        if keyfield:
            if keyfield not in self.hd:
                raise KeyError
            self.keyfield = keyfield
            self._rebuild_kd()
        else:
            self.keyfield = ''
            self.kd = {}
            
        return self
    
        
    def _rebuild_kd(self) -> None:
        """ anytime deletions are performed, the kd must be rebuilt 
            if the keyfield is set.
        """
        
        if self.keyfield and self.keyfield in self.hd:
            col_idx = self.hd[self.keyfield]
            self.kd = self.__class__._build_kd(col_idx, self.lol)
            
        return self


    @staticmethod
    def _build_kd(col_idx: int, lol: T_lola) -> T_di:
        """ build key dictionary from col_idx col of lol """
        
        # from utilities import utils

        key_col = utils.select_col_of_lol_by_col_idx(lol, col_idx)
        kd = {key: index for index, key in enumerate(key_col)}
        return kd
        
        
    def row_idx_of(self, rowkey: str) -> int:
        """ return row_idx of key provided or -1 if not able to do it.
        """
        if not self.keyfield or not self.kd:
            return -1
        return self.kd.get(rowkey, -1)
        

    
    #===========================
    # dtypes
    
    def apply_dtypes(self):
        """ convert columns to the datatypes specified in self.dtypes dict """
        
        self.lol = utils.apply_dtypes_to_hdlol((self.hd, self.lol), self.dtypes)[1]
            
        return self
        
        
    def unflatten_cols(self, cols: T_ls):
        """ 
            given a pydf and list of cols, 
            convert cols named to either list or dict if col exists and it appears to be 
                stringified using f"{}" functionality.
                
        """

        if not self:
            return    
            
        # from utilities import utils

        self.hd, self.lol = utils.unflatten_hdlol_by_cols((self.hd, self.lol), cols)    
            
        return self


    def unflatten_dirname(self, dirname: str):

        if not self:
            return self
        
        from models.BIF import BIF

        cols = BIF.get_dirname_cols_with_format(dirname=dirname, fmt='json')
        if not cols:
            return self
        
        self.unflatten_cols(cols)
            
        return self
        
        
    def unflatten_by_dtypes(self):

        if not self or not self.dtypes:
            return self
                
        unflatten_cols = self.calc_cols(include_types = [list, dict])
        
        if not unflatten_cols:
            return self
       
        self.unflatten_cols(unflatten_cols)
            
        return self
        
        
    def flatten_cols(self, cols: T_ls):
        # given a pydf, convert given list of columns to json.

        if not self:
            return self
        
        # from utilities import utils

        for irow, da in enumerate(self):
            record_da = copy.deepcopy(da)
            for col in cols:
                if col in da:
                    record_da[col] = utils.json_encode(record_da[col])        
            self.update_record_da_irow(irow, record_da)        
            
        return self
    
    
    def flatten_by_dtypes(self):

        if not self or not self.dtypes:
            return self
                
        flatten_cols = self.calc_cols(include_types = [list, dict])
        
        if not flatten_cols:
            return self
       
        self.flatten_cols(cols=flatten_cols)
            
        return self


    def flatten_dirname(self, dirname: str):

        if not self:
            return self
            
        # change True/False to '1'/'0' strings.
        from models.BIF import BIF

        strbool_cols = BIF.get_dirname_cols_with_format(dirname=dirname, fmt='strbool')
        self.cols_to_strbool(strbool_cols)
        
        # make sure the df has all the columns and no extra columns.
        self.normalize(defined_cols=BIF.get_dirname_columns(dirname))
        
        # convert objects marked with format 'json' to json strings.
        json_cols = BIF.get_dirname_cols_with_format(dirname=dirname, fmt='json')
        self.flatten_cols(cols=json_cols)
            
        return self
        

    def cols_to_strbool(self, cols: T_ls):
        # given a lod, convert given list of columns to strbool.

        # from utilities import utils

        for irow, da in enumerate(self):
            record_da = {k:utils.make_strbool(da[k]) for k in cols if k in da}
            self.update_record_da_irow(irow, record_da)        
            
        return self


    def _safe_tofloat(val: Any) -> Union[float, str]:
        try:
            return float(val)
        except ValueError:
            return 0.0
    
    #===========================
    # indexing

    def __getitem__(self, slice_spec:   Union[slice, int, str, T_li, T_ls, T_lb, 
                                Tuple[  Union[slice, int, str, T_li, T_ls, T_lb], 
                                        Union[slice, int, str, T_li, T_ls, T_lb]]]) -> 'Pydf':
        
        """ allow selection and slicing using one or two specs:
        
            my_pydf[2, 3]         -- select cell at row 2, col 3 and return value.
            my_pydf[2]            -- select row 2, including all columns, return as a list.
            my_pydf[2, :]         -- same as above
            my_pydf[[2], :]       -- same as above
            my_pydf[[2,5,8]]      -- select rows 2, 5, and 8, including all columns
            my_pydf[[2,5,8], :]   -- same as above.
            my_pydf[:, 3]         -- select only column 3, including all rows. Return as a list.
            my_pydf[:, 'C']       -- select only column named 'C', including all rows, return as a list.
            my_pydf[:, ['C']]     -- same as above
            my_pydf[:, [1,4,7]]   -- select columns 1,4, and 7, including all rows. Return as a pydf
            my_pydf[:, ['C','F']] -- select columns 'C' and 'F' including all rows. Return as a pydf
            my_pydf[[2,5,8], [1,4,7]]     -- select rows 2, 5, and 8, including columns 1,4, and 7.
            my_pydf[[2,5,8], ['C','F']]   -- select rows 2, 5, and 8, including columns 'C' and 'F'
            
            my_pydf[2:4]          -- select rows 2 and 3, including all columns, return as pydf.
            my_pydf[2:4, :]       -- same as above
            my_pydf[:, 3:5]       -- select columns 3 and 4, including all rows, return as pydf.
            
            new row selection using keys:
            my_pydf['row1']       -- select entire row with keyfield 'row1'.
                                        Note this differs from Pandas operation.
            my_pydf['row1','C']   -- select cell at row with keyfield 'row1' at colname 'C'
                                        Similar to dict-of-dict selection dod['row1']['C']
            my_pydf[my_pydf.rowidxof('row1'):my_pydf.rowidxof('row8')] -- select rows including 'row1' upto but not including 'row8' (7 rows)
            my_pydf[['row1', 'row5, 'row8']]                -- select three rows by list of keyfield names.
            my_pydf['row1':'row8', ['C','F']]               -- NOT SUPPORTED YET select rows including 'row1' upto but not including 'row8' (7 rows) in columns 'C' and 'F'
            my_pydf[['row1', 'row5, 'row8'], ['C','F']]     -- select three rows by list of keyfield names and two columns, by name.
            
            my_pydf[:, my_pydf.columns().isin(['C', 'F'])]  -- select just columns 'C' and 'F' by name using boolean mask method.
            my_pydf[:, ~my_pydf.columns().isin(['C', 'F'])]  -- omit columns 'C' and 'F' by name using boolean mask method.
        
            returns a consistent pydf instance copied from the original, and with the data specified.
            always returns the simplest object possible.
            if multiple rows or columns are specified, they will be returned in the original orientation.
            if only one cell is selected, return a single value.
            If only one row is selected, return a list. If a dict is required, use select_irow()
            if only one col is selected, return a list.
        """
        return_val = indexing._get_item(self, slice_spec)
        
        return return_val
        
        
    def __setitem__(self, 
            slice_spec: Union[int, Tuple[Union[slice, int, List[str], List[bool]], Union[slice, int, str, List[str], List[bool]]]], 
            value: Any):
        """
        Handles the assignment of values, lists or dicts to Pydf elements.
        
        Can handle the following scenarios:
            my_pydf[3] = list                   -- assign the entire row at index 3 to the list provided
            my_pydf[[3]] = list                 -- same as above
            my_pydf[3, :] = list                -- same as above.
            my_pydf[[3], :] = list              -- same as above.
            my_pydf[3, :] = dict                -- assign the entire row at index 3 to the dict provided, respecting dict keys.
                                                    will only assign those values that have a new value in the provided dict.
            my_pydf[3] = value                  -- assign the entire row at index 3 to the value provided.
            my_pydf[[3]] = value                -- same as above.
            my_pydf[3, :] = value               -- same as above.
            my_pydf[[3], :] = value             -- same as above.
            my_pydf[[3, 5, 8], :] = value       -- set rows 3, 5 and 8 to the value in all columns
            my_pydf[3, 4] = value               -- set one cell 3, 4 to value
            my_pydf[3, 5:20] = value            -- set a single value in row 3, columns 5 through 19
            my_pydf[3, 5:20] = list             -- set row 3 in columns 5 through 19 to values from the the list provided.
            my_pydf[3, [1,4,7]] = list          -- set row 3 in columns 1, 4, and 7 to values from the the list provided.
            my_pydf[:, 4] = list                -- assign the entire column at index 4 to the list provided.
            my_pydf[3:5, 5] = list              -- assign a partial column at index 5 at rows 3 and 4 to the list provided.

            my_pydf[3, 'C'] = value             -- set a value in cell 3, col 'C'
            my_pydf[3, ['C', 'D', 'G'] = list   -- set a row 3 in columns 'C', 'D' and 'G' to the values in list.
            my_pydf[:, 'C'] = list              -- assign the entire column 'C' to the list provided
            my_pydf[3:5, 'C'] = list            -- assign a partial column 'C' to list provided in rows 3 and 4
            my_pydf[:, 4] = value               -- assign the entire column 4 to the value provided.
            
            my_pydf[[3,5,8], :] = pydf          -- set rows 3,5,8 to the data in pydf provided
            my_pydf[[3,5,8], ['C', 'D', 'G']] = pydf   -- set rows 3,5,8 in columns 'C', 'D' and 'G' to the data in pydf provided
            my_pydf['R1']                       -- choose entire row by name
            my_pydf['R1', :]                    -- choose entire row by name
            my_pydf[['R1', 'R2', 'R3']]         -- choose three rows
            my_pydf[['R1', 'R2', 'R3'], :]      -- choose three rows

        Args:
        - slice_spec: The slice_spec (index or slice) indicating the location to assign the value.
        - value: The value to assign.

        Returns:
        - None
        """

        return indexing._set_item(self, slice_spec, value)
        

    #===========================
    # initializers
    
    def clone_empty(self, lol: Optional[T_lola]=None, cols: Optional[T_ls]=None) -> 'Pydf':
        """ Create Pydf instance from pydf, adopting dict keys as column names
            adopts keyfield but does not adopt kd.
            test exists in test_pydf.py
            if lol is provided, it is used in the new Pydf.
         """
        if self is None:
            return Pydf()
            
        new_cols = cols if cols else self.columns()
        
        new_pydf = Pydf(cols=new_cols, lol=lol, keyfield=self.keyfield, dtypes=copy.deepcopy(self.dtypes))
        
        return new_pydf
        
        
    def set_lol(self, new_lol: T_lola) -> 'Pydf':
        """ set the lol with the value passed, leaving other settings, but recalculating kd. 
        """
        
        self.lol = new_lol
        self._rebuild_kd()
        
        return self
        

    #===========================
    # convert from / to other data or files.
    
    # ==== Python lod (list of dictionaries)
    @staticmethod
    def from_lod(
            records_lod:    T_loda,                         # List[List[Any]] to initialize the lol data array.
            keyfield:       str='',                         # set a new keyfield or set no keyfield.
            dtypes:         Optional[T_dtype_dict]=None     # set the data types for each column.
            ) -> 'Pydf':
        """ Create Pydf instance from loda type, adopting dict keys as column names
            Generally, all dicts in records_lod should be the same OR the first one must have all keys
                and others can be missing keys.
        
            test exists in test_pydf.py
            
            my_pydf = Pydf.from_lod(sample_lod)
        """
        if dtypes is None:
            dtypes = {}
        
        if not records_lod:
            return Pydf(keyfield=keyfield, dtypes=dtypes)
        
        cols = list(records_lod[0].keys())
        
        # from utilities import utils
        
        lol = [list(utils.set_cols_da(record_da, cols).values()) for record_da in records_lod]
        
        return Pydf(cols=cols, lol=lol, keyfield=keyfield, dtypes=dtypes)
        
        
    def to_lod(self) -> T_loda:
        """ Create lod from pydf
            test exists in test_pydf.py
        """
        
        if not self:
            return []

        cols = self.columns()
        result_lod = [dict(zip(cols, la)) for la in self.lol]
        return result_lod
        
    
    # ==== Python dod (dict of dict)    
    @staticmethod
    def from_dod(
            dod:            T_doda,         # Dict(str, Dict(str, Any))
            keyfield:       str='rowkey',   # The keyfield will be set to the keys of the outer dict.
                                            # this will set the preferred name. Defaults to 'rowkey'
            dtypes:         Optional[T_dtype_dict]=None     # optionally set the data types for each column.
            ) -> 'Pydf':
        """ a dict of dict (dod) structure is very similar to a Pydf table, but there is a slight difference.
            A dod structure will have a first key which indexes to a specific dict.
            The key in that dict is likely not also found in the "value" dict of the first level, but it might be.
            
            a Pydf table always has the keys of the outer dict as items in each table.
            Thus dod1 = {'row_0': {'rowkey': 'row_0', 'data1': 1, 'data2': 2, ... },
                         'row_1': {'rowkey': 'row_1', 'data1': 11, ... },
                         ...
                         }
            is fully compatible because it has a first item which is the rowkey.
            If a dod is passed that does not have this column, then it will be created.
            The 'keyfield' parameter should be set to the name of this column.
            
            A typical dod does not have the row key as part of the data in each row, such as:
            
             dod2 = {'row_0': {'data1': 1, 'data2': 2, ... },
                     'row_1': {'data1': 11, ... },
                     ...
                    }
            
            If dod2 is passed, it will be convered to dod1 and then converted to pydf instance.
            
            A Pydf table is able 1/3 the size of an equivalent dod. because the column keys are not repeated.
            
            use to_dod() to recover the original form by setting 'remove_rowkeys'=True if the row keys are
            not required in the dod.
            
        """
        return Pydf.from_lod(utils.dod_to_lod(dod, keyfield=keyfield), dtypes=dtypes)
    
    
    def to_dod(
            self,
            dod:                T_doda,         # Dict(str, Dict(str, Any))
            remove_keyfield:    bool=True,      # by default, the keyfield column is removed.
            ) -> T_doda:
        """ a dict of dict structure is very similar to a Pydf table, but there is a slight difference.
            a Pydf table always has the keys of the outer dict as items in each table.
            Thus dod1 = {'row_0': {'rowkey': 'row_0', 'data1': 1, 'data2': 2, ... },
                         'row_1': {'rowkey': 'row_1', 'data1': 11, ... },
                         ...
                         }
            If a dod is passed that does not have this column, then it will be created.
            The 'keyfield' parameter should be set to the name of this column.
            
            A typical dod does not have the row key as part of the data in each row, such as:
            
             dod2 = {'row_0': {'data1': 1, 'data2': 2, ... },
                     'row_1': {'data1': 11, ... },
                     ...
                    }
            
            If remove_keyfield=True (default) dod2 will be produced, else dod1.
                        
        """
        return utils.lod_to_dod(self.to_lod(), keyfield=self.keyfield, remove_keyfield=remove_keyfield)
    

    # ==== cols_dol
    @staticmethod
    def from_cols_dol(cols_dol: T_dola, keyfield: str='', dtypes: Optional[T_dtype_dict]=None) -> 'Pydf':
        """ Create Pydf instance from cols_dol type, adopting dict keys as column names
            and creating columns from each value (list)
            
            my_pydf = Pydf.from_cols_dol({'A': [1,2,3], 'B': [4,5,6], 'C': [7,8,9])
            
            produces:
                my_pydf.columns() == ['A', 'B', 'C']
                my_pydf.lol == [[1,4,7], [2,5,8], [3,6,9]] 
            
            
        """
        if dtypes is None:
            dtypes = {}
        
        if not cols_dol:
            return Pydf(keyfield=keyfield, dtypes=dtypes)
        
        cols = list(cols_dol.keys())
        
        lol = []
        for irow in range(len(cols_dol[cols[0]])):
            row = []
            for col in cols:
                row.append(cols_dol[col][irow])
            lol.append(row)    
        
        return Pydf(cols=cols, lol=lol, keyfield=keyfield, dtypes=dtypes)
        
        
    def to_cols_dol(self) -> dict:
        """ convert pydf to dictionary of lists of values, where key is the 
            column name, and the list are the values in that column.
        """
        pass
        

    def to_attrib_dict(self) -> dict:
        """
        Convert Pydf instance to a dictionary representation.
        The dictionary has two keys: 'cols' and 'lol'.
        
        DEPRECATED

        Example:
        {
            'cols': ['A', 'B', 'C'],
            'lol': [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        }
        """
        return {'cols': self.columns(), 'lol': self.lol}

    

    @staticmethod
    def from_lod_to_cols(lod: T_loda, cols:Optional[List]=None, keyfield: str='', dtypes: Optional[T_dtype_dict]=None) -> 'Pydf':
        r""" Create Pydf instance from a list of dictionaries to be placed in columns
            where each column shares the same keys in the first column of the array.
            This transposes the data from rows to columns and adds the new 'cols' header,
            while adopting the keys as the keyfield. dtypes is applied to the columns
            transposition and then to the rows.
            
            If no 'cols' parameter is provided, then it will be the name 'key' 
            followed by normal spreadsheet column names, like 'A', 'B', ... 
            
            Creates a pydf where the first column are the keys from the dicts,
            and each subsequent column are each of the values of the dicts.
            
            my_pydf = Pydf.from_coldicts_lod( 
                cols = ['Feature', 'Try 1', 'Try 2', 'Try 3'],
                lod =       [{'A': 1, 'B': 2, 'C': 3},          # data for Try 1
                             {'A': 4, 'B': 5, 'C': 6},          # data for Try 2
                             {'A': 7, 'B': 8, 'C': 9} ]         # data for Try 3
            
            produces:
                my_pydf.columns() == ['Feature', 'Try 1', 'Try 2', 'Try 3']
                my_pydf.lol ==        [['A',       1,       4,       7], 
                                             ['B',       2,       5,       8], 
                                             ['C',       3,       6,       9]] 
            
            This format is useful for producing reports of several tries 
            with different values for the same attributes placed in columns,
            particularly when there are many features that need to be compared.
            Columns are defined directly from cols parameter.
            
        """
        if dtypes is None:
            dtypes = {}
            
        if cols is None:
            cols = []
        
        if not lod:
            return Pydf(keyfield=keyfield, dtypes=dtypes, cols=cols)
        
        # the following will adopt the dictionary keys as cols.
        # note that dtypes applies to the columns in this orientation.
        rows_pydf = Pydf.from_lod(lod, dtypes=dtypes)
        
        # this transposes the entire dataframe, including the column names, which become the first column
        # in the new orientation, then adds the new column names, if provided. Otherwise they will be
        # defined as ['key', 'A', 'B', ...]
        cols_pydf = rows_pydf.transpose(new_keyfield = keyfield, new_cols = cols, include_header = True)
        
        return cols_pydf


    #==== Excel
    @staticmethod
    def from_excel_buff(
            excel_buff: bytes, 
            keyfield: str='',                       # field to use as unique key, if not ''
            dtypes: Optional[T_dtype_dict]=None,    # dictionary of types to apply if set.
            noheader: bool=False,                   # if True, do not try to initialize columns in header dict.
            user_format: bool=False,                # if True, preprocess the file and omit comment lines.
            unflatten: bool=True,                   # unflatten fields that are defined as dict or list.
            ) -> 'Pydf':
        """ read excel file from a buffer and convert to pydf.
        """
        
        # from utilities import xlsx_utils

        csv_buff = utils.xlsx_to_csv(excel_buff)

        my_pydf  = Pydf.from_csv_buff(
                        csv_buff, 
                        keyfield    = keyfield,         # field to use as unique key, if not ''
                        dtypes      = dtypes,           # dictionary of types to apply if set.
                        noheader    = noheader,         # if True, do not try to initialize columns in header dict.
                        user_format = user_format,      # if True, preprocess the file and omit comment lines.
                        unflatten   = unflatten,        # unflatten fields that are defined as dict or list.
                        )
        
        return my_pydf
    
    #==== CSV
    @staticmethod
    def from_csv_buff(
            csv_buff: Union[bytes, str],            # The CSV data as bytes or string.
            keyfield: str='',                       # field to use as unique key, if not ''
            dtypes: Optional[T_dtype_dict]=None,    # dictionary of types to apply if set.
            noheader: bool=False,                   # if True, do not try to initialize columns in header dict.
            user_format: bool=False,                # if True, preprocess the file and omit comment lines.
            sep: str=',',                           # field separator.
            unflatten: bool=True,                   # unflatten fields that are defined as dict or list.
            include_cols: Optional[T_ls]=None,      # include only the columns specified. noheader must be false.
            ) -> 'Pydf':
        """
        Convert CSV data in a buffer (bytes or string) to a pydf object

        Args:
            buff (Union[bytes, str]): 
            keyfield: field to use as unique key, if not ''
            dtypes: dictionary of types to apply if set.
            noheader: do not initialize columns from the first (non-comment) line.
            user_format (bool): Whether to preprocess the CSV data (remove comments and blank lines).
            sep (str): The separator used in the CSV data.

        Returns:
            hllola: A tuple containing a header list and a list of lists representing the CSV data.
        """
        
        from models.DB import DB
    
        data_lol = DB.buff_csv_to_lol(csv_buff, user_format=user_format, sep=sep, include_cols=include_cols, dtypes=dtypes)
        
        cols = []
        if not noheader:
            cols = data_lol.pop(0)        # return the first item and shorten the list.
        
        my_pydf = Pydf(lol=data_lol, cols=cols, keyfield=keyfield, dtypes=dtypes)
        
        if unflatten:
            my_pydf.unflatten_by_dtypes()
   
        return my_pydf
    


    def to_csv_file(
            self,
            file_path: str='',
            line_terminator: Optional[str]=None,
            include_header: bool=True,
            ) -> str:

        buff = self.to_csv_buff(
                line_terminator=line_terminator,
                include_header=include_header,
                )

        self.__class__.buff_to_file(buff, file_path=file_path)
        
        return file_path


    def to_csv_buff(
            self, 
            line_terminator: Optional[str]=None,
            include_header: bool=True,
            ) -> T_buff:
        """ this function writes the pydf array to a csv buffer, including the header if include_header==True.
            The buffer can be saved to a local file or uploaded to a storage service like s3.
        """
    
        if not self:
            return ''
        
        if line_terminator is None:
            line_terminator = '\r\n'
    
        f = io.StringIO(newline = '')           # Use newline='' to ensure consistent line endings
        
        csv_writer = csv.writer(f, lineterminator=line_terminator)
        if include_header:
            csv_writer.writerow(self.columns())     # Write the header row
        csv_writer.writerows(self.lol)          # Write the data rows

        buff = f.getvalue()
        f.close()

        return buff   


    @staticmethod
    def buff_to_file(buff: T_buff, file_path: str):
    
        return utils.write_buff_to_fp(buff, file_path)

    
    #==== Pandas
    @staticmethod
    def from_pandas_df(df: T_df, keyfield:str='', name:str='', use_csv:bool=False, dtypes: Optional[T_dtype_dict]=None) -> 'Pydf':
        """
        Convert a Pandas dataframe to pydf object
        """
        import pandas as pd     # type: ignore
        
        if not use_csv:
    
            if isinstance(df, pd.Series):
                rowdict = df.to_dict()
                cols = list(rowdict.keys())
                lol = [list(rowdict.values())]
            else:
                cols = list(df.columns)
                lol = df.values.tolist()

            return Pydf(cols=cols, lol=lol, keyfield=keyfield, name=name, dtypes=df.dtypes.to_dict())
            
        # first convert the Pandas df to a csv buffer.
        try:
            csv_buff = df.to_csv(None, index=False, quoting=csv.QUOTE_MINIMAL, lineterminator= '\r\n')
        except TypeError:
            csv_buff = df.to_csv(None, index=False, quoting=csv.QUOTE_MINIMAL, line_terminator= '\r\n')
            
        return Pydf.from_csv_buff(
            csv_buff=csv_buff,
            keyfield=keyfield,
            dtypes=dtypes,    
            unflatten=False,  
            )
            

    def to_pandas_df(self, use_csv: bool=False) -> Any:
    
        import pandas as pd     # type: ignore
    
        if not use_csv:
            columns = self.columns()
            # return pd.DataFrame(self.lol, columns=columns, dtypes=self.dtypes)
            # above results in NotImplementedError: compound dtypes are not implemented in the DataFrame constructor

            return pd.DataFrame(self.lol, columns=columns)
            
        # it seems this may work faster if we first convert the data to a csv_buff internally,
        # and then convert that to a df.
    
        csv_buff = self.to_csv_buff()
        sio = io.StringIO(csv_buff)            
        df  = pd.read_csv(sio, 
            na_filter=False, 
            index_col=False, 
            #dtype=self.dtypes,
            #sep=sep,
            usecols=None,
            #comment='#', 
            #skip_blank_lines=True
            )
        return df
        
            
    #==== Numpy
    @staticmethod
    def from_numpy(npa: Any, keyfield:str='', cols:Optional[T_la]=None, name:str='') -> 'Pydf':
        """
        Convert a Numpy dataframe to pydf object
        The resulting Python list will contain Python native types, not NumPy types. 
        """
        # import numpy as np
        
        lol = npa.tolist()
    
        return Pydf(cols=cols, lol=lol, keyfield=keyfield, name=name)
    

    @staticmethod
    def from_hllola(hllol: T_hllola, keyfield: str='', dtypes: Optional[T_dtype_dict]=None) -> 'Pydf':
        """ Create Pydf instance from hllola type.
            This is used for all DB. loading.
            test exists in test_pydf.py
            
            DEPRECATED
        """
        
        hl, lol = hllol
        
        return Pydf(lol=lol, cols=hl, keyfield=keyfield, dtypes=dtypes)
        
        
    #==== Googlesheets
    
    @staticmethod
    def from_googlesheet(spreadsheet_id: str, sheetname: str = 'Sheet1') -> 'Pydf':
        from googleapiclient.discovery import build
        from google.oauth2 import service_account

        """
        Read data from a Google Sheet specified by its ID.
        
        Args:
            spreadsheet_id (str): The ID of the Google Sheet.
            
        Returns:
            Pydf instance
            
        """
        
        # Set up credentials for the Google Sheets API
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'path/to/your/service_account.json'
        
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('sheets', 'v4', credentials=creds)
        
        # Specify the range from which to read data (all values)
        range_name = sheetname 
        
        # Call the Sheets API to get values from the specified range
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name
        ).execute()
        
        lol = result.get('values', [])
        
        # if not lol:
            # print('No data found in the Google Sheet.')
            # return None
        # else:
            # return values

        #num_rows = len(lol)
        num_cols = 0 if not lol else len(lol[0])
        
        cols = Pydf._generate_spreadsheet_column_names_list(num_cols)

        gs_pydf = Pydf(cols=cols, lol=lol)
        
        return gs_pydf
        
        
    def to_googlesheet(self, spreadsheet_id: str, sheetname: str = 'Sheet1') -> 'Pydf':
        """ export data from pydf structure to googlesheet. """
    
        from googleapiclient.discovery import build
        from google.oauth2 import service_account

        # Set up credentials for the Google Sheets API
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']       # this might be okay.
        SERVICE_ACCOUNT_FILE = 'path/to/your/service_account.json'      # probably wrong.

        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('sheets', 'v4', credentials=creds)

        # Define your list of lists array (Pydf)
        # self.lol

        # Define the range where you want to write the data (e.g., Sheet1!A1:C4)
        # get the column name of the last column in the array.
        num_cols = self.num_cols()
        last_col_idx = num_cols - 1
        last_spreadsheet_colname = Pydf._calculate_single_column_name(last_col_idx)
        
        range_name = f"{sheetname}!A1:{last_spreadsheet_colname}{len(self.lol)}"
        
        # Build the request body
        body = {
            'values': self.lol
        }

        # Call the Sheets API to update the data in the specified range
        request = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption='RAW',     # Question: does this provide formulas or just numbers.
            body=body
        )

        response = request.execute()
        # parse response and detect if there was an error.
        
        response = response     # fool linter

        print('Data successfully written to Google Sheets.')
        
        return self


    #===========================
    # convert to other format
    
    def to_numpy(self) -> Any:
        """ 
        Convert the core array of a Pydf object to numpy.
        Note: does not convert any column names if they exist.
        Keyfield lookups are lost, if they are defined.
        
        When you create a NumPy array with a specific data type 
        (e.g., int32, float64), NumPy will attempt to coerce or 
        cast the elements to the specified data type. The rules 
        for type casting follow a hierarchy where more general 
        types are converted to more specific types.
        
        examples:
           if dtype is np.int32 and there are some float values, they will be truncated.
           if dtype is np.int32 and there are some string values, they will be converted to an integer if possible.
           if dtype is float64 and there are some integer values, they will be csst to float64 type.
           if casting is not possible, it will raise an error.
        
        """
    
        import numpy as np
        return np.array(self.lol)
        

    def to_hllola(self) -> T_hllola:
        """ Create hllola from pydf 
            test exists in test_pydf.py
            
            DEPRECATED
        """    
        return (list(self.hd.keys()), self.lol)
        
    #===========================
    # append
        
    def append(self, data_item: Union[T_Pydf, T_loda, T_da, T_la]):
        """ general append method can handle appending one record as T_da or T_la, many records as T_loda or T_pydf
        """
        # test exists in test_pydf.py for all three cases
        
        if not data_item:
            return self
        
        if isinstance(data_item, dict):
            self.record_append(data_item)
            
        elif isinstance(data_item, list):
            if isinstance(data_item[0], dict):
                # lod type
                self.extend(data_item)
            else:
                # simple list.
                if self.hd:
                    # columns are defined, and keyfield might also be defined
                    # create a dict.
                    da = dict(zip(self.hd.keys(), data_item))
                    self.record_append(da)
                else:    
                    # no columns defined, therefore just append to lol.
                    self.lol.append(data_item)
                
        elif isinstance(data_item, Pydf):  # type: ignore
            self.concat(data_item)
        else:    
            raise RuntimeError    # pragma: no cover
            
        return self
        

    def concat(self, other_instance: 'Pydf'):
        """ concatenate records from passed pydf cls to self pydf 
            This directly modifies self
            if keyfield is '', then insert without respect to the key value
            otherwise, allow only one record per key.
            columns must be equal.
            test exists in test_pydf.py
        """
        
        if not other_instance:
            return 
            
        diagnose = False

        if diagnose:      # pragma: no cover
            print(f"self=\n{self}\npydf=\n{other_instance}")
            
        if not self.lol and not self.hd:
            
            self.hd = other_instance.hd
            self.lol = other_instance.lol
            self.kd = other_instance.kd
            self.keyfield = other_instance.keyfield
            self._rebuild_kd()   # only if the keyfield is set.
            return self
            
        # fields must match exactly!
        if self.hd != other_instance.hd:
            raise KeyError ("keys in pydf do not match lod keys")
        
        # simply append the rows from pydf.lol to the end of self.lol
        for idx in range(len(other_instance.lol)):
            rec_la = other_instance.lol[idx]
            self.lol.append(rec_la)
        self._rebuild_kd()   # only if the keyfield is set.

        if diagnose:  # pragma: no cover
            print(f"result=\n{self}")
            
        return self
                

    def extend(self, records_lod: T_loda):
        """ append lod of records into pydf 
            This directly modifies pydf
            if keyfield is '', then insert without respect to the key value
            otherwise, allow only one record per key.
            test exists in test_pydf.py
         """
        
        if not records_lod or len(records_lod) == 1 and not records_lod[0]:
            return self
            
        if not self.lol and not self.hd:
            # new pydf, adopt structure of lod.
            # but there is only one header and data is lol
            # this saves space.
            
            self.hd = {col_name: index for index, col_name in enumerate(records_lod[0].keys())}
            self.lol = [list(record_da.values()) for record_da in records_lod]
            self._rebuild_kd()   # only if the keyfield is set.
            return self
            
        for record_da in records_lod:
            # this test done inside record_append()
            # if not record_da:
                # # do not append any records that are empty.
                # continue
            
            # the following will either append or insert
            # depending on the keyvalue.
            self.record_append(record_da)    
            
        return self            
            

    def record_append(self, record_da: T_da):
        """ perform append of one record into pydf (T_da is Dict[str, Any]) 
            This directly modifies pydf
            if keyfield is '', then insert without respect to the key value
            otherwise, allow only one record per key.
            
            if the pydf is empty, it will adopt the structure of record_da.
            Each new append will add to the end of the pydf.lol and will
            update the kd.
            
            If the keys in the record_da have a different order, they will
            be reordered and then appended correctly.
        """
            # test exists in test_pydf.py
        
        if not record_da:
            return self
            
        if not self.lol and not self.hd:
            # new pydf, adopt structure of lod.
            # but there is only one header and data is lol
            # this saves space.
            
            self.hd = {col_name: index for index, col_name in enumerate(record_da.keys())}
            self.lol = [list(record_da.values())]
            self._rebuild_kd()   # only if the keyfield is set.
            return self
            
        # check if fields match exactly.
        reorder = False
        if list(self.hd.keys()) != list(record_da.keys()):
            reorder = True
        
        if reorder:
            # construct a dict with exactly the cols specified.
            # defaults to '' at this point.
            rec_la = [record_da.get(col, '') for col in self.hd]
        else:
            rec_la = list(record_da.values())
            
        if self.keyfield:
            # insert will overwrite any existing key with the same value.
            keyval = record_da[self.keyfield]
            idx = self.kd.get(keyval, -1)
            if idx >= 0:
                self.lol[idx] = rec_la
            else:
                self._basic_append_la(rec_la, keyval)
        else:
            # no keyfield is set, just append to the end.
            self.lol.append(rec_la)
            
        return self


    def _basic_append_la(self, rec_la: T_la, keyval: str):
        """ basic append to the end of the array without any checks
            including appending to kd and la to lol
        """
        self.kd[keyval] = len(self.lol)
        self.lol.append(rec_la)
            
        return self
                

    #=========================
    # remove records per keyfield; drop cols

    def remove_key(self, keyval:str, silent_error=True) -> None:
        """ remove record from pydf using keyfield
            This directly modifies pydf
        """
        # test exists in test_pydf.py

        if not self.keyfield:
            return self
        
        try:
            key_idx = self.kd[keyval]   #will raise KeyError if key not exists.
        except KeyError:
            if silent_error: 
                return self
            raise
            
        self.lol.pop(key_idx)
        self._rebuild_kd()
        return self
        
    
    def remove_keylist(self, keylist: T_ls, silent_error=True):
        """ remove records from pydf using keyfields
            This directly modifies pydf
            test exists in test_pydf.py
        """

        # get the indexes of rows to be deleted.
        idx_li: T_li = []
        for keyval in keylist:
            try:
                idx = self.kd[keyval]
            except KeyError:
                if silent_error: continue
                raise
            idx_li.append(idx)    
                
        # delete records from the end so the indexes are valid after each deletion.
        reverse_sorted_idx_li = sorted(idx_li, reverse=True)

        for idx in reverse_sorted_idx_li:
            self.lol.pop(idx)

        self._rebuild_kd()
            
        return self
        
        
    def get_existing_keys(self, keylist: T_ls) -> T_ls:
        """ check the keylist against the keys defined in a pydf instance. 
        """
    
        return [key for key in keylist if key in self.kd]


    #=========================
    #   selecting
    
    def select_record_da(self, key: str) -> T_da:
        """ Select one record from pydf using the key and return as a single T_da dict.
            test exists in test_pydf.py
        """
        
        if not self.keyfield:
            raise RuntimeError
            
        row_idx = self.kd.get(key, -1)
        if row_idx < 0:
            return {}
        if row_idx >= len(self.lol):
            return {}
        
        record_da = self._basic_get_record_da(row_idx)
        
        return record_da
        
    
    def _basic_get_record_da(self, irow: int, include_cols: Optional[T_ls]=None) -> T_da:
        """ return a record at irow as dict 
            include only "include_cols" if it is defined
            note, this requires that hd is defined.
            TODO options:
                create a column header if needed here.
                always create a column header when pydf is created if one is not defined.
        """
        if not self.hd:
            raise RuntimeError("hd must be defined here")
        
        if include_cols:
            return {col:self.lol[irow][self.hd[col]] for col in include_cols if col in self.hd}
        else:
            return dict(zip(self.hd, self.lol[irow]))

        
    def select_irows(self, irows_li: T_li) -> 'Pydf':
        """ Select multiple records from pydf using row indexes and create new pydf.
            
        """
        
        selected_pydf = self.clone_empty()
        
        for row_idx in irows_li:
            record_da = self._basic_get_record_da(row_idx)
        
            selected_pydf.append(record_da)
                      
        return selected_pydf
        
        
    def select_records_pydf(self, keys_ls: T_ls, inverse:bool=False) -> 'Pydf':
        """ Select multiple records from pydf using the keys and return as a single pydf.
            If inverse is true, select records that are not included in the keys.
            
        """
        #    unit tests exist but not for inverse yet.
        
        if not self.keyfield:
            raise RuntimeError
            
        # determine the rows selected.
        if not inverse:
            selected_irows = [self.kd[key] for key in keys_ls if key in self.kd]    
        else:
            if len(keys_ls) > 10 and len(self.kd) > 30:
                keys_d = dict.fromkeys(keys_ls)     # create a dictionary for fast lookup.
                selected_irows = [self.kd[key] for key in self.kd if key not in keys_d]    
            else:
                # short lists work just fine for fast lookups.
                selected_irows = [self.kd[key] for key in self.kd if key not in keys_ls]    

        
        return self.select_irows(selected_irows) 
        
        
    def irow(self, irow: int, include_cols: Optional[T_ls]=None) -> T_da:
        """ alias for iloc 
            test exists in test_pydf.py
        """
        return self.iloc(irow, include_cols)
        

    def iloc(self, irow: int, include_cols: Optional[T_ls]=None) -> T_da:
        """ Select one record from pydf using the idx and return as a single T_da dict
            test exists in test_pydf.py
        """
        
        if irow < 0 or irow >= len(self.lol) or not self.lol or not self.lol[irow]:
            return {}
            
        if self.hd: 
            return self._basic_get_record_da(irow, include_cols)
                
        colnames = self.__class__._generate_spreadsheet_column_names_list(num_cols=len(self.lol[irow]))
        return dict(zip(colnames, self.lol[irow]))
        

    def select_by_dict_to_lod(self, selector_da: T_da, expectmax: int=-1, inverse: bool=False) -> T_loda:
        """ Select rows in pydf which match the fields specified in d, returning lod 
            test exists in test_pydf.py
        """

        # from utilities import utils

        result_lod = [d2 for d2 in self if inverse ^ utils.is_d1_in_d2(d1=selector_da, d2=d2)]
    
        if expectmax != -1 and len(result_lod) > expectmax:
            raise LookupError
            # import pdb; pdb.set_trace() #perm
            # pass
        
        return result_lod


    def select_by_dict(self, selector_da: T_da, expectmax: int=-1, inverse:bool=False, keyfield:str='') -> 'Pydf':
        """ Selects rows in pydf which match the fields specified in d
            and return new pydf, with keyfield set according to 'keyfield' argument.
            test exists in test_pydf.py
        """

        # from utilities import utils

        result_lol = [list(d2.values()) for d2 in self if inverse ^ utils.is_d1_in_d2(d1=selector_da, d2=d2)]
    
        if expectmax != -1 and len(result_lol) > expectmax:
            raise LookupError
            # import pdb; pdb.set_trace() #perm
            # pass
            
        new_keyfield = keyfield or self.keyfield
        
        pydf = Pydf(cols=self.columns(), lol=result_lol, keyfield=new_keyfield, dtypes=self.dtypes)
        
        return pydf
        
        
    def select_first_row_by_dict(self, selector_da: T_da, inverse:bool=False) -> T_da:
        """ Selects the first row in pydf which matches the fields specified in selector_da
            and returns that row. Else returns {}.
            Use inverse to find the first row that does not match.
        """
            
        # test exists in test_pydf.py

        for d2 in self:
            if inverse ^ utils.is_d1_in_d2(d1=selector_da, d2=d2):
                return d2

        return {}


    def select_where(self, where: Callable) -> 'Pydf':
        """
        Select rows in Pydf based on the provided where condition
        if provided as a string, the variable 'row' is the current row being evaluated.
        if a callable function, then it is passed the row.

        # Example Usage
        
            result_pydf = original_pydf.select_where(lambda row: bool(int(row['colname']) > 5))
        
        """
        result_lol = [list(row.values()) for row in self if where(row)]

        pydf = Pydf(cols=self.columns(), lol=result_lol, keyfield=self.keyfield, dtypes=self.dtypes)

        return pydf    
        

    def select_where_idxs(self, where: Callable) -> T_li:
        """
        Select rows in Pydf based on the provided where condition
        variable 'row' is the current row being evaluated
        and return list of indexes.

        # Examle Usage
            result_pydf = original_pydf.select_where("int(row['colname']) > 5")
        
        """
        return [idx for idx, row in enumerate(self) if where(row)]


    def col(self, colname: str, unique: bool=False, omit_nulls: bool=False, silent_error:bool=False) -> list:
        """ alias for col_to_la()
            can also use column ranges and then transpose()
            test exists in test_pydf.py
        """
        return self.col_to_la(colname, unique, omit_nulls=omit_nulls, silent_error=silent_error)


    def col_to_la(self, colname: str, unique: bool=False, omit_nulls: bool=False, silent_error:bool=False) -> list:
        """ pull out out a column from pydf by colname as a list of any
            does not modify pydf. Using unique requires that the 
            values in the column are hashable.
            test exists in test_pydf.py
        """
        
        if not colname:
            raise RuntimeError("colname is required.")
        if colname not in self.hd:
            if silent_error:
                return []
            raise RuntimeError(f"colname {colname} not defined in this pydf. Use silent_error to return [] in this case.")

        icol = self.hd[colname]
        result_la = self.icol_to_la(icol, unique=unique, omit_nulls=omit_nulls)
        
        return result_la

        
    def icol(self, icol: int) -> list:
        return self.icol_to_la(icol)


    def icol_to_la(self, icol: int, unique: bool=False, omit_nulls: bool=False) -> list:
        """ pull out out a column from pydf by icol idx as a list of any 
            can also use column ranges and then transpose()
            does not modify pydf
            test exists in test_pydf.py
        """
        
        if icol < 0 or not self or icol >= self.num_cols():
            return []
        
        if omit_nulls:
            result_la = [la[icol] for la in self.lol if la[icol]]
        else:
            result_la = [la[icol] for la in self.lol]

        if unique:
            result_la = list(dict.fromkeys(result_la))
            
        return result_la
            
    
    def drop_cols(self, exclude_cols: Optional[T_ls]=None):
        """ given a list of colnames, cols, remove them from pydf array
            alters the pydf and creates a copy of all data.
            
            Note: could provide an option to not create a copy, and use splicing.
            
            test exists in test_pydf.py
        """
        
        if exclude_cols:
            keep_idxs_li: T_li = [self.hd[col] for col in self.hd if col not in exclude_cols]
        
        else:
            return
        
        for irow, la in enumerate(self.lol):
            la = [la[idx] for idx in keep_idxs_li]
            self.lol[irow] = la
            
        old_cols = list(self.hd.keys())
        new_cols = [old_cols[idx] for idx in keep_idxs_li]
        self._cols_to_hd(new_cols)
        
        new_dtypes = {col: typ for idx, (col, typ) in enumerate(self.dtypes.items()) if idx not in keep_idxs_li}
        self.dtypes = new_dtypes
        

    def select_cols(self, 
            cols: Optional[T_ls]=None, 
            exclude_cols: Optional[T_ls]=None, 
            ) -> 'Pydf':
        """ given a list of colnames, alter the pydf to select only the cols specified.
            this produces a new pydf. Instead of selecting cols in this manner, simply
            provide cols parameter in any .apply, .reduce, .from_xxx or .to_xxx methods.
        """
        
        if not cols:
            cols = []
        if not exclude_cols:
            exclude_cols = []
            
        desired_cols = self.calc_cols( 
            include_cols=cols,
            exclude_cols=exclude_cols
            )
    
        selected_cols_li = [self.hd[col] for col in desired_cols if col in self.hd]
        
        # select from the array and create a new object.
        # this is time consuming.
        for irow, la in enumerate(self.lol):
            la = [la[col_idx] for col_idx in range(len(la)) if col_idx in selected_cols_li]
            self.lol[irow] = la
       
        # fix up the column names  
        old_cols = list(self.hd.keys())
        new_cols = [old_cols[idx] for idx in range(len(old_cols)) if idx in selected_cols_li]
        self._cols_to_hd(new_cols)
        
        self.dtypes = {col: typ for col, typ in self.dtypes.items() if col in new_cols}
        

    def from_selected_cols(self, cols: Optional[T_ls]=None, exclude_cols: Optional[T_ls]=None) -> 'Pydf':
        """ given a list of colnames, create a new pydf of those cols.
            creates as new pydf
        """
        
        if not cols:
            cols = []
        if not exclude_cols:
            exclude_cols = []
            
        desired_cols = self.calc_cols(include_cols=cols, exclude_cols=exclude_cols)
    
        selected_idxs = [self.hd[col] for col in desired_cols if col in self.hd]
        
        new_lol = []
        
        for irow, la in enumerate(self.lol):
            la = [la[idx] for idx in range(len(la)) if idx in selected_idxs]
            new_lol.append(la)
            
        old_cols = list(self.hd.keys())
        new_cols = [old_cols[idx] for idx in range(len(old_cols)) if idx in selected_idxs]
        
        new_dtypes = {col: typ for col, typ in self.dtypes.items() if col in new_cols}
        
        return Pydf(lol=new_lol, cols=new_cols, dtypes=new_dtypes)
        

    #=========================
    #   modify records
        
    def assign_record_da(self, record_da: T_da):
        """ Assign one record in pydf using the key using a single T_da dict.
            unit tests exist
        """
        
        if not self.keyfield:
            raise RuntimeError("No keyfield estabished for pydf.")
            
        keyfield = self.keyfield
        if keyfield not in record_da:
            raise RuntimeError("No keyfield in dict.")
            
        if self and list(record_da.keys()) != list(self.hd.keys()):
            raise RuntimeError("record fields not equal to pydf columns")
            
        keyval = record_da[keyfield]
            
        row_idx = self.kd.get(keyval, -1)
        if row_idx < 0 or row_idx >= len(self.lol):
            self.append(record_da)
        else:
            #normal_record_da = Pydf.normalize_record_da(record_da, cols=self.columns(), dtypes=self.dtypes)   
            self.lol[row_idx] = [record_da.get(col, '') for col in self.hd]
        

    def assign_record_da_irow(self, irow: int=-1, record_da: Optional[T_da]=None):
        """ Assign one record in pydf using the iloc using a single T_da dict.
            unit tests exist
        """
        
        if record_da is None:
            return
        
        if irow < 0 or irow >= len(self.lol):
            self.append(record_da)
        else:
            #normal_record_da = Pydf.normalize_record_da(record_da, cols=self.columns(), dtypes=self.dtypes)   
            self.lol[irow] = [record_da.get(col, '') for col in self.hd]
        

    def update_by_keylist(self, keylist: Optional[T_ls]=None, record_da: Optional[T_da]=None):
        """ Update selected records in pydf by keylist using record_da
            only update those columns that have dict keys
            but keep all other dict items intact in that row if not updated.
        """
        
        if record_da is None or not self.lol or not self.hd or not self.keyfield or not keylist:
            return

        for key in keylist:
            self.update_record_da_irow(self.kd.get(key, -1), record_da)
            
        

    def update_record_da_irow(self, irow: int=-1, record_da: Optional[T_da]=None):
        """ Update one record in pydf at iloc using a single T_da dict,
            and only update those columns that have dict keys
            but keep all other dict items intact in that row.
            unit tests exist
        """
        
        if record_da is None or not self.lol or not self.hd:
            return
        
        if irow < 0 or irow >= len(self.lol):
            return
        
        for colname, val in record_da.items():
            icol = self.hd.get(colname, -1)
            if icol >= 0:
                self.lol[irow][icol] = record_da[colname]
        

    def assign_icol(self, icol: int=-1, col_la: Optional[T_la]=None, default: Any=''):
        """ modify icol by index using col_la 
            use default if col_la not long enough to fill all cells.
            Also, if col_la not provided, use default to fill all cells in the column.
            if icol == -1, append column on the right side.
        """
        # from utilities import utils

        self.lol = utils.assign_col_in_lol_at_icol(icol, col_la, lol=self.lol, default=default)
        
        
        
    def insert_icol(self, icol: int=-1, col_la: Optional[T_la]=None, colname: str='', default: Any='', keyfield:str=''):
        """ insert column col_la at icol, shifting other column data. 
            use default if la not long enough
            If icol==-1, insert column at right end.
            unit tests
        """
        
        # from utilities import utils

        self.lol = utils.insert_col_in_lol_at_icol(icol, col_la, lol=self.lol, default=default)
        
        if colname:
            if not self.hd:
                self.hd = {}
            if icol < 0 or icol >= len(self.hd):
                icol = len(self.hd)
            hl = list(self.hd.keys())
            hl.insert(icol, colname)
            self.hd = {k: idx for idx, k in enumerate(hl)}
            
        if keyfield:
            self.keyfield = keyfield
            self._rebuild_kd()

        
    def insert_irow(self, irow: int=-1, row_la: Optional[T_la]=None, default: Any=''):
        """ insert row row_la at irow, shifting other rows down. 
            use default if la not long enough
            If irow > len(pydf), insert row at the end.
            
        """
        
        # from utilities import utils

        self.lol = utils.insert_row_in_lol_at_irow(irow=irow, row_la=row_la, lol=self.lol, default=default)
        
        self._rebuild_kd()


    def assign_col(self, colname: str, la: Optional[T_la]=None, default: Any=''):
        """ modify col by colname using la 
            use default if la not long enough.
            test exists in test_pydf.py
        """
        
        if not colname or colname not in self.hd:
            return []
        icol = self.hd[colname]
        self.assign_icol(icol, la, default)
        

    # def set_col(self, colname: str, val: Any):
        # """ modify col by colname using val """
        
        # if not colname or colname not in self.hd:
            # return
        # icol = self.hd[colname]
        # self.set_icol(icol, val)
        

    def insert_col(self, colname: str, col_la: Optional[T_la]=None, icol:int=-1, default:Any='', keyfield:str=''):
        """ add col by colname and set to la at icol
            if la is not long enough for a full column, use the default.
            if colname exists, overwrite it.
            Can use to set a constant value by not passing col_la and setting default.
            Can assign a new keyfield to this column, if keyfield is not ''
            unit tested
        """
        
        if not colname:
            return
        if not col_la:
            col_la = []
            
        colname_icol = self.hd.get(colname, -1)
        if colname_icol >= 0:
            # column already exists. ignore icol, overwrite data.
            self.assign_col(colname, col_la, default)
            return

        self.insert_icol(icol=icol, col_la=col_la, colname=colname, default=default, keyfield=keyfield)
        
        # hl = list(self.hd.keys())
        # hl.insert(icol, colname)
        # self.hd = {k: idx for idx, k in enumerate(hl)}        
        
    
    def insert_idx_col(self, colname='idx', icol:int=0, startat:int=0):
        """ insert an index column at column icol with name colname with indexes starting at 'startat' 
            unit tested
        """
        
        num_rows = len(self)
        col_la = list(range(startat, startat + num_rows))
    
        self.insert_col(colname, col_la, icol)


    def set_col_irows(self, colname: str, irows: T_li, val: Any):
        """ set a given icol and list of irows to val """
        
        if not colname or colname not in self.hd:
            return
        icol = self.hd[colname]

        self.set_icol_irows(icol, irows, val)
    

    def set_icol(self, icol: int, val: Any):
    
        for irow in range(len(self.lol)):
            self.lol[irow][icol] = val
        

    def set_icol_irows(self, icol: int, irows: T_li, val: Any):
        """ set a given icol and list of irows to val """
        
        for irow in irows:
            if irow >= len(self.lol) or irow < 0:
                continue
        
            self.lol[irow][icol] = val        
    
    
    #=========================
    # find/replace
    
    def find_replace(self, find_pat, replace_val):
        """ scan cells in pydf and if match is found, replace the cell with pattern """

        for row_la in self.lol:
            for i, value in enumerate(row_la):
                if bool(re.search(find_pat, str(value))):
                    row_la[i] = replace_val
        
    

    #=========================
    # split and grouping
    
    def split_pydf_into_ranges(self, chunk_ranges: List[Tuple[int, int]]) -> List['Pydf']:
        """ Given a df and list of (start,end) ranges, split pydf into list of pydf.
        """
        
        chunks_lopydf = [self.select_irows(list(range(start, end))) for start,end in chunk_ranges]
        #chunks_lopydf = [self[start:end] for start, end in chunk_ranges]
        return chunks_lopydf
        
        
    
    def split_pydf_into_chunks_lopydf(self, max_chunk_size: int) -> List['Pydf']:
        """ given a pydf, split it evenly by rows into a list of pydfs.
            size of some pydfs may be less than the max but not over.
        """
        # from utilities import utils
        
        chunk_sizes_list = utils.calc_chunk_sizes(num_items=len(self), max_chunk_size=max_chunk_size)
        chunk_ranges = utils.convert_sizes_to_idx_ranges(chunk_sizes_list)
        chunks_lopydf = self.split_pydf_into_ranges(chunk_ranges)
        return chunks_lopydf

           
    #=========================
    #   sort
            
    def sort_by_colname(self, colname:str, reverse: bool=False, length_priority: bool=False):
        """ sort the data by a given colname, using length priority unless specified.
            sorts in place. Make a copy if you need the original order.
        """
        colidx = self.hd[colname]
        self.lol = utils.sort_lol_by_col(self.lol, colidx, reverse=reverse, length_priority=length_priority)
        self._rebuild_kd()
        
    #=========================
    #   apply formulas

    def apply_formulas(self, formulas_pydf: 'Pydf'):
        r""" apply an array of formulas to the data in pydf
        
        formulas must have the same shape as self pydf instance.
        cells which are empty '' do not function.
        
        formulas are re-evaluated until there are no further changes. Error will result if expressions are circular.
        
        #### Special Notation
        There is only a very few cases of special notation:

        - $d -- references the current pydf instance, a convenient shorthand.
        - $c -- the current cell column index
        - $r -- the current cell row index
        
        Typical cases:
            sum($d[$r, :$c])        sum all cells in the current row from the first column upto but not including the current column
            sum($d[:$r, $c])        sum all cells in the cnrrent column from the first row upto but not including the current row
            $d[14,20]+$d[15,25]     add data in the cell at row 14, col 20 to the data in cell at row 15 and column 25
            max(0,$d[($r-1),$c])    the value prior row in current column unless less than 0, then will enter 0.
            $d[($r-1),$c] * 0.15    15% of the value prior row in current column  

        By using the current cell references, formulas can be the same no matter where they may be written, similar to spreadsheet formulas.
        Typical spreadsheet formulas are treated as relative, and then modified whenever copied for the same relative cell references, unless they are made absolute by using $.
        Here, the references are absolute unless you create a relative reference by relating to the current cell row $r and/or column $c.
        
        Example usage:
            The following example adds rows and columns of a 3 x 2 array of values.
        
            example_pydf = Pydf(cols=['A', 'B', 'C'], lol=[[1, 2, 0],[4, 5, 0],[7, 8, 0],[0, 0, 0]])
            formulas_pydf = Pydf(cols=['A', 'B', 'C'], 
            formulas_pydf = Pydf(cols=['A', 'B', 'C'], 
                    lol=[['',                    '',                    "sum($d[$r,:$c])"],
                         ['',                    '',                    "sum($d[$r,:$c])"],
                         ['',                    '',                    "sum($d[$r,:$c])"],
                         ["sum($d[:$r,$c])",     "sum($d[:$r,$c])",     "sum($d[:$r,$c])"]]
                         )
            expected_result = Pydf(cols=['A', 'B', 'C'], lol=[[1, 2, 3],[4, 5, 9],[7, 8, 15],[12, 15, 27]])
            
        """
        
        # TODO: This algorithm is not optimal. Ideally, a dependency tree would be formed and
        # cells modified in from those with no dependencies to those that depend on others.
        # This issue will not become a concern unless the number of formulas is substantial.
        
        if not self:
            return
        
        if self.shape() != formulas_pydf.shape():
            import pdb; pdb.set_trace() #temp
            
            raise RuntimeError("apply_formulas requires data arrays of the same shape.")
        
        lol_changed = True     # must evaluate at least once.
        loop_limit = 100
        loop_count = 0
        
        # the following deals with $d, $r, $c in the formulas
        parsed_formulas_pydf = formulas_pydf._parse_formulas()
        
        while lol_changed:
            lol_changed = False
            loop_count += 1
            if loop_count > loop_limit:
                raise RuntimeError("apply_formulas is resulting in excessive evaluation loops.")
            
            for irow in range(len(self.lol)):
                for icol in range(self.num_cols()):
                    cell_formula = parsed_formulas_pydf.lol[irow][icol]
                    if not cell_formula:
                        # no formula provided -- do nothing
                        continue
                    try:    
                        new_value = eval(cell_formula)
                    except Exception as err:
                        print(f"Error in formula for cell [{irow},{icol}]: '{cell_formula}': '{err}'")
                        import pdb; pdb.set_trace() #temp
                        raise
                    
                    if new_value != self.lol[irow][icol]:
                        # update the value in the array, and set lol_changed flag
                        self.lol[irow][icol] = new_value
                        lol_changed = True
                    else:
                        continue
        self._rebuild_kd()
        
    def _parse_formulas(self) -> 'Pydf':
    
        # start with unparsed formulas
        parsed_formulas = copy.deepcopy(self)
    
        for irow in range(len(self.lol)):
            for icol in range(self.num_cols()):
                proposed_formula = self.lol[irow][icol]
                if not proposed_formula:
                    # no formula provided.
                    continue
                    
                proposed_formula = proposed_formula.replace('$d', 'self')    
                proposed_formula = proposed_formula.replace('$c', str(icol))    
                proposed_formula = proposed_formula.replace('$r', str(irow))    
                      
                parsed_formulas[irow,icol] = proposed_formula
                
        return parsed_formulas
        
            

    def cols_to_dol(self, colname1: str, colname2: str) -> T_dola:
        """ given a pydf with at least two columns, create a dict of list
            lookup where the key are values in col1 and list of values are 
            unique values in col2. Values in cols must be hashable.
            
        For example, if:

        pydf.lol = [['a', 'b', 'c'], 
                    ['b', 'd', 'e'], 
                    ['a', 'f', 'g'], 
                    ['b', 'd', 'm']]
        pydf.columns = ['col1', 'col2', 'col3']
        pydf.cols_to_dol('col1', 'col2') results in
        {'a': ['b', 'f'], 'b':['d']}
            
            test exists in test_pydf.py
            
        """
        
        if colname1 not in self.hd or colname2 not in self.hd or not self.lol:
            return {}

        colidx1 = self.hd[colname1]
        colidx2 = self.hd[colname2]
        
        
        # first work with dict of dict for speed.
        result_dadn: Dict[Any, Dict[Any, None]] = {}
        
        for la in self.lol:
            val1 = la[colidx1]
            val2 = la[colidx2]
            if val1 not in result_dadn:
                result_dadn[val1] = {val2: None}
            elif val2 not in result_dadn[val1]:
                result_dadn[val1][val2] = None
            # otherwise, it is already in the result.
                
        # now convert dadn to dola

        result_dola = {k: list(d.keys()) for k, d in result_dadn.items()}
                
        return result_dola        

    #===============================
    # apply and reduce

    def apply(self, 
            func: Callable[[Union[T_da, T_Pydf], Optional[T_la]], Union[T_da, T_Pydf]], 
            by: str='row', 
            cols: Optional[T_la]=None,                      # columns included in the apply operation.
            keylist: Optional[T_ls]=None,                   # list of keys of rows to include.
            **kwargs: Any,
            ) -> "Pydf":
        """
        Apply a function to each 'row', 'col', or 'table' in the Pydf and create a new Pydf with the transformed data.
        Note: to apply a function to a portion of the table, first select the columns or rows desired 
                using a selection process.

        Args:
            func (Callable): The function to apply to each 'row', 'col', or 'table'. 
            It should take a row dictionary and any additional parameters.
            by (str): either 'row', 'col' or 'table'
                if by == 'table', function should create a new Pydf instance.
            keylist: Optional[T_ls]=None,                   # list of keys of rows to include.
            **kwargs: Additional parameters to pass to the function.

        Returns:
            Pydf: A new Pydf instance with the transformed data.
        """
        if by == 'table':
            return func(self, **kwargs)
       
        result_pydf = self.clone_empty()

        if by == 'row':
            if keylist is None:
                keylist = []
        
            keylist_or_dict = keylist if not keylist or len(keylist) < 30 else dict.fromkeys(keylist)
            for row in self:
                if self.keyfield and keylist_or_dict and self.keyfield not in keylist_or_dict:
                    continue
                transformed_row = func(row, cols, **kwargs)
                result_pydf.append(transformed_row)
                
        elif by == 'col':
            # this is not working yet, don't know how to handle cols, for example.
            raise NotImplementedError
        
            num_cols = self.num_cols()
            for icol in range(num_cols):
                col_la = self.icol(icol)
                transformed_col = func(col_la, cols, **kwargs)
                result_pydf.insert_icol(icol, transformed_col)
        else:
            raise NotImplementedError
            
        # Rebuild the internal data structure (if needed)
        result_pydf._rebuild_kd()

        return result_pydf
      
      
    def update_row(row, da):
        row.update(da)
        return row
      
        
    def apply_in_place(self, 
            func: Callable[[T_da], T_da], 
            by: str='row', 
            keylist: Optional[T_ls]=None,                   # list of keys of rows to include.
            **kwargs: Any,
            ):
        """
        Apply a function to each 'row', 'col', or 'table' in the pydf.

        Args:
            func (Callable): The function to apply to each 'row' 
            It should take a row dictionary and any additional parameters.
            # by (str): either 'row', 'col' or 'table'
            #     if by == 'table', function should create a new Pydf instance.
            keylist: list of keys of rows to include.
            **kwargs: Additional parameters to pass to the function.

        Modifies self in-place.
        """
        if keylist is None:
            keylist = []
        
        if by == 'row':
            keylist_or_dict = keylist if not keylist or len(keylist) < 30 else dict.fromkeys(keylist)

            for idx, row_da in enumerate(self):
                if self.keyfield and keylist_or_dict and self.keyfield not in keylist_or_dict:
                    continue
                transformed_row_da = func(row_da, **kwargs)
                self.lol[idx] = list(transformed_row_da.values())
                
        else:
            raise NotImplementedError
            
        # Rebuild the internal data structure (if needed)
        self._rebuild_kd()
        
        
    def reduce(self, 
            func: Callable[[T_da, T_da], Union[T_da, T_la]], 
            by: str='row', 
            cols: Optional[T_la]=None,                      # columns included in the reduce operation.
            **kwargs: Any,
            ) -> Union[T_da, T_la]:
        """
        Apply a function to each 'row', 'col', or 'table' and accumulate to a single T_da
        Note: to apply a function to a portion of the table, first select the columns or rows desired 
                using a selection process.

        Args:
            func (Callable): The function to apply to each 'row', 'col', or 'table'. 
            It should take a row dictionary and any additional parameters.
            by (str): either 'row', 'col' or 'table'
                if by == 'table', function should create a new Pydf instance.
            **kwargs: Additional parameters to pass to the function.

        Returns:
            either a dict (by='rows' or 'table') or list (by='cols')
        """
        if by == 'table':
            reduction_da = func(self, cols, **kwargs)
            return reduction_da    

        if by == 'row':
            reduction_da = {}
            for row_da in self:
                reduction_da = func(row_da, reduction_da, cols, **kwargs)
            return reduction_da    
                
        elif by == 'col':
            reduction_la = []
            num_cols = self.num_cols()
            for icol in range(num_cols):
                col_la = self.icol(icol)
                reduction_la = func(col_la, reduction_la, **kwargs)
            return reduction_la

        else:
            raise NotImplementedError
        return [] # for mypy only.
        
        
    def manifest_apply(self, 
            func: Callable[[T_da, Optional[T_la]], Tuple[T_da, 'Pydf']],    # function to apply according to 'by' parameter 
            load_func: Callable[[T_da], 'Pydf'],            # optional function to load data for each manifest entry, defaults to local file system 
            save_func: Callable[[T_da, 'Pydf'], str],       # optional function to save data for each manifest entry, defaults to local file system
            by: str='row',                                  # determines how the func is applied.
            cols: Optional[T_la]=None,                      # columns included in the apply operation.
             **kwargs: Any,
            ) -> "Pydf":
        """
        Given a chunk_manifest_pydf, where each record is a chunk_spec (dict),
        1. load the each chunk using 'load_func(chunk_spec)'
        2. apply 'func' to the loaded Pydf instance to produce (result_chunk_spec, new_pydf) 
        3. save new_pydf using 'save_func(result_chunk_spec)'
        4. append result_chunk_spec to result_manifest_pydf describing the resulting chunks 

        Args:
            func (Callable): The function to apply to each table specified by each record in self.
            load_func (Callable): load specified pydf table based on the chunkspec in each row of self.
            save_func (Callable): save resulting pydf table after operation by func.
            **kwargs: Additional parameters to pass to func

        Returns:
            result_manifest_pydf
            
        Note, this method can be used for transformation, where the same number of transformed chunks exists,
            or, it can be used for reduction.
        if 'reduce' is true, then each chunk returns a pydf with a single row.
            
            
        """

        result_manifest_pydf = Pydf()

        for chunk_spec in self:
            # Apply the function for all chunks specified.
            # Load the specified Pydf table
            loaded_pydf = load_func(chunk_spec)

            # Apply the function to the loaded Pydf
            result_chunk_spec, transformed_pydf = loaded_pydf.apply(func, by=by, cols=cols, **kwargs)
            
            # Save the resulting Pydf table
            save_func(result_chunk_spec, transformed_pydf)
        
            # Update the manifest with information about the resulting chunk
            result_manifest_pydf.append(result_chunk_spec)
            
        return result_manifest_pydf        

    
    def manifest_reduce(self, 
            func: Callable[[T_da, Optional[T_la]], T_da], 
            load_func: Optional[Callable[[T_da], 'Pydf']] = None,
            by: str='row',                                  # determines how the func is applied.
            cols: Optional[T_la]=None,                      # columns included in the reduce operation.
            **kwargs: Any,
            ) -> T_da:
        """
        Apply a reduction function to the tables specified by the chunk manifest.

        Args:
            func (Callable): The function to apply to each table specified by each record in self.
            load_func (Callable): Load specified pydf table based on the chunkspec in each row of self.
            **kwargs: Additional parameters to pass to func

        Returns:
            Pydf: Result of reducing all chunks into a single record.
        """
        first_reduction_pydf = self.clone_empty()

        for chunk_spec in self:
            # Load the specified Pydf table
            loaded_pydf = load_func(chunk_spec)

            # Apply the function to the loaded Pydf
            reduction_da = loaded_pydf.reduce(func, by=by, cols=cols, **kwargs)

            first_reduction_pydf.append(reduction_da)     

        final_reduction_da = first_reduction_pydf.reduce(func, by=by, cols=cols, **kwargs)
        
        return final_reduction_da
        
        
    def manifest_process(self, 
            func: Callable[[T_da, Optional[T_la]], T_da],   # function to run for each hunk specified by the manifest
            **kwargs: Any,
            ) -> 'Pydf':                                    # records describing metadata of each hunk
        """
        Given a chunk_manifest_pydf, where each record is a chunk_spec (dict),
        1. apply 'func' to each chunk specified by the manifest.
        2. func() will load the chunk and save any results.
        3. returns one record for each func() call, add these to the resulting pydf.

        Args:
            func (Callable): The function to apply to each table specified by each record in self.
            cols:            Reduce scope to a set of cols
            **kwargs: Additional parameters to pass to func

        Returns:
            result_pydf
                      
        """

        result_pydf = Pydf()

        for chunk_spec in self:
            # Apply the function for all chunks specified.
            # Load the specified Pydf table
            # Apply the function to the loaded Pydf
            result_da = func(chunk_spec, **kwargs)
            
            # Update the manifest with information about the resulting chunk
            result_pydf.append(result_da)
            
        return result_pydf        

    
    def groupby(self, 
            colname: str='', 
            colnames: Optional[T_ls]=None,
            omit_nulls: bool=False,         # do not group to values in column that are null ('')
            ) -> Union[Dict[str, 'Pydf'], Dict[Tuple[str, ...], 'Pydf']]:
        """ given a pydf, break into a number of pydf's based on one colname or list of colnames specified. 
            For each discrete value in colname(s), create a pydf table with all cols,
            including colname, and return in a dopydf (dict of pydf) structure.
            If list of colnames is provided, dopydf keys are tuples of the values.
        """
        
        if isinstance(colname, list) and not colnames:
            return self.groupby_cols(colnames=colname)
        elif colnames and not colname:
            if len(colnames) > 1:
                return self.groupby_cols(colnames=colnames)
            else:
                colname = colnames[0]
                # can continue below.
        
        result_dopydf: Dict[str, 'Pydf'] = {}
        
        for da in self:
            fieldval = da[colname]
            if omit_nulls and fieldval=='':
                continue
            
            if fieldval not in result_dopydf:
                result_dopydf[fieldval] = self.clone_empty()
                
            this_pydf = result_dopydf[fieldval]
            this_pydf.record_append(record_da=da)
            result_dopydf[fieldval] = this_pydf
    
        return result_dopydf
    

    def groupby_cols(self, colnames: T_ls) -> Dict[Tuple[str, ...], 'Pydf']:
        """ given a pydf, break into a number of pydf's based on colnames specified. 
            For each discrete value in colname, create a pydf table with all cols,
            including colnames, and return in a dopydf (dict of pydf) structure,
            where the keys are a tuple of the column values.
            
            Examine the records to determine what the values are for the colnames specified.
        """
        
        result_dopydf: Dict[Tuple[str, ...], 'Pydf'] = {}
        
        for da in self:
            fieldval_tuple = tuple(da[colname] for colname in colnames)
            if fieldval_tuple not in result_dopydf:
                result_dopydf[fieldval_tuple] = this_pydf = self.clone_empty()
            
            else:
                this_pydf = result_dopydf[fieldval_tuple]
                
            this_pydf.record_append(record_da=da)
            result_dopydf[fieldval_tuple] = this_pydf
    
        return result_dopydf


    def groupby_cols_reduce(self, 
            groupby_colnames: T_ls, 
            func: Callable[[T_da, Union['Pydf', T_da]], Union[T_da, T_la, 'Pydf']], 
            by: str='row',                                  # determines how the func is applied.
            reduce_cols: Optional[T_la]=None,               # columns included in the reduce operation.
            diagnose: bool = False,
            **kwargs: Any,
            ) -> 'Pydf':
            
        """ 
            Given a pydf, break into a number of pydf's based on values in groupby_colnames. 
            For each group, apply func. to data in reduce_cols.
            returns pydf with one row per group, and keyfield not set.
        """
        # unit test exists.
        """
            
            This can be commonly used when some colnames are important for grouping, while others
            contain values or numeric data that can be reduced.
            
            For example, consider the data table with the following columns:
            
            gender, religion, zipcode, cancer, covid19, gun, auto
            
            The data can be first grouped by the attribute columns gender, religion, zipcode, and then
            then prevalence of difference modes of death can be summed. The result is a pydf with one
            row per unique combination of gender, religion, zipcode. Say we consider just M/F, C/J/I, 
            and two zipcodes 90001, and 90002, this would result in the following rows, where the 
            values in paranthesis are the reduced values for each of the numeric columns, such as the sum.
            
            In general, the number of rows is reduced to the product of number of unique values in each column
            grouped. In this case, there are 2 genders, 3 religions, and 2 zipcodes, resulting in
            2 * 3 * 2 = 12 rows.
            
            groupby_colnames = ['gender', 'religion', 'zipcode']
            reduce_colnames  = ['cancer', 'covid19', 'gun', 'auto']
            
            grouped_and_summed = data_table.groupby_cols_reduce(
                groupby_colnames=['gender', 'religion', 'zipcode'], 
                func = sum_np(),
                by='table',                                     # determines how the func is applied.
                reduce_cols = reduce_colnames,                  # columns included in the reduce operation.
                )

            
            cols = ['gender', 'religion', 'zipcode', 'cancer', 'covid19', 'gun', 'auto']
            lol = [
            ['M', 'C', 90001,  1,  2,  3,  4],
            ['M', 'C', 90001,  5,  6,  7,  8],
            ['M', 'C', 90002,  9, 10, 11, 12],
            ['M', 'C', 90002, 13, 14, 15, 16],
            ['M', 'J', 90001,  1,  2,  3,  4],
            ['M', 'J', 90001, 13, 14, 15, 16],
            ['M', 'J', 90002,  5,  6,  7,  8],
            ['M', 'J', 90002,  9, 10, 11, 12],
            ['M', 'I', 90001, 13, 14, 15, 16],
            ['M', 'I', 90001,  1,  2,  3,  4],
            ['M', 'I', 90002,  4,  3,  2,  1],
            ['M', 'I', 90002,  9, 10, 11, 12],
            ['F', 'C', 90001,  4,  3,  2,  1],
            ['F', 'C', 90001,  5,  6,  7,  8],
            ['F', 'C', 90002,  4,  3,  2,  1],
            ['F', 'C', 90002, 13, 14, 15, 16],
            ['F', 'J', 90001,  4,  3,  2,  1],
            ['F', 'J', 90001,  1,  2,  3,  4],
            ['F', 'J', 90002,  8,  7,  6,  5],
            ['F', 'J', 90002,  1,  2,  3,  4],
            ['F', 'I', 90001,  8,  7,  6,  5],
            ['F', 'I', 90001,  5,  6,  7,  8],
            ['F', 'I', 90002,  8,  7,  6,  5],
            ['F', 'I', 90002, 13, 14, 15, 16],
            ]

            result_lol = [
            ['M', 'C', 90001,  6,  8, 10, 12],
            ['M', 'C', 90002, 21, 24, 26, 18],
            ['M', 'J', 90001, 14, 16, 18, 20],
            ['M', 'J', 90002, 14, 16, 18, 20],
            ['M', 'I', 90001, 14, 16, 18, 20],
            ['M', 'I', 90002, 13, 13, 13, 13],
            ['F', 'C', 90001,  9,  9,  9,  9],
            ['F', 'C', 90002, 17, 17, 17, 17],
            ['F', 'J', 90001,  5,  5,  5,  5],
            ['F', 'J', 90002,  9,  9,  9,  9],
            ['F', 'I', 90001, 13, 13, 13, 13],
            ['F', 'I', 90002, 21, 21, 21, 21],
            ]
            
            This reduction can then be further grouped and summed to create reports or to allow for 
            comparison based on any combination of the subgroups.
            
            
        """
        
        # divide up the table into groups where each group has a unique set of values in groupby_colnames
        # import pdb; pdb.set_trace() #temp
        
        if diagnose:  # pragma: no cover
            utils.sts(f"Starting groupby_cols() of {len(self):,} records.", 3)
            
        grouped_tdopydf = self.groupby_cols(groupby_colnames)
        
        if diagnose:  # pragma: no cover
            utils.sts(f"Total of {len(grouped_tdopydf):,} groups. Reduction starting.", 3)
        
        result_pydf = Pydf(cols=groupby_colnames + reduce_cols)
                
        for coltup, this_pydf in grouped_tdopydf.items():
        
            if not this_pydf:
                # nothing found with this combination of groupby cols.
                continue
                
            # apply the reduction function
            reduction_da = this_pydf.reduce(func, by=by, cols=reduce_cols, **kwargs)
            
            # add back in the groupby cols
            for idx, groupcolname in enumerate(groupby_colnames):
                reduction_da[groupcolname] = coltup[idx]
            
            result_pydf.append(reduction_da)

        if diagnose:  # pragma: no cover
            utils.sts(f"Reduction completed: {len(result_pydf):,} records.", 3)

        return result_pydf
    

    def groupby_reduce(self, 
            colname:str, 
            func: Callable[[T_da, T_da], Union[T_da, T_la]], 
            by: str='row',                                  # determines how the func is applied.
            reduce_cols: Optional[T_la]=None,                      # columns included in the reduce operation.
            **kwargs: Any,
            ) -> 'Pydf':
        """ given a pydf, break into a number of pydf's based on colname specified. 
            For each group, apply callable.
            returns pydf with one row per group, with keyfield the groupby value in colname.
            
        """
        
        grouped_dopydf = self.groupby(colname)
        result_pydf = Pydf(keyfield = colname)
        
        for colval, this_pydf in grouped_dopydf.items():
        
            # maybe remove colname from cols here
        
            reduction_da = this_pydf.reduce(func, by=by, cols=reduce_cols, **kwargs)
            
            # add colname:colval to the dict
            reduction_da = {colname: colval, **reduction_da}
            
            # this will also maintain the kd.
            result_pydf.append(reduction_da)

        return result_pydf

        
    #===================================
    # apply / reduce convenience methods

    def pydf_sum(self, 
            by: str = 'row', 
            cols: Optional[T_la]=None
            ) -> T_da:
            
        return self.reduce(func=Pydf.sum_da, by=by, cols=cols)
    

    def pydf_valuecount(self, 
            by: str = 'row', 
            cols: Optional[T_la]=None
            ) -> T_da:
        """ count values in columns specified and return for each column,
            a dictionary of values and counts for each value in the column
            
            Need a way to specify that blank values will also be counted.
        """
            
        return self.reduce(func=Pydf.count_values_da, by=by, cols=cols)


    def groupsum_pydf(self,
            colname:str, 
            func: Callable[[T_da, T_da, Optional[T_la]], Union[T_da, T_la]], 
            by: str='row',                                  # determines how the func is applied.
            reduce_cols: Optional[T_la]=None,               # columns included in the reduce operation.
            ) -> 'Pydf':
    
        result_pydf = self.groupby_reduce(colname=colname, func=Pydf.sum_da, by=by, reduce_cols=reduce_cols)
        
        return result_pydf


    def set_col2_from_col1_using_regex_select(self, col1: str, col2: str='', regex: str=''):
    
        """ given two cols that already exist, apply regex select to col1 to create col2
            regex should include parens that enclose the desired portion of col1.
        """
        
        # from utilities import utils
    
        def set_row_col2_from_col1_using_regex_select(row_da: T_da, col1: str, col2: str, regex: str) -> T_da:
            row_da[col2] = utils.safe_regex_select(regex, row_da[col1])
            return row_da
            
        if not col2:
            col2 = col1

        self.apply_in_place(lambda row_da: set_row_col2_from_col1_using_regex_select(row_da, col1, col2, regex)) 


    def apply_to_col(self, col: str, func: Callable, **kwargs):
    
        self[:, col] = list(map(func, self[:, col], **kwargs))
        
    # for example:
    #   my_pydf.apply_to_col(col='colname', func=lambda x: re.sub(r'^\D+', '', x))    

    #====================================
    # reduction atomic functions
    
    # requirements for reduction functions:
    #   1. reduction will produce a single dictionary of results, for each pydf chunk.
    #   2. each atomic function will be staticmethod which accepts a single row dictionary, this_da
    #       and contributes to an accum_da. The accum_da is mutated by each row call.
    #   3. the reduction atomic function must be able to deal with combining results
    #       in a pydf where each record is the result of processing one chunk.
    #   4. each atomic function will also accept a cols parameter which identifies which 
    #       columns are to be included in the reduction, if it is not None or []
    #       Otherwise, all columns will be processed. This columns parameter can be
    #       initialized explicitly or using my_pydf.calc_cols(include_cols, exclude_cols, include_dtypes, excluded_dtypes)
    #   5. Even if columns are reduced, the result of the function will include all columns
    #       and non-specified columns will be initialized to '' empty string. This complies
    #       with design goal of always producing a result that will be useful in a report.
    #   6. Therefore, the reduction result may be appended to the pydf if desired.
    
    

    @staticmethod
    def sum_da(row_da: T_da, accum_da: T_da, cols: Optional[T_la]=None, diagnose:bool=False) -> T_da:     # result_da
        """ sum values in row and accum dicts per colunms provided. 
            will safely skip data that can't be summed.
        """
        diagnose = diagnose
        
        cols_list = {}
        
        if cols is None:
            cols_list = []
        elif not isinstance(cols, list):
            cols_list = [cols]
        else:
            cols_list = cols
            
        if len(cols_list) > 10:    
            cols_list_or_dict = dict.fromkeys(cols)
        else:
            cols_list_or_dict = cols_list
            
        for key, value in row_da.items():
            if cols_list_or_dict and key not in cols_list_or_dict:
                # accum_da[key] = ''
                continue

            try:
                if key in accum_da:
                    accum_da[key] += value
                else:
                    accum_da[key] = value
            except Exception:
                pass
        return accum_da


    @staticmethod
    def count_values_da(row_da: T_da, result_dodi: T_dodi, cols: Optional[T_la]=None) -> T_dodi:
        """ incrementally build the result_dodi, which is the valuecounts for each item in row_da.
            can be used to calculate valuecounts over all rows and chunks.
            
            row_da may be scalar values (typically strings that are to be counted)
            but may also be a dodi of totals from a set of chunks that are to be combined.
            
            Intended use is to use this to calculate valuecounts by scanning all rows of a pydf.
            Return a dodi.
            Put those in a pydf table and then scan those combined values and create a singular result.
            
            This is a reducing and accumulating operation. Can be used with pydf.reduce()
            
        """
    
        if cols is None:
            cols_dict = {}
        else:
            cols_dict = dict.fromkeys(cols)
        
        for key, val in row_da.items():
            
            if cols_dict and key not in cols_dict:
                continue

            if key not in result_dodi:
                result_dodi[key] = {}
                
            if val and isinstance(val, dict):
                # val is a dict of values determined in another pass.
                Pydf.sum_dodis(val, result_dodi)
                continue
                
            if val not in result_dodi[key]:
                result_dodi[key][val] = 1
            else:    
                result_dodi[key][val] += 1
        
        return result_dodi
        
                        
    @staticmethod
    def sum_dodis(this_dodi: T_dodi, accum_dodi: T_dodi):
        """ add values for matching keys in this_dodi and accum_dodi.
            sum cases where the keys are the same.
        """
    
        for key, this_di in this_dodi.items():
            if key in accum_dodi:
                Pydf.sum_da(this_di, accum_dodi[key])
            else:
                accum_dodi[key] = this_di

                    
    #===============================================
    # functions not following apply or reduce pattern
    
    # this function does not use normal reduction approach.
    def sum(self, colnames_ls: Optional[T_ls]=None, numeric_only: bool=False) -> dict: # sums_di
        """ total the columns in the table specified, and return a dict of {colname: total,...} 
        
        
            unit tests exist
        """


        if colnames_ls is None:
            cleaned_colnames_ls = list(self.hd.keys())
            cleaned_colidxs_li = list(range(len(cleaned_colnames_ls)))
        elif not (numeric_only and self.dtypes):
            cleaned_colnames_ls = [col for col in colnames_ls if col in self.hd]
            cleaned_colidxs_li = [self.hd[col] for col in cleaned_colnames_ls]  
        else:    
            cleaned_colnames_ls = [col for col in colnames_ls if col in self.hd and self.dtypes.get(col) in [int, float]]
            cleaned_colidxs_li = [self.hd[col] for col in cleaned_colnames_ls]  
        
        sums_d_by_colidx = dict.fromkeys(cleaned_colidxs_li, 0.0)
        
        for la in self.lol:
            for colidx in cleaned_colidxs_li:
                if la[colidx]:
                    if numeric_only:
                        sums_d_by_colidx[colidx] += Pydf._safe_tofloat(la[colidx])
                    else:
                        sums_d_by_colidx[colidx] += float(la[colidx])

        try:
            sums_d = {cleaned_colnames_ls[idx]: sums_d_by_colidx[colidx] for idx, colidx in enumerate(cleaned_colidxs_li)}
        except Exception:
            import pdb; pdb.set_trace() #perm ok
            pass 
        sums_d = utils.set_dict_dtypes(sums_d, self.dtypes)  # type: ignore
        
        return sums_d
        

    def sum_np(self, colnames_ls: Optional[T_ls]=None, ) -> dict: # sums_di
        """ total the columns in the table specified, and return a dict of {colname: total,...}
            This uses NumPy and requires that library, but this is about 3x faster.
            If you have mixed types in your Pydf array, then use colnames to subset the
            columns sent to NumPy to those that contain only numerics and blanks.
            For many numeric operations, convert a set of columns to NumPy
            and work directly with NumPy and then convert back. See to_numpy and from_numpy()
        """
        # unit tests exist
        #   need tests for blanks and subsetting columns.
        
        if not self:
            return {}

        if colnames_ls is None:
            to_sum_pydf = self
            colnames_ls = self.columns()
        else:
            to_sum_pydf = self.from_selected_cols(cols=colnames_ls)
            """ given a list of colnames, create a new pydf of those cols.
                creates as new pydf
            """
        
        # convert those columns to an numpy array.
        nparray = to_sum_pydf.to_numpy()
        
        # sum the columns in the array.
        sum_columns = np.sum(nparray, axis=0)
        
        #convert to a dictionary.
        sums_d = dict(zip(colnames_ls, sum_columns.tolist()))
        
        return sums_d

    
    def valuecounts_for_colname(self, 
            colname: str, 
            sort: bool=False, 
            reverse: bool=True,
            omit_nulls: bool=False,
            ) -> T_di:
        """ given a column of enumerated values, count all unique values in the column 
            and return a dict of valuecounts_di, where the key is each of the unique values
            and the value is the count of that value in the column.
            if sort is true, return the dict sorted from most frequent to least frequently
            detected value.
            unit tests exist
        """

        valuecounts_di: T_di = {}
        
        if colname not in self.hd:
            return {}

        icol = self.hd[colname]
        
        for irow in range(len(self.lol)):
            val = self.lol[irow][icol]
            if val not in valuecounts_di:
                valuecounts_di[val] = 1
            else:
                valuecounts_di[val] += 1

        if omit_nulls:
            utils.safe_del_key(valuecounts_di, '') 
                
        if sort:
            valuecounts_di = dict(sorted(valuecounts_di.items(), key=lambda x: x[1], reverse=reverse))

        return valuecounts_di


    def valuecounts_for_colnames_ls(self, colnames_ls: Optional[T_ls]=None, sort: bool=False, reverse: bool=True) -> T_dodi:
        """ return value counts for a set of columns or all columns if no colnames_ls are provided.
            sort if noted from most prevalent to least in each column.
        """
    
        if not colnames_ls:
            colnames_ls = self.columns()
            
        colnames_ls = cast(T_ls, colnames_ls)    

        valuecounts_dodi: T_dodi = {}
        
        for colname in colnames_ls:
            valuecounts_dodi[colname] = \
                self.valuecounts_for_colname(colname, sort=sort, reverse=reverse)

        return valuecounts_dodi
    

    def valuecounts_for_colname_selectedby_colname(
            self, 
            colname: str, 
            selectedby_colname: str, 
            selectedby_colvalue: str,
            sort: bool = False, 
            reverse: bool = True,
            ) -> T_di:
        """ Create valuecounts for each colname for all rows where
            selectedby_colvalue is found in selectedby_colname
        """    
    

        valuecounts_di: T_di = {}
        
        if colname not in self.hd or selectedby_colname not in self.hd:
            return {}

        icol = self.hd[colname]
        selectedby_colidx = self.hd[selectedby_colname]
        
        for irow in range(len(self.lol)):
            val = self.lol[irow][selectedby_colidx]
            if val != selectedby_colvalue:
                continue
            val = self.lol[irow][icol]    
            if val not in valuecounts_di:
                valuecounts_di[val] = 1
            else:
                valuecounts_di[val] += 1

        if sort:
            valuecounts_di = dict(sorted(valuecounts_di.items(), key=lambda x: x[1], reverse=reverse))

        return valuecounts_di
        

    def valuecounts_for_colnames_ls_selectedby_colname(self, 
            colnames_ls: Optional[T_ls]=None,
            selectedby_colname: str = '', 
            selectedby_colvalue: str = '',
            sort: bool = False, 
            reverse: bool = True,
            ) -> T_dodi:
            
        """ Create valuecounts for each column in colnames_ls (or all columns if None)
            when selectedby_colvalue is found in selectedby_colname
            
            
        """    
    

        if not colnames_ls:
            colnames_ls = self.columns()
            
        colnames_ls = cast(T_ls, colnames_ls)    

        valuecounts_dodi: T_dodi = {}
        
        for colname in colnames_ls:
            valuecounts_dodi[colname] = \
                self.valuecounts_for_colname_selectedby_colname(
                        colname,
                        selectedby_colname, 
                        selectedby_colvalue,
                        sort=sort, 
                        reverse=reverse,
                        )

        return valuecounts_dodi


    def valuecounts_for_colname1_groupedby_colname2(self,
            colname1: str,
            groupedby_colname2: str, 
            sort: bool = False, 
            reverse: bool = True,
            ) -> T_dodi:
        """ frequently, two columns are related, and it may be required 
            that one is single-valued for each item in the other.
            This function does a single scan of the data and accumulates
            value counts for colname1 for each value in groupedby colname2.
            Result is dodi, with the first key being the groupby values
            and the second being the values counted in colname1.
        """
            

        valuecounts_dodi: T_dodi = {}
        
        if colname1 not in self.hd or groupedby_colname2 not in self.hd:
            return {}

        icol1 = self.hd[colname1]
        groupedby_col2idx = self.hd[groupedby_colname2]
        
        for row in self.lol:
            groupval = row[groupedby_col2idx]
            val = row[icol1]    
            if groupval not in valuecounts_dodi:
                valuecounts_dodi[groupval] = {}
            valuecounts_di: T_di = valuecounts_dodi[groupval]    
            if val not in valuecounts_di:
                valuecounts_di[val] = 1
            else:
                valuecounts_di[val] += 1

        if sort:
            for group, valuecounts_di in valuecounts_dodi.items():
                valuecounts_dodi[group] = dict(sorted(valuecounts_di.items(), key=lambda x: x[1], reverse=reverse))

        return valuecounts_dodi

    

    def gen_stats_pydf(self, col_def_lot: T_lota) -> T_doda:

        info_dod = {}

        # from utilities import utils

        for col_def_ta in col_def_lot:
            col_name, col_dtype, col_format, col_profile = col_def_ta
            
            col_data_la = self.col(col_name)
            
            info_dod[col_name] = utils.list_stats(col_data_la, profile=col_profile)
            
        return info_dod

   
    def transpose(self, new_keyfield:str='', new_cols:Optional[T_la]=None, include_header:bool = False) -> 'Pydf':
        """ 
        This implementation uses the built-in zip(*self.lol) to transpose the rows and columns efficiently. 
        The resulting transposed data is then used to create a new Pydf instance.
    
        Args:
        - new_cols (list): names of the new columns. If include_header is True, this will be the first column.
        - new_keyfield (str): The new keyfield to be used in the transposed Pydf.
        - include_header (bool): indicates if the column names, if defined, will also be included
                        and will become the first column in the result

        Returns:
        - Pydf: A new Pydf instance with transposed data and optional new keyfield.
        
        """

        if not new_cols:
            new_cols = ['key'] + Pydf._generate_spreadsheet_column_names_list(num_cols=len(self.lol))

        # transpose the array
        new_lol = [list(row) for row in zip(*self.lol)]
        
        if include_header:
            # add a new first column which will be the old column names row.
            # from utilities import utils
            
            new_lol = utils.insert_col_in_lol_at_icol(icol=0, col_la=self.columns(), lol=new_lol)
        
        return Pydf(lol=new_lol, name=self.name, keyfield=new_keyfield, cols=new_cols, use_copy=True)        



    #===============================
    # reporting

    def md_pydf_table_snippet(
            self, 
            ) -> str:
        """ provide an abbreviated md table given a pydf representation """
        
        return self.to_md(
                max_rows        = self.md_max_rows, 
                max_cols        = self.md_max_cols, 
                shorten_text    = True, 
                max_text_len    = 80, 
                smart_fmt       = False, 
                include_summary = True,
                )

    # the following alias is defind at the bottom of this file.
    # Pydf.md_pydf_table = Pydf.to_md

    def to_md(
            self, 
            max_rows:       int     = 0,         # limit the maximum number of row by keeping leading and trailing rows.
            max_cols:       int     = 0,         # limit the maximum number of cols by keeping leading and trailing cols.
            just:           str     = '',        # provide the justification for each column, using <, ^, > meaning left, center, right justified.
            shorten_text:   bool    = True,      # if the text in any field is more than the max_text_len, then shorten by keeping the ends and redacting the center text.
            max_text_len:   int     = 80,        # see above.
            smart_fmt:      bool    = False,     # if columns are numeric, then limit the number of figures right of the decimal to "smart" numbers.
            include_summary: bool   = False,     # include a one-line summary after the table.
            disp_cols:      Optional[T_ls]=None, # use these column names instead of those defined in pydf.
            ) -> str:
        """ provide an full md table given a pydf representation """

        pydf_lol = self.pydf_to_lol_summary(max_rows=max_rows, max_cols=max_cols, disp_cols=disp_cols)
        
        header_exists = bool(self.hd)
        
        mdstr = md.md_lol_table(pydf_lol, 
            header              = None, 
            includes_header     = header_exists, 
            just                = just or ('>' * len(self.hd)), 
            omit_header         = not header_exists, 
            shorten_text        = shorten_text, 
            max_text_len        = max_text_len, 
            smart_fmt           = smart_fmt,
            
            )
        if include_summary:    
            mdstr += f"\n\[{len(self.lol)} rows x {len(self.hd)} cols; keyfield={self.keyfield}; {len(self.kd)} keys ] ({self.__class__.__name__})\n"
        return mdstr

    def pydf_to_lol_summary(self, max_rows: int=10, max_cols: int=10, disp_cols:Optional[T_ls]=None) -> T_lola:
    
        # from utilities import utils

        # first build a basic summary
        if disp_cols:
            colnames_ls = disp_cols
        else:
            colnames_ls = list(self.hd.keys())
            
        result_lol = self.lol
        if colnames_ls:
            result_lol = [colnames_ls] + result_lol

        # no limits, return summary.
        if not max_rows and not max_cols:
            return result_lol

        num_rows    = len(self.lol) if self.lol else 0
        num_cols    = self.num_cols()

        if max_rows and num_rows <= max_rows:
            # Get all the rows, but potentially limit columns
            result_lol = utils.reduce_lol_cols(result_lol, max_cols=max_cols)
        
        else:
            # Get the first and last portion of rows
            
            first_lol   = self.lol[:max_rows//2]
            last_lol    = self.lol[-(max_rows//2):]
            divider_lol = [['...'] * num_cols]
            
            result_lol  = [colnames_ls] + first_lol + divider_lol + last_lol
            result_lol = utils.reduce_lol_cols(result_lol, max_cols=max_cols)

        return result_lol
        
    @staticmethod
    def dict_to_md(da: T_da, cols: Optional[T_ls]=None, just: str='<<') -> str:
        """ this convenience method can be used for interactive inspection of a dict,
            by placing the dict keys in the first column and the values in the second
            column. Much easier to work with than just using print(da).
            
            To use this interactively, use print(Pydf.dict_to_md(my_da))
        """
        if not cols:
            cols = ['key', 'value']
    
        return Pydf.from_lod_to_cols([da], cols=cols).to_md(just=just)
            
        
    #=========================================
    #  Reporting Convenience Methods

    def value_counts_pydf(self, 
            colname: str,                       # column name to include in the value_counts table
            sort: bool=False,                   # sort values in the category
            reverse: bool=True,                 # reverse the sort
            include_total: bool=False,          #
            omit_nulls: bool=False,             # set to true if '' should be omitted.            
            ) -> 'Pydf':
        """ create a values count pydf of the results of value counts analysis of one column, colname.
            The result is a pydf table with two columns.
            Left column has the values, and the right column has the counts for each value.
            column names are [colname, 'counts'] in the result. These can be changed later if they are not 
            output when used with multiple columns may be useful but only if they have the same set of values.
            provides a total line if "include_sum" is true.
        """
            
        value_counts_di   = self.valuecounts_for_colname(colname=colname, sort=sort, reverse=reverse)
        
        if omit_nulls:
            utils.safe_del_key(value_counts_di, '') 

        value_counts_pydf = Pydf.from_lod_to_cols([value_counts_di], cols=[colname, 'counts'])

        if include_total:
            value_counts_pydf.append({colname: ' **Total** ', 'counts': sum(value_counts_pydf[:,'counts'])})
        return value_counts_pydf


Pydf.md_pydf_table = Pydf.to_md            


# DO NOT DELETE THESE LINES.
# these are required to define these.
# these were required before making a full package that is pip loaded.
#T_pydf = Pydf
#T_dopydf = Dict[Union[str, Tuple[str, ...]], Optional[T_pydf]]
