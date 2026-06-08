
import System.Random (newStdGen, randomRs)
import Data.List (nub)

charset :: String
charset = concat [['a'..'z'], ['A'..'Z'], ['0'..'9'], "!@#$%"]

pick :: Int -> String -> [Int] -> String
pick 0 _ _ = []
pick n cs (r:rs) = cs !! (r `mod` length cs) : pick (n-1) cs rs

main :: IO ()
main = do
  gen <- newStdGen
  let rs = randomRs (0, 10^6) gen
  putStrLn $ pick 16 charset rs
