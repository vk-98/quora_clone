import React from "react"


import CssBaseline from '@material-ui/core/CssBaseline';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';


import Button from '@material-ui/core/Button';




const useStyles = makeStyles(theme => ({
    container: {
      display: 'flex',
      flexWrap: 'wrap',
    },
    textField: {
      marginLeft: theme.spacing(1),
      marginRight: theme.spacing(1),
      width: 2000,
    },
    root: {
        '& > *': {
          margin: theme.spacing(1),
          width: 200,
        },
      },
  }));
  

function Ques() {
    const classes = useStyles();
    return (

        
        <React.Fragment>
        <CssBaseline />
        <Container maxWidth="600px" maxHeight="300px">
       
        <form className={classes.root} noValidate autoComplete="off">
       <TextField id="outlined-basic" label="Ask Question" variant="outlined" />
       <Button variant="contained" color="primary" disableElevation>
      Submit
    </Button>
 
  </form>
        </Container>
      </React.Fragment>
    )
}

export default Ques