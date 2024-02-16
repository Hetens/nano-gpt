use ndarray::{Array, Ix1, Ix2};
use rand::Rng;
use std::collections::HashMap;

fn main() {
    let text = std::fs::read_to_string("../input.txt").expect("Error reading file");
    // reading the unique characters in the file
    let chars: Vec<char> = text.chars().collect();
    let chars: Vec<_> = chars.iter().cloned().collect();
    println!("chars: {:?}", chars.iter().take(1000).collect::<Vec<_>>());

    // encoder decoder maps
    let vocab_size = chars.len();
    let stoi: HashMap<_, _> = chars.iter().cloned().enumerate().collect();
    let itos: HashMap<_, _> = chars.iter().cloned().enumerate().collect();

    // encode and decode functions
    let encode = |s: &str| s.chars().map(|c| *stoi.get(&c).unwrap()).collect::<Vec<_>>();
    let decode = |v: &Vec<usize>| v.iter().map(|&i| *itos.get(&i).unwrap()).collect::<String>();

    // encoding the dataset
    let data: Vec<_> = encode(&text);

    // Example: decoding the encoded data
    let decoded_text = decode(&data);
    println!("Decoded Text: {:?}", decoded_text);
}
