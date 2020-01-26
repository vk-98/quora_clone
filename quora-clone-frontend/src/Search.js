import React from "react"
import { render } from "react-dom"
import { Input } from 'antd';

const { Search } = Input;

function SearchBar(){

        return(

            <div>
      
            <br />
            <Search placeholder="input search text" onSearch={value => console.log(value)}   enterButton />
            <br />
              
          </div>



        )
    
}
export default SearchBar;
