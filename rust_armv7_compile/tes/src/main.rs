use std::collections::HashMap;
extern crate reqwest;

fn main() -> Result<(), reqwest::Error> {
    let resp = reqwest::blocking::get("https://api.ipify.org?format=json")?
        .json::<HashMap<String, String>>();
    match resp {
        Ok(ip) => {
            println!("{:#?}", ip);
            Ok(())
        }
        Err(err) => Err(err),
    }
}
