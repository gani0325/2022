let Subset = `
## Subset
Extract subset data with the conditions you want.
* DataFrame : Two-dimensional, size-mutable, potentially heterogeneous tabular data.
* Method
    * iloc : Purely integer-location based indexing for selection by position.
    * loc : Access a group of rows and columns by label(s) or a boolean array.
    * query : Query the columns of a DataFrame with a boolean expression.
* Allocate to : declare variable

### Row/Column Subset View
Select Options
* Indexing : choose row index
* Slicing : input start index, end index
* Condition
    * choose row name, operation, value
    * value : It can be variable or number
    * if you select 'Text' checkbox, value can get string type
`


const obj  = {    
    'Subset' : `
    ## Subset
    Extract subset data with the conditions you want.
    * DataFrame : Two-dimensional, size-mutable, potentially heterogeneous tabular data.
    * Method
        * iloc : Purely integer-location based indexing for selection by position.
        * loc : Access a group of rows and columns by label(s) or a boolean array.
        * query : Query the columns of a DataFrame with a boolean expression.
    * Allocate to : declare variable
    
    ### Row/Column Subset View
    Select Options
    * Indexing : choose row index
    * Slicing : input start index, end index
    * Condition
        * choose row name, operation, value
        * value : It can be variable or number
        * if you select 'Text' checkbox, value can get string type
    `,
    'File' :'File test',
    'Upload' :'Upload test'
};

const str = JSON.stringify(obj);
console.log(obj);
console.log("-----------------------------------------------------");
console.log(Subset);





// result
// {
//     Subset: '\n' +
//       '    ## Subset\n' +
//       '    Extract subset data with the conditions you want.\n' +
//       '    * DataFrame : Two-dimensional, size-mutable, potentially heterogeneous tabular data.\n' +
//       '    * Method\n' +
//       '        * iloc : Purely integer-location based indexing for selection by position.\n' +
//       '        * loc : Access a group of rows and columns by label(s) or a boolean array.\n' +
//       '        * query : Query the columns of a DataFrame with a boolean expression.\n' +
//       '    * Allocate to : declare variable\n' +
//       '    \n' +
//       '    ### Row/Column Subset View\n' +
//       '    Select Options\n' +
//       '    * Indexing : choose row index\n' +
//       '    * Slicing : input start index, end index\n' +
//       '    * Condition\n' +
//       '        * choose row name, operation, value\n' +
//       '        * value : It can be variable or number\n' +
//       "        * if you select 'Text' checkbox, value can get string type\n" +
//       '    ',
//     File: 'File test',
//     Upload: 'Upload test'
//   }
//   -----------------------------------------------------
  
//   ## Subset
//   Extract subset data with the conditions you want.
//   * DataFrame : Two-dimensional, size-mutable, potentially heterogeneous tabular data.
//   * Method
//       * iloc : Purely integer-location based indexing for selection by position.
//       * loc : Access a group of rows and columns by label(s) or a boolean array.
//       * query : Query the columns of a DataFrame with a boolean expression.
//   * Allocate to : declare variable
  
//   ### Row/Column Subset View
//   Select Options
//   * Indexing : choose row index
//   * Slicing : input start index, end index
//   * Condition
//       * choose row name, operation, value
//       * value : It can be variable or number
//       * if you select 'Text' checkbox, value can get string type
  
