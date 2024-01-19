use ndarray::{Array, Ix1,Ix2};
use rand::Rng;

fn main(){
    let text = std::fs::read_to_string("../input.txt").expect("Error reading file");
    //reading the unique characters in the file
    let chars :Vec<char> = text.chars().collect();
    let chars :Vec<_> = chars.iter().cloned().collect();    
    //println!("chars: {:?}", chars.iter().take(1000).collect::<Vec<_>>());

}
