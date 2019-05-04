module Lib
    ( someFunc
    ) where

someFunc :: IO ()
someFunc = putStrLn $ show (prob1 3 5 1 1000)


prob1 div1 div2 start end = helper 0 start where
    helper acc curr | curr == end          = acc
    helper acc curr | curr `mod` div1 == 0 = helper (acc + curr) (curr + 1)
    helper acc curr | curr `mod` div2 == 0 = helper (acc + curr) (curr + 1)
    helper acc curr                        = helper (acc) (curr + 1)
